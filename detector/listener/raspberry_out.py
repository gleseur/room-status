from __future__ import unicode_literals
import signals


def setup_action():
    print "Setup done"

def motion_action():
    print "Motion detected"

def idle_action():
    print "Back to idle state"

signals.setup.connect(setup_action)
signals.motion.connect(motion_action)
signals.idle.connect(idle_action)
