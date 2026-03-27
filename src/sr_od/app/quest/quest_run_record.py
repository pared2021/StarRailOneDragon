"""Quest 任务功能运行记录类"""
from typing import List, Optional

from one_dragon.base.operation.application_run_record import AppRunRecord


class QuestRunRecord(AppRunRecord):
    """Quest 任务功能的运行记录"""

    def __init__(self, instance_idx: Optional[int] = None, game_refresh_hour_offset: int = 0):
        self.finished_quests: List[str] = []  # 已完成的任务ID列表
        AppRunRecord.__init__(self, 'quest', instance_idx=instance_idx,
                              game_refresh_hour_offset=game_refresh_hour_offset)
        self.finished_quests = self.get('finished_quests', [])

    def reset_record(self):
        """重置记录"""
        AppRunRecord.reset_record(self)
        self.finished_quests = []

        self.update('finished_quests', self.finished_quests, False)
        self.save()

    def add_quest(self, quest_id: str):
        """
        添加已完成的任务
        :param quest_id: 任务ID
        """
        if quest_id not in self.finished_quests:
            self.finished_quests.append(quest_id)

        self.update('run_time', self.app_record_now_time_str(), False)
        self.update('dt', self.dt, False)
        self.update('finished_quests', self.finished_quests, False)
        self.save()
