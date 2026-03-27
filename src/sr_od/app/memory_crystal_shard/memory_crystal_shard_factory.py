"""记忆水晶碎片应用工厂"""

from typing import TYPE_CHECKING

from one_dragon.base.operation.application.application_factory import ApplicationFactory
from one_dragon.base.operation.application_run_record import AppRunRecord
from sr_od.app.memory_crystal_shard import memory_crystal_shard_const

if TYPE_CHECKING:
    from one_dragon.base.operation.one_dragon_context import OneDragonContext


class MemoryCrystalShardFactory(ApplicationFactory):

    def __init__(self, ctx: 'OneDragonContext'):
        self.ctx = ctx
        super().__init__(
            app_id=memory_crystal_shard_const.APP_ID,
            app_name=memory_crystal_shard_const.APP_NAME,
            default_group=memory_crystal_shard_const.DEFAULT_GROUP,
            need_notify=memory_crystal_shard_const.NEED_NOTIFY,
        )

    def create_application(self, instance_idx: int, group_id: str):
        from sr_od.app.memory_crystal_shard.memory_crystal_shard_app import MemoryCrystalShardApp
        return MemoryCrystalShardApp(self.ctx)

    def create_run_record(self, instance_idx: int) -> AppRunRecord:
        from sr_od.app.memory_crystal_shard.memory_crystal_shard_run_record import MemoryCrystalShardRunRecord
        from sr_od.context.sr_context import SrContext
        ctx: SrContext = self.ctx
        return MemoryCrystalShardRunRecord(
            instance_idx,
            ctx.game_account_config.game_refresh_hour_offset
        )
