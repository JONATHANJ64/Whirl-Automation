from stations.base import BaseStation
from utils.common import get_config
from utils.logger import logger


FEEDERS = ['upper_housing', 'crank_arm', 'rotor']


class Station2(BaseStation):

    def __init__(self, app):
        super().__init__(app, conf=get_config()['station2'], feeders=FEEDERS, name="Station2", p_index=4,
                         prefetch_parts=['upper_housing'])

    def get_ready_feeder(self):
        for name, ff in self.feeders.items():
            if not self._finished_feeders.get(name) and ff.is_finished():
                if name != 'upper_housing' and not self._finished_feeders.get('upper_housing'):
                    logger.warning(f"{self.name}: FlexFeeder({name}) is ready, but Upper Housing is not yet finished!")
                    continue
                return name
