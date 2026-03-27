"""购买仙舟包裹应用工厂"""

from typing import TYPE_CHECKING

from one_dragon.base.operation.application.application_factory import ApplicationFactory
from one_dragon.base.operation.application_run_record import AppRunRecord
from sr_od.app.buy_xianzhou_parcel import buy_xianzhou_parcel_const

if TYPE_CHECKING:
    from one_dragon.base.operation.one_dragon_context import OneDragonContext


class BuyXianzhouParcelFactory(ApplicationFactory):

    def __init__(self, ctx: 'OneDragonContext'):
        self.ctx = ctx
        super().__init__(
            app_id=buy_xianzhou_parcel_const.APP_ID,
            app_name=buy_xianzhou_parcel_const.APP_NAME,
            default_group=buy_xianzhou_parcel_const.DEFAULT_GROUP,
            need_notify=buy_xianzhou_parcel_const.NEED_NOTIFY,
        )

    def create_application(self, instance_idx: int, group_id: str):
        from sr_od.app.buy_xianzhou_parcel.buy_xianzhou_parcel_app import BuyXianzhouParcelApp
        return BuyXianzhouParcelApp(self.ctx)

    def create_run_record(self, instance_idx: int) -> AppRunRecord:
        from sr_od.app.buy_xianzhou_parcel.buy_xianzhou_parcel_run_record import BuyXianZhouParcelRunRecord
        from sr_od.context.sr_context import SrContext
        ctx: SrContext = self.ctx
        return BuyXianZhouParcelRunRecord(
            instance_idx,
            ctx.game_account_config.game_refresh_hour_offset
        )
