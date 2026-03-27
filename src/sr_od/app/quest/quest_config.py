"""Quest 任务功能配置类"""
from typing import Optional

from one_dragon.base.config.yaml_config import YamlConfig
from one_dragon_qt.widgets.setting_card.yaml_config_adapter import YamlConfigAdapter


class QuestConfig(YamlConfig):
    """Quest 任务功能的配置"""

    def __init__(self, instance_idx: Optional[int] = None):
        YamlConfig.__init__(self, 'quest', instance_idx=instance_idx)

    @property
    def team_num(self) -> int:
        """使用的配队号，0表示不切换配队"""
        return self.get('team_num', 0)

    @team_num.setter
    def team_num(self, new_value: int):
        self.update('team_num', new_value)

    @property
    def team_num_adapter(self) -> YamlConfigAdapter:
        return YamlConfigAdapter(self, 'team_num', 0, 'str', 'int')
