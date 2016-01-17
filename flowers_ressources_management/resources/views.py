from datetime import datetime

from django.shortcuts import render, render_to_response, Http404, HttpResponseRedirect
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.template.context import RequestContext



# def logout_mm(request):
#     logout(request)
#     return render_to_response('login.html')


# def index(request):
#     login_page_args = {}
#     if request.method == 'POST':
#         # Handle authentification
#         name = request.POST['username']
#         pswd = request.POST['password']
#         user = authenticate(username=name, password=pswd)
#         if user is not None:
#             login(request, user)
#         else:
#             login_page_args['error'] = 'on'
#     # Render page
#     if request.user.is_authenticated():
#         all_robots = Robot.objects.all().order_by('name')
#         return render_to_response('robots.html', {'robots': all_robots})
#     else:
#         return render_to_response('login.html', login_page_args)


# @login_required
# def robot_detail(request, robot_id):
#     try:
#         p = Robot.objects.get(pk=robot_id)
#     except Robot.DoesNotExist:
#         raise Http404
#     slots = Slot.objects.filter(robot=robot_id)
#     price = 0
#     for slot in slots:
#         price = price + slot.kind.price
#         assoc = Association.objects.filter(slot=slot, end_time=None)
#         # WTF ?
#         if len(assoc) > 0:
#             slot.assoc = assoc[0]
#         else:
#             slot.assoc = ""
#     form = ChoseDeviceForm()
#     return render_to_response('robot.html',
#             context_instance=RequestContext(request, {
#                 'robot': p,
#                 'slots': slots,
#                 'robot_id': robot_id,
#                 'price': price,
#                 'form': form,
#                 }))


# @login_required
# def robots(request):
#     all_robots = Robot.objects.all()
#     return render_to_response('robots.html', {'robots': all_robots})


# @login_required
# def edit_robot(request, robot_id):
#     error = ""
#     success = ""
#     robot = Robot.objects.get(pk=robot_id)
#     if request.method == "POST":
#         formset = RobotForm(request.POST, request.FILES, instance=robot)
#         if formset.is_valid():
#             formset.save()
#             success = "Robot saved"
#         else:
#             error = "Something wrong"
#     else:
#         formset = RobotForm(instance=robot)
#     return render(request, 'robot_form.html', {
#         'formset': formset,
#         'error': error,
#         'success': success,
#         'robot_id': robot_id
#         })


# @login_required
# def delete_robot(request, robot_id):
#     robot = Robot.objects.get(pk=robot_id)
#     robot.delete()
#     return render_to_response('robot_deleted.html')


# @login_required
# def disable_robot(request, robot_id):
#     #    try:
#     robot = Robot.objects.get(pk=robot_id)
#     if robot.active == True:
#         robot.active = False
#         robot.save()
#         # I close all association with this robot ...
#         slots = Slot.objects.filter(robot=robot_id)
#         for s in slots:
#             assocs = Association.objects.filter(slot=s)
#             for assoc in assocs:
#                 assoc.end_date = datetime.now()
#                 assoc.end_time = datetime.now()
#                 assoc.save()
#     return robot_detail(request, robot_id)


# @login_required
# def enable_robot(request, robot_id):
#     #    try:
#     robot = Robot.objects.get(pk=robot_id)
#     if robot.active == False:
#         robot.active = True
#         robot.save()

#     return robot_detail(request, robot_id)


# @login_required
# def clone_robot(request, robot_id):
#     robot = Robot.objects.get(pk=robot_id)
#     if robot > 0:
#         new_robot = Robot(name=robot.name + "_clone_" + str(robot_id),
#                           date=datetime.now(),
#                           time=datetime.now(),
#                            image=robot.image)
#         new_robot.save()
#         slots = Slot.objects.filter(robot=robot.id)
#         for slot in slots:
#             new_slot = Slot(robot=new_robot, kind=slot.kind, name=slot.name)
#             new_slot.save()
#         return robot_detail(request, new_robot.id)
#     # what is this robot id ?
#     raise Http404


