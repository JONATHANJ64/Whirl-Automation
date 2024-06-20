from routines.pneumatic_slide.base import PneumaticSlideBase


class Station4RightHandleFixturePickSlide(PneumaticSlideBase):
    """
    Slide Controller to orient pick or place of the right handle rotary
    """

    def __init__(self, root, action='pick', check_current=False, check_target=False, timeout=3):
        super().__init__(
            root=root,
            wago=root.wago,
            name="Station4 Right Handle Rotary Slide",
            conf=root.conf,
            cur_sensor=f'right_handle_rotator_{"place" if action == "pick" else "pick"}',
            target_sensor=f'right_handle_rotator_{"pick" if action == "pick" else "place"}',
            output_name='right_handle_rotator_pick_orient',
            timeout=timeout,
            action=action,
            check_current=check_current,
            check_target=check_target
        )
