import time
from typing import Optional

from one_dragon.base.operation.application_run_record import AppRunRecord
from sr_od.app.trailblaze_power.trailblaze_power_config import TrailblazePowerConfig


class TrailblazePowerRunRecord(AppRunRecord):

    def __init__(self, tp_config: TrailblazePowerConfig,
                 instance_idx: Optional[int] = None, game_refresh_hour_offset: int = 0):
        self.tp_config: TrailblazePowerConfig = tp_config
        AppRunRecord.__init__(self, 'trailblaze_power', instance_idx=instance_idx,
                              game_refresh_hour_offset=game_refresh_hour_offset)

    def check_and_update_status(self):
        # 隔天刷新：正常重置，允许当天重新执行
        if self._should_reset_by_dt():
            self.reset_record()
            return

        # loop=False 且所有计划已完成：标记为成功，一条龙调度时会跳过该任务
        if not self.tp_config.loop:
            all_done = len(self.tp_config.plan_list) > 0 and all(
                item.run_times >= item.plan_times for item in self.tp_config.plan_list
            )
            if all_done:
                self.update_status(AppRunRecord.STATUS_SUCCESS, only_status=True)
