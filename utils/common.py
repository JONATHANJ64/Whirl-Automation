import http.client
import json
import os
import shutil
import socket
import sys
import threading

_cur_dir = os.path.dirname(os.path.realpath(__file__))
_par_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.pardir)
if _par_dir not in sys.path:
    sys.path.append(_par_dir)

from utils.logger import logger
from settings import CHECK_INTERNET_URL, CONFIG_FILE, PALLET_FILE


def check_internet_connection():
    """
    Check internet connection
        It will be faster to just make a HEAD request so no HTML will be fetched.
        Also I am sure google would like it better this way :)
    """
    conn = http.client.HTTPConnection(CHECK_INTERNET_URL, timeout=5)
    try:
        conn.request("HEAD", "/")
        conn.close()
        return True
    except socket.error:
        conn.close()


def update_dict_recursively(dest, updated):
    """
    Update dictionary recursively.
    :param dest: Destination dict.
    :type dest: dict
    :param updated: Updated dict to be applied.
    :type updated: dict
    :return:
    """
    for k, v in updated.items():
        if isinstance(dest, dict):
            if isinstance(v, dict):
                r = update_dict_recursively(dest.get(k, {}), v)
                dest[k] = r
            else:
                dest[k] = updated[k]
        else:
            dest = {k: updated[k]}
    return dest


lock = threading.Lock()


def update_config_file(data):
    old_data = update_dict_recursively(dest=get_config(), updated=data)
    with lock:
        with open(CONFIG_FILE, 'w') as jp:
            json.dump(old_data, jp, indent=2)


def get_config():
    while True:
        with lock:
            try:
                conf = json.loads(open(CONFIG_FILE).read())
                break
            except Exception as e:
                logger.error(f"Failed to read config file ({e})")
                os.remove(CONFIG_FILE)
                shutil.copy(os.path.join(_cur_dir, 'default_config.json'), CONFIG_FILE)
    return conf


pallet_lock = threading.Lock()


def update_pallet_state(data):
    state = update_dict_recursively(dest=get_pallet_state(), updated=data)
    with pallet_lock:
        with open(PALLET_FILE, 'w') as jp:
            json.dump(state, jp, indent=2)
    return state


def clear_pallet_state():
    with pallet_lock:
        with open(PALLET_FILE, 'w') as jp:
            json.dump({}, jp, indent=2)


def set_pallet_state_exclusive(sn, pallet_state):
    state = get_pallet_state()
    state[sn] = pallet_state
    with pallet_lock:
        with open(PALLET_FILE, 'w') as jp:
            json.dump(state, jp, indent=2)
    return state


def get_pallet_state():
    with pallet_lock:
        try:
            state = json.loads(open(PALLET_FILE).read())
        except Exception as e:
            logger.error(f"Failed to read pallet state - ({e})")
            try:
                os.remove(PALLET_FILE)
            except Exception as e:
                logger.error(f"Failed to delete pallet state file - {e}")
            state = {}
    return state


# =====  Valve related utility functions  =====
def change_bit_of_byte(data, pos, val):
    if val:
        data = data | (1 << pos)
    else:
        data = data & ~(1 << pos)
    return data


def get_valve_bit_value(data: bytearray, pos: int):
    return int(''.join([format(v, '08b') for v in data])[16 - pos])
