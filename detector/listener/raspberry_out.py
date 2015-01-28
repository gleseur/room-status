from __future__ import unicode_literals
import signals


def setup_action(sender):
    print "Setup done"

def motion_action(sender):
    print "Motion detected"

def idle_action(sender):
    print "Back to idle state"

signals.setup.connect(setup_action)
signals.motion.connect(motion_action)
signals.idle.connect(idle_action)
