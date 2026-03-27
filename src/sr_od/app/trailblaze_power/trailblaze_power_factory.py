"""开拓力应用工厂"""

from typing import TYPE_CHECKING

from one_dragon.base.operation.application.application_factory import ApplicationFactory
from one_dragon.base.operation.application_run_record import AppRunRecord
from sr_od.app.trailblaze_power import trailblaze_power_const

if TYPE_CHECKING:
    from one_dragon.base.operation.one_dragon_context import OneDragonContext


class TrailblazePowerFactory(ApplicationFactory):

    def __init__(self, ctx: 'OneDragonContext'):
        self.ctx = ctx
        super().__init__(
            app_id=trailblaze_power_const.APP_ID,
            app_name=trailblaze_power_const.APP_NAME,
            default_group=trailblaze_power_const.DEFAULT_GROUP,
            need_notify=trailblaze_power_const.NEED_NOTIFY,
        )

    def create_application(self, instance_idx: int, group_id: str):
        from sr_od.app.trailblaze_power.trailblaze_power_app import TrailblazePowerApp
        return TrailblazePowerApp(self.ctx)

    def create_run_record(self, instance_idx: int) -> AppRunRecord:
        from sr_od.app.trailblaze_power.trailblaze_power_run_record import TrailblazePowerRunRecord
        from sr_od.context.sr_context import SrContext
        ctx: SrContext = self.ctx
        return TrailblazePowerRunRecord(
            ctx.power_config,
            instance_idx,
            ctx.game_account_config.game_refresh_hour_offset
        )
