from typing import Optional

from one_dragon.base.config.notify_config import NotifyConfig as BaseNotifyConfig


# SR 应用的 app_id -> 中文名映射
SR_APP_MAP = {
    'assignments': '委托',
    'echo_of_war': '历战余响',
    'trailblaze_power': '开拓力',
    'world_patrol': '锄大地',
    'sim_universe': '模拟宇宙',
    'relic_salvage': '遗器分解',
    'email': '邮件',
    'buy_xianzhou_parcel': '仙舟过期邮包',
    'trick_snack': '奇巧零食',
    'memory_crystal_shard': '记忆残晶',
    'support_character': '支援角色奖励',
    'daily_training': '每日实训',
    'nameless_honor': '无名勋礼',
}


class NotifyConfig(BaseNotifyConfig):
    """SR 专用通知配置，继承框架层 NotifyConfig"""

    def __init__(self, instance_idx: Optional[int] = None):
        super().__init__(instance_idx=instance_idx, app_map=SR_APP_MAP)
