import os
import shutil

ROOT_DIR = os.path.expanduser('~/.whirl')

os.makedirs(ROOT_DIR, exist_ok=True)


_cur_dir = os.path.dirname(os.path.realpath(__file__))

CHECK_INTERNET_URL = 'www.google.com'

WAGO_VERBOSE = False

CONFIG_FILE = os.path.join(ROOT_DIR, 'config.json')
if not os.path.exists(CONFIG_FILE):
    print('No JSON Config File Found! Recovering the default one...')
    shutil.copy(os.path.join(_cur_dir, 'default_config.json'), CONFIG_FILE)

PALLET_FILE = os.path.join(ROOT_DIR, 'pallet.json')

CANBUS_BITRATE = 1000000
MOTOR_RETRY_CNT = 5

KMTRONIC_USB_VID = 0x0403
KMTRONIC_USB_PID = 0x6001

R_PART_TO_PICK = "I10"
R_ABORT_SENSOR_CHECK = "I13"
R_CAMERA_NOT_BLOCKED = "I22"
R_MOVING_TO_PARK = "I25"
R_HOPPER_PICKED = 'I43'
R_TASK_COMPLETED = "I50"
R_REQUEST_AIR1_OFF = "I23"
R_REQUEST_AIR1_ON = "I24"
R_ACK_AIR1_OFF = "I26"
R_ACK_AIR1_ON = "I27"
R_DISABLE_COLLISION_DETECTION = "I28"
R_PART_IN_FIXTURE = 'I69'
R_PARK_COMPLETE = "I70"
R_REQUEST_FIXTURE_OPEN = 'I64'
R_REQUEST_FIXTURE_CLOSE = 'I65'
R_REQUEST_FIXTURE_ROTATE_0 = 'I66'
R_REQUEST_FIXTURE_ROTATE_180 = 'I67'
R_UNLOAD_MODE = 'I73'
R_UNLOAD_DIRECTION = 'I59'
R_UNLOAD_PLACE_POINT = 'I75'
R_UNLOAD_FINISHED = 'I41'
R_UNLOAD_PICKED = 'I60'
R_UNLOAD_ROTARY_HOME = 'I61'
R_UNLOAD_ROTARY_180 = 'I62'
R_VACUUM_ACTUATOR = {3: 67, 4: 64}
R_INK_JET_VERTICAL_ADJUST = 'I16'
R_DO_PREFETCH = 'I30'
R_PREFETCH_FINISHED = "I31"
R_WAITING = 'I32'
R_BOXING_MODE = "I30"
R_BOXING_FINISHED = 'I40'
R_BOXING_START_WAIT_SENSOR3 = "I13"
R_BOX_PULLED = "I34"

DEBUG = False

ROBOT_IO_HAND = {
    'in': [None, 48, 10, 48, 13, 48],
    'out': [None, (64, 65), (64, 65), (64, 65), (65, 66), (64, 65)]
}
ROBOT_IO_AGITATOR = {
    'picker': {
        'in': 10,
        'out': (70, 69)
    },
    'placer': {
        'in': 9,
        'out': (68, 67)
    }
}

ROBOT_COMMON_EVENTS = {
    80: "robot {num} hand close sensor was not detected after hand actuation during processing of {part}, "
        "please park robot and then inspect sensor...",
    81: "robot {num} hand open sensor was not detected after hand actuation during processing of {part}, "
        "please park robot and then inspect sensor...",
    82: "robot {num}: unexpected hand sensor state detected after hand actuation during processing of {part}, "
        "was expecting both sensors to be off.  Please park robot and inspect sensors."
}

ROBOT_EXTRA_EVENTS = {
    2: {
        87: "Robot 2 alignment shafts: misalignment sensors triggered during upper housing pick, "
            "please park and inspect robot tooling before continuing.",
    },
    3: {
        89: "Robot 3 Vacuum Sensor:  Sensor did not detect vacuum presence during part pick, "
            "please park robot and adjust sensor if necessary.",
        90: "Robot 3 Vacuum Sensor:  Sensor did not detect vacuum absence during part release, "
            "please park robot and adjust sensor if necessary.",
    },
    4: {
        83: "Robot 4 Agitator Place Arm:  Retract sensor was not detected after actuating arm, "
            "please retract arm manually, park robot and inspect sensor.",
        84: "Robot 4 Agitator Place Arm:  Extend sensor was not detected after actuating arm, "
            "please retract arm manually (if applicable), park robot and inspect sensor.",
        85: "Robot 4 Agitator Pick Arm:  Extend sensor was not detected after actuating arm, "
            "please retract arm manually (if applicable), park robot and inspect sensor.",
        86: "Robot 4 Agitator Pick Arm:  Retract sensor was not detected after actuating arm, "
            "please retract arm manually, park robot and inspect sensor.",
        87: "Robot 4 Handle Press Pins: Sensors were not detected during handle press, "
            "please park and inspect robot tooling before continuing.",
        88: "Robot 4 Hopper Press Pins: Sensors were not detected during hopper installation, "
            "please park and inspect robot tooling before continuing.",
        89: "Robot 4 Vacuum Sensor:  Sensor did not detect vacuum presence during part pick, "
            "please park robot and adjust sensor if necessary.",
        90: "Robot 4 Vacuum Sensor:  Sensor did not detect vacuum absence during part release, "
            "please park robot and adjust sensor if necessary.",
    },
    5: {
        92: "Robot 5 Parking:  Cannot automatically park robot, please park robot with teach pendant, "
            "before resuming.",
    }
}


COGNEX_JOBS = {
    'Whirl - U.S.': 100,
    'Whirl - Canadian': 101,
    'Sta-Green': 102,
    'ACE': 103
}

PRODUCT_BARCODES = {
    'Whirl - U.S.': '0032247710602',
    'Whirl - Canadian': '0032247710060',
    'Sta-Green': '0032247006866',
    'ACE': '0082901382584'
}

try:
    from local_settings import *
except ImportError:
    pass
