import datetime
# import re

from django.utils import timezone
from django.db import models
from ..users.models import User
# from django import forms
# from django.forms import Form, ModelForm, ModelChoiceField, CharField
# from django.utils.html import mark_safe
# from django.core.exceptions import ValidationError


MAX_PRICE_DIGITS = 10
OK_STATE = 'OK'


class Category(models.Model):

    """Robot, motor, sensor, ..."""
    name = models.CharField(max_length=70)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    def count_usage(self):
        return len(Reference.objects.filter(category=self))


class Reference(models.Model):

    """Reference of the object (MX-64, Poppy-humanoid, Thymio)"""
    name = models.CharField(max_length=70)  # MX-64, Poppy-humanoid, ...
    category = models.ForeignKey(Category)
    description = models.TextField(null=True, blank=True)
    image = models.FileField(upload_to='%Y/%m/%d', null=True, blank=True)

    def __str__(self):
        return "%s %s" % (self.category.name, self.name)

    def count_usage(self):
        return len(Item.objects.filter(reference=self))


class Item(models.Model):

    """unique object designed by its name or its primary key
        Example : poppy-white, darth-poppy, """
    name = models.CharField(
        max_length=70, blank=True, help_text="Can be let blank for little items like motors")  # Poppy-pink, poppy-white, ...
    reference = models.ForeignKey(Reference)
    parent_item = models.ForeignKey("Item", blank=True, null=True)
    description = models.TextField(null=True, blank=True, help_text="Additional information about this item")
    image = models.FileField(upload_to='%Y/%m/%d', null=True, blank=True)
    price = models.DecimalField(
        max_digits=MAX_PRICE_DIGITS,
        decimal_places=2,
        default=0)
    added = models.DateTimeField(auto_now_add=True, editable=False)
    last_edit = models.DateTimeField(auto_now=True, editable=False)
    active = models.BooleanField(default=True)

    def __str__(self):
        if self.name != "":
            return "[%s] %s" % (self.reference.__str__(), self.name)
        else:
            return "[%s] %s" % (self.reference.__str__(), self.pk)

    def sub_items_number(self):
        return len(Item.objects.filter(parent_item=self))

    def last_event(self):
        if not hasattr(self, '_cached_last_event'):
            try:
                self._cached_last_event = Item.objects.filter(
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
            return str(state)

    # Add a Signal
    # def initiate_state(self, state=OK_STATE):
    #     state_obj = State.objects.get(name=state)
    #     init_evt = ItemEvent(
    #         item=self,
    #         state=state_obj,
    #         start_date=datetime.now(),
    #         start_time=datetime.now(),
    #         description='New motor.',
    #     )
    #     init_evt.save()


# class WorkingState(models.Model):

#     """Working condition of an item.
#         example : REPARATION, BROKEN, WORKING
#     """
#     name = models.CharField(max_length=200, unique=True)
#     description = models.TextField(null=True, blank=True, help_text="Additional information about this state")

#     def __str__(self):
#         return "%s : %s" % (self.name, self.description)


class CommonEvent(models.Model):

    """ Abstract class for Loan and State"""
    creator = models.ForeignKey(User, related_name='%(class)s_event_created',
                                on_delete=models.PROTECT,
                                help_text="User who create this event",
                                null=True)
    is_active = models.BooleanField('active', default=True)
    creation_date = models.DateTimeField('creation date', default=timezone.now)
    last_modification_date = models.DateTimeField('last modification date', default=timezone.now)
    passived_date = models.DateTimeField('passived date', null=True, blank=True, default=None,
                                         help_text="Date were this state became inactive. Automatically set when the is_active field become unchecked.")
    description = models.TextField(null=True, blank=True, help_text="Additional information about this state")

    class Meta:
        abstract = True


class State(CommonEvent):

    """General state of an Item
    """
    WORKS = 'OK'
    BROKEN = 'HS'
    REPARATION = 'RE'
    TO_CHECK = 'TC'
    WORKING_STATE = (
        (WORKS, 'Works well'),
        (BROKEN, 'Broken'),
        (REPARATION, 'In reparation'),
        (TO_CHECK, 'Undetermined'))

    working_state = models.CharField(max_length=2,
                                     choices=WORKING_STATE,
                                     default=WORKS)

    def save(self, *args, **kwargs):
        if not self.is_active:
            self.passived_date = timezone.now

        self.last_modification_date = timezone.now
        # else:
        # TODO checked unicity of active state for an Item
        super(State, self).save(*args, **kwargs)


class Loan(CommonEvent):

    """ Manage the way an user can borrow an Item """
    LOW = 0
    NORMAL = 1
    HIGH = 3

    PRIORITIES = (
        (LOW, 'Low'),
        (NORMAL, 'Normal'),
        (HIGH, 'High'),
    )

    priority = models.IntegerField(
        default=NORMAL, choices=PRIORITIES,
        help_text="Priority of the loan. Only staff renter should have high priority")
    renter = models.ForeignKey(User,
                               on_delete=models.PROTECT,
                               help_text="User who borrow the Item")
    items = models.ManyToManyField(Item, help_text="Items loaned by an user")
    starting_date = models.DateTimeField('loan starting date', help_text="Starting date of the loan")
    ending_date = models.DateTimeField('loan ending date', help_text="Ending date of the loan")

    def __str__(self):
        items_str = [item.name for item in self.items.all()]
        return "[%s] %s for %s" % (self.PRIORITIES[self.priority][1], ' - '.join(items_str), self.renter)

 #   def save(self, *args, **kwargs):
 #       if not self.is_active:
 #          self.passived_date = timezone.now

 #       self.last_modification_date = timezone.now
        # else:
        # TODO checked unicity of active state for an Item
        # super(Loan, self).save(*args, **kwargs)
#


# ################################################################################


# class MotorTypeForm(forms.Form):
#     name = forms.CharField(max_length=200)
#     price = forms.DecimalField(
#         max_digits=MAX_PRICE_DIGITS,
#         decimal_places=2,
#     )


# class RobotForm(ModelForm):

#     class Meta:
#         model = Robot
#         exclude = {'active'}
# widgets = {'date' :  SelectDateWidget()}


# class EditRobotForm(forms.Form):
#     name = forms.CharField()
#     date = forms.DateTimeField()
#     image = forms.FileField(required=False)


# class SlotForm(ModelForm):

#     class Meta:
#         model = Slot
#         exclude = ('robot',)

#     def __init__(self, *args, **kwargs):
#         super(SlotForm, self).__init__(*args, **kwargs)
#         self.fields['name'].label = 'Item description'


# class MotorForm(ModelForm):

#     class Meta:
#         model = Motor

#     def __init__(self, *args, **kwargs):
#         super(MotorForm, self).__init__(*args, **kwargs)
#         self.fields['name'].initial = Motor.get_free_name()


# TODO Move widgets to an other file (26/09/2012)

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
# "        $('#%s').calendricalDate({" % html_id,
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
# "        $('#%s').calendricalTime({" % html_id,
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
# verbose_name = 'e-mail ")
