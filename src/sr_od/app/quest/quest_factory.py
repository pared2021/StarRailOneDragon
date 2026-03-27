"""任务应用工厂"""

from typing import TYPE_CHECKING

from one_dragon.base.operation.application.application_factory import ApplicationFactory
from one_dragon.base.operation.application_run_record import AppRunRecord
from sr_od.app.quest import quest_const

if TYPE_CHECKING:
    from one_dragon.base.operation.one_dragon_context import OneDragonContext


class QuestFactory(ApplicationFactory):

    def __init__(self, ctx: 'OneDragonContext'):
        self.ctx = ctx
        super().__init__(
            app_id=quest_const.APP_ID,
            app_name=quest_const.APP_NAME,
            default_group=quest_const.DEFAULT_GROUP,
            need_notify=quest_const.NEED_NOTIFY,
        )

    def create_application(self, instance_idx: int, group_id: str):
        from sr_od.app.quest.quest_app import QuestApp
        return QuestApp(self.ctx)

    def create_run_record(self, instance_idx: int) -> AppRunRecord:
        from sr_od.app.quest.quest_run_record import QuestRunRecord
        from sr_od.context.sr_context import SrContext
        ctx: SrContext = self.ctx
        return QuestRunRecord(
            instance_idx,
            ctx.game_account_config.game_refresh_hour_offset
        )
