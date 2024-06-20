from routines.pneumatic_slide.base import PneumaticSlideBase


class PalletHandlerLiftAndLocateSlide(PneumaticSlideBase):
    """
    Slide Controller to activate/deactivate Lift & Locate cylinder
    """

    def __init__(self, pallet, action='up', check_current=True, check_target=True, timeout=3):
        station = pallet.root
        super().__init__(
            root=station,
            wago=station.wago,
            name=f"Lift & Locate {pallet.index}",
            conf=station.conf,
            cur_sensor=f'lift_locate_{"retracted" if action == "up" else "extended"}_{pallet.index}',
            target_sensor=f'lift_locate_{"extended" if action == "up" else "retracted"}_{pallet.index}',
            output_name=f'lift_locate_up_{pallet.index}',
            timeout=timeout,
            action=action,
            check_current=check_current,
            check_target=check_target
        )
