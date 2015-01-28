u"""
Here we define the settings for the detection
"""
from __future__ import unicode_literals

DETECTION_PAIRS = {
    "male": {
        "pir": 7,
        "light": 17,
        "free_time": 5,  # time in seconds after which we deem the room freed
    }
}
