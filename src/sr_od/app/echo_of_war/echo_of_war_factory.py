"""历战余响应用工厂"""

from typing import TYPE_CHECKING

from one_dragon.base.operation.application.application_factory import ApplicationFactory
from one_dragon.base.operation.application_run_record import AppRunRecord
from sr_od.app.echo_of_war import echo_of_war_const

if TYPE_CHECKING:
    from one_dragon.base.operation.one_dragon_context import OneDragonContext


class EchoOfWarFactory(ApplicationFactory):

    def __init__(self, ctx: 'OneDragonContext'):
        self.ctx = ctx
        super().__init__(
            app_id=echo_of_war_const.APP_ID,
            app_name=echo_of_war_const.APP_NAME,
            default_group=echo_of_war_const.DEFAULT_GROUP,
            need_notify=echo_of_war_const.NEED_NOTIFY,
        )

    def create_application(self, instance_idx: int, group_id: str):
        from sr_od.app.echo_of_war.echo_of_war_app import EchoOfWarApp
        return EchoOfWarApp(self.ctx)

    def create_run_record(self, instance_idx: int) -> AppRunRecord:
        from sr_od.app.echo_of_war.echo_of_war_run_record import EchoOfWarRunRecord
        from sr_od.context.sr_context import SrContext
        ctx: SrContext = self.ctx
        return EchoOfWarRunRecord(
            instance_idx,
            ctx.game_account_config.game_refresh_hour_offset
        )
