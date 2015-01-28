from __future__ import unicode_literals
import signals


def setup_action(sender):
    print "Setup done {}".format(sender.name)

def motion_action(sender):
    print "Motion detected {}".format(sender.name)

def idle_action(sender):
    print "Back to idle state {}".format(sender.name)

def busy_action(sender):
    print "Action detected in the bathroom {}".format(sender.name)

def room_freed_action(sender):
    print "Room {} has been freed. Bye Bye".format(sender.name)


signals.setup.connect(setup_action)
signals.motion.connect(motion_action)
signals.idle.connect(idle_action)
signals.busy.connect(busy_action)
signals.room_freed.connect(room_freed_action)
