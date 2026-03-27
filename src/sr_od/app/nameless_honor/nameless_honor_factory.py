"""无名勋礼应用工厂"""

from typing import TYPE_CHECKING

from one_dragon.base.operation.application.application_factory import ApplicationFactory
from one_dragon.base.operation.application_run_record import AppRunRecord
from sr_od.app.nameless_honor import nameless_honor_const

if TYPE_CHECKING:
    from one_dragon.base.operation.one_dragon_context import OneDragonContext


class NamelessHonorFactory(ApplicationFactory):

    def __init__(self, ctx: 'OneDragonContext'):
        self.ctx = ctx
        super().__init__(
            app_id=nameless_honor_const.APP_ID,
            app_name=nameless_honor_const.APP_NAME,
            default_group=nameless_honor_const.DEFAULT_GROUP,
            need_notify=nameless_honor_const.NEED_NOTIFY,
        )

    def create_application(self, instance_idx: int, group_id: str):
        from sr_od.app.nameless_honor.nameless_honor_app import NamelessHonorApp
        return NamelessHonorApp(self.ctx)

    def create_run_record(self, instance_idx: int) -> AppRunRecord:
        from sr_od.app.nameless_honor.nameless_honor_run_record import NamelessHonorRunRecord
        from sr_od.context.sr_context import SrContext
        ctx: SrContext = self.ctx
        return NamelessHonorRunRecord(
            instance_idx,
            ctx.game_account_config.game_refresh_hour_offset
        )
