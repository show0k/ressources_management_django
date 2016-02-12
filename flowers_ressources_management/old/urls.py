from django.conf.urls.defaults import patterns

urlpatterns = patterns('robot.views',
    (r'^$', 'index'),
    (r'^logout/$', 'logout_mm'),

    (r'^robot/(?P<robot_id>\d+)/$', 'robot_detail'),
    (r'^robot/(?P<robot_id>\d+)/slot/$', 'new_slot'),
    (r'^robot/(?P<robot_id>\d+)/additem/$', 'new_slot_from_device'),
    (r'^robot/(?P<robot_id>\d+)/edit/$', 'edit_robot'),
    (r'^robot/(?P<robot_id>\d+)/clone/$', 'clone_robot'),
    (r'^robot/(?P<robot_id>\d+)/disable/$', 'disable_robot'),
    (r'^robot/(?P<robot_id>\d+)/enable/$', 'enable_robot'),
    (r'^robot/(?P<robot_id>\d+)/delete/$', 'delete_robot'),
    (r'^robot/$', 'new_robot'),
    (r'^robots/$', 'robots'),

    (r'^type/$', 'type'),
    (r'^type/new/$', 'new_type'),

    (r'^init$', 'init'),

    (r'^help/$', 'help'),

    (r'^slot/(?P<slot_id>\d+)/$', 'slot'),
    (r'^slot/(?P<slot_id>\d+)/edit/$', 'edit_slot'),
    (r'^slot/(?P<slot_id>\d+)/remove/$', 'remove_slot'),
    (r'^slot/(?P<slot_id>\d+)/removed/$', 'removed_slot'),

    (r'^motor/$', 'new_motor'),
    (r'^motor/(?P<motor_id>\d+)/$', 'motor'),
    (r'^motor/(?P<motor_id>\d+)/edit/$', 'edit_motor'),
    (r'^motors/$', 'motors'),

    (r'^search/$', 'search'),

    (r'^association/$', 'new_association'),
    (r'^association/slot/(?P<slot_id>\d+)/$', 'new_association'),
    (r'^association/slot/(?P<slot_id>\d+)/new_motor/$', 'new_association_new_motor'),

    (r'^event/(?P<motor_id>\d+)/$', 'new_event'),
)
