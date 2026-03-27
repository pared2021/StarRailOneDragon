"""邮件应用工厂"""

from typing import TYPE_CHECKING

from one_dragon.base.operation.application.application_factory import ApplicationFactory
from one_dragon.base.operation.application_run_record import AppRunRecord
from sr_od.app.claim_email import email_const

if TYPE_CHECKING:
    from one_dragon.base.operation.one_dragon_context import OneDragonContext


class EmailFactory(ApplicationFactory):

    def __init__(self, ctx: 'OneDragonContext'):
        self.ctx = ctx
        super().__init__(
            app_id=email_const.APP_ID,
            app_name=email_const.APP_NAME,
            default_group=email_const.DEFAULT_GROUP,
            need_notify=email_const.NEED_NOTIFY,
        )

    def create_application(self, instance_idx: int, group_id: str):
        from sr_od.app.claim_email.email_app import EmailApp
        return EmailApp(self.ctx)

    def create_run_record(self, instance_idx: int) -> AppRunRecord:
        from sr_od.app.claim_email.email_run_record import EmailRunRecord
        from sr_od.context.sr_context import SrContext
        ctx: SrContext = self.ctx
        return EmailRunRecord(
            instance_idx,
            ctx.game_account_config.game_refresh_hour_offset
        )
