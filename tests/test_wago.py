import argparse
import os
import sys

_cur_dir = os.path.dirname(os.path.realpath(__file__))
_par_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.pardir)
if _par_dir not in sys.path:
    sys.path.append(_par_dir)

from utils.logger import logger
from utils.wago import WagoController


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='WAGO testing script')
    parser.add_argument('-a', '--address', help='Host of WAGO module. Use IP address', required=True)
    parser.add_argument('-c', '--channel', help='Target channel to turn on & off(starts from 0)',
                        required=True, type=int)
    parser.add_argument('-v', '--value', help='Value, should be ON/OFF', required=True)
    args = parser.parse_args()

    wago = WagoController(host=args.address)

    logger.debug(f"Trying to connect {args.address}")
    if wago.connect():
        r = wago.write_coil(address=args.channel, value=1 if str(args.value).lower() in {'on', 'true', '1'} else 0)
        logger.info(f"Result: {r}")
    else:
        sys.exit(-1)
