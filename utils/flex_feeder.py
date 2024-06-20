from json import JSONDecodeError

import requests

from utils.logger import logger


class FlexFeeder:

    def __init__(self, name, host):
        self.host = host
        self.name = name

    def _send_request(self, method='get', url='', json=None):
        full_url = f"http://{self.host}{url}"
        try:
            if method == 'get':
                r = requests.get(url=full_url, timeout=1)
            elif method == 'patch':
                r = requests.patch(url=full_url, json=json, timeout=1)
            elif method == 'post':
                r = requests.post(url=full_url, json=json, timeout=1)
            elif method == 'delete':
                r = requests.delete(url=full_url, timeout=1)
            else:
                logger.error(f"Unknown method - {method}")
                return
            # logger.debug(f"FlexFeeder({self.name}): Sent request({url}), response: ({r.status_code}){r.content}")
            return r
        except Exception as e:
            logger.error(f"Failed to get FlexFeeder response({url}) - {e}")

    def is_alive(self) -> bool:
        r = self._send_request(url='/api/v1/ping')
        return r is not None and r.status_code == 200 and r.content.decode() == 'OK'

    def start_feed(self):
        # Need to resume first cuz sometimes feeders are in paused status...
        self.resume_feed()
        self._send_request(url='/api/v1/feed')

    def reset_feed(self):
        self._send_request(url='/api/v1/reset')

    def lift_slide(self, action='up'):
        self._send_request(url=f'/api/v1/slide/lift?action={action}')

    def set_state(self, state):
        return self._send_request(url=f"/api/v1/state/set?state={state}")

    def action_motor(self, name, action, direction=None):
        payload = {'direction': direction} if action == 'speed' else {}
        return self._send_request(method='post', url=f"/api/v1/motor/manual?motor={name}&action={action}", json=payload)

    def stop_motor(self, name):
        return self._send_request(method='delete', url=f"/api/v1/motor/manual?motor={name}")

    def get_config(self):
        r = self._send_request(url='/api/v1/config')
        if r is not None and r.status_code == 200:
            return r.json()

    def update_config(self, data):
        r = self._send_request(method='patch', url='/api/v1/config', json=data)
        if r is not None and r.status_code == 200:
            return r.content.decode()

    def finish_feed(self):
        self._send_request(url='/api/v1/finish')

    def reject_part(self):
        self._send_request(url='/api/v1/reject')

    def stop_feed(self):
        self._send_request(url='/api/v1/action?val=stop_feed')

    def pause_feed(self):
        self._send_request(url='/api/v1/action?val=pause')

    def resume_feed(self):
        self._send_request(url='/api/v1/action?val=resume')

    def turn_backlight(self, val):
        return self._send_request(url=f'/api/v1/backlight?val={val}')

    def turn_ev0(self, val):
        return self._send_request(url=f'/api/v1/ev0?val={val}')

    def get_current_state(self):
        r = self._send_request(url='/api/v1/current')
        if r is not None and r.status_code == 200:
            return r.json()
        else:
            return {}

    def get_ready_status(self):
        r = self._send_request(url='/api/v1/ready')
        if r is not None and r.status_code == 200:
            try:
                return r.json()
            except JSONDecodeError:
                pass
        return {}
