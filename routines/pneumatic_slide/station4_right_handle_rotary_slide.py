from routines.pneumatic_slide.base import PneumaticSlideBase


class Station4RightHandleRotarySlide(PneumaticSlideBase):
    """
    Slide Controller to open/close the right handle rotary
    """

    def __init__(self, root, action='open', check_current=False, check_target=False, timeout=3):
        super().__init__(
            root=root,
            wago=root.wago,
            name="Station4 Right Handle Rotary Slide",
            conf=root.conf,
            cur_sensor=f'right_handle_rotator_slide_{"closed" if action == "open" else "open"}',
            target_sensor=f'right_handle_rotator_slide_{"open" if action == "open" else "closed"}',
            output_name='right_handle_rotator_slide_close',
            timeout=timeout,
            action=action,
            check_current=check_current,
            check_target=check_target
        )
