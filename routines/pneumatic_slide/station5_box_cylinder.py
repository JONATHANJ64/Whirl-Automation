from routines.pneumatic_slide.base import PneumaticSlideBase
from utils.logger import logger


class Station5BoxCylinder(PneumaticSlideBase):
    """
    Box Cylinder in the boxing platform
    """

    def __init__(self, root, action='extend', check_current=False, check_target=False, timeout=5):
        super().__init__(
            root=root,
            wago=root.wago,
            name="Station5 Box Cylinder",
            conf=root.conf,
            cur_sensor='box_cylinder_retracted' if action == "extend" else "boxing_sensor_3",
            target_sensor="boxing_sensor_3" if action == 'extend' else 'box_cylinder_retracted',
            output_name='box_cylinder_actuate',
            timeout=timeout,
            action=action,
            check_current=check_current,
            check_target=check_target
        )

    def write_output(self):
        val = self.action == 'extend'
        logger.debug(f"{self.name} : Turning {self.output_name} wago output - '{val}'")
        self.wago.write_output(channel=self.conf['io'][self.output_name], val=val)

    def read_target_sensor(self):
        if self.action == 'extend':
            # When extending the cylinder, we wait for the sensor 3 to be OFF... exceptional case...
            return not self.wago.read_input(self.conf['io']['boxing_sensor_3'])
        else:
            return super().read_target_sensor()
