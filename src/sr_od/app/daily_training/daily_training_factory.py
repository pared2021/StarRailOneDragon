"""每日实训应用工厂"""

from typing import TYPE_CHECKING

from one_dragon.base.operation.application.application_factory import ApplicationFactory
from one_dragon.base.operation.application_run_record import AppRunRecord
from sr_od.app.daily_training import daily_training_const

if TYPE_CHECKING:
    from one_dragon.base.operation.one_dragon_context import OneDragonContext


class DailyTrainingFactory(ApplicationFactory):

    def __init__(self, ctx: 'OneDragonContext'):
        self.ctx = ctx
        super().__init__(
            app_id=daily_training_const.APP_ID,
            app_name=daily_training_const.APP_NAME,
            default_group=daily_training_const.DEFAULT_GROUP,
            need_notify=daily_training_const.NEED_NOTIFY,
        )

    def create_application(self, instance_idx: int, group_id: str):
        from sr_od.app.daily_training.daily_training_app import DailyTrainingApp
        return DailyTrainingApp(self.ctx)

    def create_run_record(self, instance_idx: int) -> AppRunRecord:
        from sr_od.app.daily_training.daily_training_run_record import DailyTrainingRunRecord
        from sr_od.context.sr_context import SrContext
        ctx: SrContext = self.ctx
        return DailyTrainingRunRecord(
            instance_idx,
            ctx.game_account_config.game_refresh_hour_offset
        )
