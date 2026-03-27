"""模拟宇宙应用工厂"""

from typing import TYPE_CHECKING

from one_dragon.base.operation.application.application_factory import ApplicationFactory
from one_dragon.base.operation.application_run_record import AppRunRecord
from sr_od.app.sim_uni import sim_uni_const

if TYPE_CHECKING:
    from one_dragon.base.operation.one_dragon_context import OneDragonContext


class SimUniFactory(ApplicationFactory):

    def __init__(self, ctx: 'OneDragonContext'):
        self.ctx = ctx
        super().__init__(
            app_id=sim_uni_const.APP_ID,
            app_name=sim_uni_const.APP_NAME,
            default_group=sim_uni_const.DEFAULT_GROUP,
            need_notify=sim_uni_const.NEED_NOTIFY,
        )

    def create_application(self, instance_idx: int, group_id: str):
        from sr_od.app.sim_uni.sim_uni_app import SimUniApp
        return SimUniApp(self.ctx)

    def create_run_record(self, instance_idx: int) -> AppRunRecord:
        from sr_od.app.sim_uni.sim_uni_run_record import SimUniRunRecord
        from sr_od.context.sr_context import SrContext
        ctx: SrContext = self.ctx
        return SimUniRunRecord(
            ctx.sim_uni_config,
            instance_idx,
            ctx.game_account_config.game_refresh_hour_offset
        )
