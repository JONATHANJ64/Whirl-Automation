from routines.pneumatic_slide.base import PneumaticSlideBase


class Station5RotaryFixture(PneumaticSlideBase):
    """
    Slide Controller rotate the final product fixture
    """

    def __init__(self, root, action='home', check_current=False, check_target=False, timeout=3):
        super().__init__(
            root=root,
            wago=root.wago,
            name="Station5 Rotary Fixture Slide",
            conf=root.conf,
            cur_sensor=f'whirl_rotator_{"ccw" if action == "home" else "cw"}',
            target_sensor=f'whirl_rotator_{"cw" if action == "home" else "ccw"}',
            output_name='whirl_rotator',
            timeout=timeout,
            action=action,
            check_current=check_current,
            check_target=check_target
        )
