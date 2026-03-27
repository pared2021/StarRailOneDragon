"""锄大地应用工厂"""

from typing import TYPE_CHECKING

from one_dragon.base.operation.application.application_factory import ApplicationFactory
from one_dragon.base.operation.application_run_record import AppRunRecord
from sr_od.app.world_patrol import world_patrol_const

if TYPE_CHECKING:
    from one_dragon.base.operation.one_dragon_context import OneDragonContext


class WorldPatrolFactory(ApplicationFactory):

    def __init__(self, ctx: 'OneDragonContext'):
        self.ctx = ctx
        super().__init__(
            app_id=world_patrol_const.APP_ID,
            app_name=world_patrol_const.APP_NAME,
            default_group=world_patrol_const.DEFAULT_GROUP,
            need_notify=world_patrol_const.NEED_NOTIFY,
        )

    def create_application(self, instance_idx: int, group_id: str):
        from sr_od.app.world_patrol.world_patrol_app import WorldPatrolApp
        return WorldPatrolApp(self.ctx)

    def create_run_record(self, instance_idx: int) -> AppRunRecord:
        from sr_od.app.world_patrol.world_patrol_run_record import WorldPatrolRunRecord
        from sr_od.context.sr_context import SrContext
        ctx: SrContext = self.ctx
        return WorldPatrolRunRecord(
            instance_idx,
            ctx.game_account_config.game_refresh_hour_offset
        )
