"""委托应用工厂"""

from typing import TYPE_CHECKING

from one_dragon.base.operation.application.application_factory import ApplicationFactory
from one_dragon.base.operation.application_run_record import AppRunRecord
from sr_od.app.assignments import assignments_const

if TYPE_CHECKING:
    from one_dragon.base.operation.one_dragon_context import OneDragonContext


class AssignmentsFactory(ApplicationFactory):

    def __init__(self, ctx: 'OneDragonContext'):
        self.ctx = ctx
        super().__init__(
            app_id=assignments_const.APP_ID,
            app_name=assignments_const.APP_NAME,
            default_group=assignments_const.DEFAULT_GROUP,
            need_notify=assignments_const.NEED_NOTIFY,
        )

    def create_application(self, instance_idx: int, group_id: str):
        from sr_od.app.assignments.assignments_app import AssignmentsApp
        return AssignmentsApp(self.ctx)

    def create_run_record(self, instance_idx: int) -> AppRunRecord:
        from sr_od.app.assignments.assignments_run_record import AssignmentsRunRecord
        from sr_od.context.sr_context import SrContext
        ctx: SrContext = self.ctx
        return AssignmentsRunRecord(
            instance_idx,
            ctx.game_account_config.game_refresh_hour_offset
        )
