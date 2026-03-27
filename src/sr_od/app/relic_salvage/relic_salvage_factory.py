"""遗器分解应用工厂"""

from typing import TYPE_CHECKING

from one_dragon.base.operation.application.application_factory import ApplicationFactory
from one_dragon.base.operation.application_run_record import AppRunRecord
from sr_od.app.relic_salvage import relic_salvage_const

if TYPE_CHECKING:
    from one_dragon.base.operation.one_dragon_context import OneDragonContext


class RelicSalvageFactory(ApplicationFactory):

    def __init__(self, ctx: 'OneDragonContext'):
        self.ctx = ctx
        super().__init__(
            app_id=relic_salvage_const.APP_ID,
            app_name=relic_salvage_const.APP_NAME,
            default_group=relic_salvage_const.DEFAULT_GROUP,
            need_notify=relic_salvage_const.NEED_NOTIFY,
        )

    def create_application(self, instance_idx: int, group_id: str):
        from sr_od.app.relic_salvage.relic_salvage_app import RelicSalvageApp
        return RelicSalvageApp(self.ctx)

    def create_run_record(self, instance_idx: int) -> AppRunRecord:
        from sr_od.app.relic_salvage.relic_salvage_run_record import RelicSalvageRunRecord
        from sr_od.context.sr_context import SrContext
        ctx: SrContext = self.ctx
        return RelicSalvageRunRecord(
            instance_idx,
            ctx.game_account_config.game_refresh_hour_offset
        )