# @login_required
# def new_robot(request):
#     error = ""
#     success = ""
#     if request.method == "POST":
#         formset = RobotForm(request.POST, request.FILES)
#         if formset.is_valid():
#             formset.save()
#             success = "Robot saved"
#         else:
#             error = "Something wrong"
#     else:
#         formset = RobotForm()
#     return render(request, 'robot_form.html', {
#         'formset': formset,
#         'error': error,
#         'success': success
#         })


# @login_required
# def new_event(request, motor_id):
#     error = ""
#     success = ""
#     formset = MotorEventForm(request.POST or None)
#     if formset.is_valid():
#         event = MotorEvent(device=Motor.objects.get(pk=motor_id),
#                             state=formset.cleaned_data['state'],
#                             date=formset.cleaned_data['date'],
#                             time=formset.cleaned_data['time'],
#                             description=formset.cleaned_data['description'])
#         event.save()
#         success = "Slot saved"
#     elif request.method == 'POST':
#         error = "Something went wrong"
#     motor = Motor.objects.get(id=motor_id)
#     return render(request, 'event_form.html', {
#         'formset': formset,
#         'error': error,
#         'success': success,
#         'motor': motor,
#         'last_event': motor.last_event(),
#         })


# @login_required
# def type(request):
#     all_type = MotorType.objects.all()
#     return render_to_response('types.html', {'all_type': all_type})


# @login_required
# def new_type(request):
#     error = ""
#     success = ""
#     formset = MotorTypeForm(request.POST or None)
#     if formset.is_valid():
#         motor_type = MotorType(
#                 name=formset.cleaned_data['name'],
#                 price=formset.cleaned_data['price'],
#                 )
#         motor_type.save()
#         success = "Motor type saved"
#         all_type = MotorType.objects.all()
#         return render_to_response('types.html', {
#             'success': success,
#             'all_type': all_type,
#             })
#         # TODO use proper redirection (26/10/2012)
#     else:
#         error = "Check the form..."
#     return render(request, 'type.html', {
#         'error': error,
#         'formset': formset,
#         })


# @login_required
# def new_slot(request, robot_id):
#     error = ""
#     success = ""
#     try:
#         robot = Robot.objects.get(pk=robot_id)
#         slot = Slot(robot=robot)
#         form = SlotForm(request.POST or None, instance=slot)
#         if form.is_valid():
#             form.save()
#             success = "Item saved"
#         elif request.POST:
#             error = "Something went wrong"
#         return render(request, 'slot_form.html', {
#             'form': form,
#             'error': error,
#             'success': success,
#             'robot': robot,
#             })
#     except Robot.DoesNotExist:
#         raise Http404


# @login_required
# def new_slot_from_device(request, robot_id):
#     try:
#         robot = Robot.objects.get(pk=robot_id)
#         form = ChoseDeviceForm(request.POST or None)
#         if form.is_valid():
#             device = form.cleaned_data['device']
#             new_slot = Slot(robot=robot,
#                             kind=device.kind,
#                             name=str(device.kind))
#             new_slot.save()
#             new_assoc = Association(device=device, slot=new_slot)
#             new_assoc.save()
#         return HttpResponseRedirect("/robot/%d/" % robot.id)
#     except Robot.DoesNotExist:
#         raise Http404


# @login_required
# def edit_slot(request, slot_id):
#     error = ""
#     success = ""
#     slot = Slot.objects.get(pk=slot_id)
#     if request.method == "POST":
#         form = SlotForm(request.POST, request.FILES, instance=slot)
#         if form.is_valid():
#             form.save()
#             success = "Slot saved"
#         else:
#             error = "Something wrong"
#     else:
#         form = SlotForm(instance=slot)
#     return render(request, 'slot_form.html', {
#         'form': form,
#         'error': error,
#         'success': success,
#         'robot': slot.robot,
#         'slot_id': slot_id
#         })


# @login_required
# def remove_slot(request, slot_id):
#     error = ""
#     success = ""
#     slot = Slot.objects.get(pk=slot_id)
#     robot_id = slot.robot.id
#     return render(request, 'slot_delete.html', {
#         'slot': slot,
#         'error': error,
#         'success': success,
#         'robot_id': robot_id,
#         'slot_id': slot_id
#         })


# @login_required

# def help(request):
#     return render(request, 'help.html')
