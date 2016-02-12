from datetime import datetime
import re

from django.db import models
from django import forms
from django.forms import Form, ModelForm, ModelChoiceField, CharField
from django.utils.html import mark_safe
from django.core.exceptions import ValidationError


MAX_PRICE_DIGITS = 10
OK_STATE = 'OK'


class Robot(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateField('date creation', default=datetime.now())
    time = models.TimeField(default=datetime.now())
    image = models.FileField(upload_to='%Y/%m/%d',
            null=True, blank=True)
    active = models.BooleanField(default=True)
    description = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return self.name

    def nb_slots(self):
        return len(Slot.objects.filter(robot=self))


class MotorType(models.Model):
    name = models.CharField(max_length=200, unique=True)
    price = models.DecimalField(
            max_digits=MAX_PRICE_DIGITS,
            decimal_places=2,
            default=0)

    def __unicode__(self):
        return self.name


class Slot(models.Model):
    robot = models.ForeignKey(Robot)
    kind = models.ForeignKey(MotorType)
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name

    def clean(self):
        if Slot.objects.filter(robot=self.robot
                ).filter(name=self.name
                        ).exclude(pk=self.id):
            raise ValidationError(
                    "A slot already exists on robot %s with name %s"
                    % (self.robot, self.name)
                    )


class Location(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name


class State(models.Model):
    name = models.CharField(max_length=40, unique=True)

    def __unicode__(self):
        return self.name

    def get_style(self):
        return 'state_' + re.sub(r"[^\w]", "_", self.name).lower()


# TODO Use name as id and hard-code nomenclature convention (20/09/2012)
class Motor(models.Model):
    kind = models.ForeignKey(MotorType)
    name = models.CharField(max_length=50, unique=True, blank=False)

    def __unicode__(self):
        return "[" + self.kind.name + "] " + self.name

    def last_event(self):
        if not hasattr(self, '_cached_last_event'):
            try:
                self._cached_last_event = MotorEvent.objects.filter(
                        device=self).order_by('date', 'time').reverse()[0]
            except IndexError:
                self._cached_last_event = None
        return self._cached_last_event

    def current_state(self):
        evt = self.last_event()
        if evt is None:
            return None
        else:
            return evt.state

    def current_state_style(self):
        state = self.current_state()
        if state is None:
            return 'state_unknown'
        else:
            return state.get_style()

    def count_usage(self):
        return len(Association.objects.filter(device=self))

    def current_association(self):
        assocs = Association.objects.filter(device=self, end_date=None)
        return assocs[0] if assocs else None

    def initiate_state(self, state=OK_STATE):
        state_obj = State.objects.get(name=state)
        init_evt = MotorEvent(
                device=self,
                state=state_obj,
                date=datetime.now(),
                time=datetime.now(),
                description='New motor.',
                )
        init_evt.save()

    @classmethod
    def get_free_name(cls):
        # Get all names that are integers
        ints = [int(m.name) for m in cls.objects.all() if m.name.isdigit()]
        if len(ints) == 0:
            next_nb = 1
        else:
            next_nb = max(ints) + 1
        new_name = "%04d" % next_nb
        # Convention requires motor names to be 4 digits
        if len(new_name) < 4:
            new_name = ' ' * (4 - len(new_name)) + new_name
        return new_name

    @classmethod
    def get_free_motors(cls, kind=None):
        assocs = Association.objects.filter(end_date=None)
        if kind is None:
            qset = Motor.objects
        else:
            qset = Motor.objects.filter(kind=kind)
        return qset.exclude(id__in=[o.device.id for o in assocs])


# This is more to be understood as a change in motor state
class MotorEvent(models.Model):
    device = models.ForeignKey(Motor)
    state = models.ForeignKey(State)
    date = models.DateField(default=datetime.now())
    time = models.TimeField(default=datetime.now())
    description = models.TextField()
    # e.g. Why is the motor broken ? How was it repaired ?


class Association(models.Model):
    device = models.ForeignKey(Motor)
    slot = models.ForeignKey(Slot)
    start_date = models.DateField(default=datetime.now())
    start_time = models.TimeField(default=datetime.now())
    end_date = models.DateField(null=True)
    end_time = models.TimeField(null=True)

    def __unicode__(self):
        return "[" + self.device.kind.name + "] : " + self.device.name


# TODO add protection against multiple active associations for motors and
# slots (26/09/2012)


class MotorTypeForm(forms.Form):
    name = forms.CharField(max_length=200)
    price = forms.DecimalField(
            max_digits=MAX_PRICE_DIGITS,
            decimal_places=2,
            )


class RobotForm(ModelForm):

    class Meta:
        model = Robot
        exclude = {'active'}
#        widgets = {'date' :  SelectDateWidget()}


class EditRobotForm(forms.Form):
    name = forms.CharField()
    date = forms.DateTimeField()
    image = forms.FileField(required=False)


class SlotForm(ModelForm):

    class Meta:
        model = Slot
        exclude = ('robot',)

    def __init__(self, *args, **kwargs):
        super(SlotForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = 'Item description'


# class MotorForm(ModelForm):

#     class Meta:
#         model = Motor

#     def __init__(self, *args, **kwargs):
#         super(MotorForm, self).__init__(*args, **kwargs)
#         self.fields['name'].initial = Motor.get_free_name()


# # TODO Move widgets to an other file (26/09/2012)

# class CalandarWidget(forms.DateInput):

#     def render(self, name, value, attrs=None):
#         if attrs:
#             if 'class' in attrs:
#                 attrs['class'] += ' small'
#             else:
#                 attrs['class'] = 'small'
#         html_id = attrs['id'] if 'id' in attrs else 'date'
#         field = super(CalandarWidget, self).render(name, value, attrs=attrs)
#         html = "\n".join([
#             field,
#             "<script type='text/javascript'>",
#             "    $(document).ready(function() {",
#             "        $('#%s').calendricalDate({" % html_id,
#             "            usa: true",
#             "        });",
#             "    });",
#             "</script>",
#             ])
#         return mark_safe(html)


# class TimeWidget(forms.TimeInput):

#     def render(self, name, value, attrs=None):
#         if attrs:
#             if 'class' in attrs:
#                 attrs['class'] += ' small'
#             else:
#                 attrs['class'] = 'small'
#         html_id = attrs['id'] if 'id' in attrs else 'date'
#         field = super(TimeWidget, self).render(name, value, attrs=attrs)
#         html = "\n".join([
#             field,
#             "<script type='text/javascript'>",
#             "    $(document).ready(function() {",
#             "        $('#%s').calendricalTime({" % html_id,
#             "            isoTime: true",
#             "        });",
#             "    });",
#             "</script>",
#             ])
#         return mark_safe(html)


# class DeviceChoiceField(ModelChoiceField):
#     """Displays device status in choices.
#     """

#     def __init__(self, display_kind=False):
#         super(DeviceChoiceField, self).__init__(Motor)
#         self._display_kind = display_kind

#     def label_from_instance(self, motor):
#         if self._display_kind:
#             return "%s (%s) [%s]" % (motor.name, motor.kind,
#                                      motor.current_state())
#         else:
#             return "%s [%s]" % (motor.name, motor.current_state())


# class ChoseDeviceForm(Form):

#     device = DeviceChoiceField(display_kind=True)

#     def __init__(self, *args, **kwargs):
#         super(ChoseDeviceForm, self).__init__(*args, **kwargs)
#         self.fields['device'].queryset = Motor.get_free_motors()


# class AssociationForm(ModelForm):
#     device = DeviceChoiceField()

#     class Meta:
#         model = Association
#         fields = ('device', 'start_date', 'start_time')
#         widgets = {
#                 'start_date': CalandarWidget(attrs={
#                     'title': 'Start date'
#                     }),
#                 'start_time': TimeWidget(attrs={
#                     'title': 'Start time'
#                     }),
#                 'device': forms.Select(attrs={
#                     'class': 'small',
#                     }),
#                 }

#     def __init__(self, slot, *args, **kwargs):
#         super(AssociationForm, self).__init__(*args, **kwargs)
#         self.slot = slot
#         self.fields['device'].queryset = Motor.get_free_motors(slot.kind)

#     def clean_device(self):
#         device = self.cleaned_data['device']
#         required = self.slot.kind
#         if device.kind != required:
#             raise forms.ValidationError(
#                     "The given device has wrong kind (%s) for this slot (%s)."
#                     % (device.kind, required))
#         return device

#     def save(self):
#         motor = self.cleaned_data['device']
#         start_date = self.cleaned_data['start_date']
#         start_time = self.cleaned_data['start_time']
#         assoc = Association(device=motor, slot=self.slot,
#                             start_date=start_date, start_time=start_time)
#         assoc.save()
#         return assoc


# class AssociationNewMotorForm(ModelForm):
#     motor_name = CharField(max_length=200)

#     class Meta:
#         model = Association
#         fields = ('start_date', 'start_time')
#         widgets = {
#                 'start_date': CalandarWidget(attrs={
#                     'title': 'Start date'
#                     }),
#                 'start_time': TimeWidget(attrs={
#                     'title': 'Start time'
#                     }),
#                 }

#     def __init__(self, slot, *args, **kwargs):
#         super(AssociationNewMotorForm, self).__init__(*args, **kwargs)
#         self.slot = slot
#         self.fields['motor_name'].initial = Motor.get_free_name()
#         self.fields['motor_name'].label = 'New device name'

#     def clean_motor_name(self):
#         motor = Motor(name=self.cleaned_data['motor_name'],
#                 kind=self.slot.kind)
#         motor.full_clean()
#         return motor.name

#     def save(self):
#         motor = Motor(name=self.cleaned_data['motor_name'],
#                 kind=self.slot.kind)
#         motor.save()
#         motor.initiate_state()
#         start_date = self.cleaned_data['start_date']
#         start_time = self.cleaned_data['start_time']
#         assoc = Association(device=motor, slot=self.slot,
#                             start_date=start_date, start_time=start_time)
#         assoc.save()
#         return assoc


# class MotorEventForm(ModelForm):

#     class Meta:
#         model = MotorEvent
#         exclude = {'device', }

#@login_required
#verbose_name = 'e-mail ")
