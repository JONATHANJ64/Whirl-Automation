from routines.pneumatic_slide.base import PneumaticSlideBase


class Station3PartFlipNestSlide(PneumaticSlideBase):
    """
    Slide Controller to open/close the part flip nest gripper
    """

    def __init__(self, root, action='open', check_current=False, check_target=False, timeout=3):
        super().__init__(
            root=root,
            wago=root.wago,
            name="Station3 Part Flip Nest Slide",
            conf=root.conf,
            cur_sensor=f'part_flip_{"closed" if action == "open" else "open"}',
            target_sensor=f'part_flip_{"open" if action == "open" else "closed"}',
            output_name='flip_nest_gripper_open',
            timeout=timeout,
            action=action,
            check_current=check_current,
            check_target=check_target
        )
