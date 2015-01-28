from __future__ import unicode_literals
import signals


def setup_action(sender):
    print "Setup done {}".format(sender.name)

def motion_action(sender):
    print "Motion detected {}".format(sender.name)

def idle_action(sender):
    print "Back to idle state {}".format(sender.name)

signals.setup.connect(setup_action)
signals.motion.connect(motion_action)
signals.idle.connect(idle_action)
