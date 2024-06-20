from routines.pneumatic_slide.base import PneumaticSlideBase


class Station5BoxClamp(PneumaticSlideBase):
    """
    Box Clamp slider in the boxing platform
    """

    def __init__(self, root, action='engage', check_current=False, check_target=False, timeout=3):
        super().__init__(
            root=root,
            wago=root.wago,
            name="Station5 Box Clamp",
            conf=root.conf,
            cur_sensor='box_clamp_retracted' if action == "engage" else "box_clamp_engaged",
            target_sensor="box_clamp_engaged" if action == 'engage' else 'box_clamp_retracted',
            output_name='box_clamp_engage',
            timeout=timeout,
            action=action,
            check_current=check_current,
            check_target=check_target
        )
