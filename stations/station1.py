from stations.base import BaseStation
from utils.common import get_config
from utils.logger import logger


FEEDERS = ['cross_gear', 'pinion', 'crank_handle', 'ring_gear']


class Station1(BaseStation):

    def __init__(self, app):
        super().__init__(app, conf=get_config()['station1'], feeders=FEEDERS, name='Station1', p_index=3,
                         prefetch_parts=['cross_gear', 'crank_handle'])

    def get_ready_feeder(self):
        for name, ff in self.feeders.items():
            if not self._finished_feeders.get(name) and ff.is_finished():
                if name in {'pinion', 'ring_gear'} and not self._finished_feeders.get('cross_gear'):
                    logger.warning(f"{self.name}: FlexFeeder({name}) is ready, but Cross Gear is not yet finished!")
                    continue
                return name
