from PySide6.QtWidgets import QWidget
from numpy.core.defchararray import title
from qfluentwidgets import FluentIcon, SettingCardGroup

from one_dragon.base.config.config_item import ConfigItem
from one_dragon.base.operation.one_dragon_context import ContextInstanceEventEnum
from one_dragon_qt.widgets.column import Column
from one_dragon_qt.widgets.vertical_scroll_interface import VerticalScrollInterface
from one_dragon_qt.widgets.setting_card.combo_box_setting_card import ComboBoxSettingCard
from one_dragon_qt.widgets.setting_card.text_setting_card import TextSettingCard
from one_dragon_qt.view.context_event_signal import ContextEventSignal
from sr_od.app.sim_uni.sim_uni_const import SimUniWorldEnum
from sr_od.context.sr_context import SrContext


class SimUniSettingInterface(VerticalScrollInterface):


    def __init__(self, ctx: SrContext, parent=None):
        self.ctx: SrContext = ctx
        self._context_event_signal = ContextEventSignal()

        VerticalScrollInterface.__init__(
            self,
            object_name='sr_sim_uni_setting_interface',
            content_widget=None, parent=parent,
            nav_text_cn='每周配置'
        )

    def get_content_widget(self) -> QWidget:
        content_widget = Column()

        self.weekly_sim_uni_num_opt = ComboBoxSettingCard(icon=FluentIcon.GAME, title='模拟宇宙')
        content_widget.add_widget(self.weekly_sim_uni_num_opt)

        self.weekly_sim_uni_diff_opt = ComboBoxSettingCard(icon=FluentIcon.GAME, title='难度')
        content_widget.add_widget(self.weekly_sim_uni_diff_opt)

        self.weekly_plan_times_opt = TextSettingCard(icon=FluentIcon.CALENDAR, title='每周精英次数')
        content_widget.add_widget(self.weekly_plan_times_opt)

        self.daily_plan_times_opt = TextSettingCard(icon=FluentIcon.CALENDAR, title='每日精英次数')
        content_widget.add_widget(self.daily_plan_times_opt)

        challenge_group = SettingCardGroup(title='挑战配置')
        content_widget.add_widget(challenge_group)

        self.challenge_opt_list = {}

        for i in SimUniWorldEnum:
            if i.name in ['WORLD_00', 'WORLD_01', 'WORLD_02']:
                continue

            challenge_opt = ComboBoxSettingCard(icon=FluentIcon.GAME, title=i.value.name)
            challenge_group.addSettingCard(challenge_opt)

            self.challenge_opt_list[i.value.idx] = challenge_opt

        content_widget.add_stretch(1)
        return content_widget

    def on_interface_shown(self) -> None:
        VerticalScrollInterface.on_interface_shown(self)

        self.ctx.listen_event(ContextInstanceEventEnum.context_init_done.value, self._on_context_init_done)
        self._context_event_signal.instance_changed.connect(self._reload_data)

        if not self.ctx.ready_for_application:
            return

        self._reload_data()

    def on_interface_hidden(self) -> None:
        VerticalScrollInterface.on_interface_hidden(self)
        self.ctx.unlisten_all_event(self)
        try:
            self._context_event_signal.instance_changed.disconnect(self._reload_data)
        except RuntimeError:
            pass

    def _on_context_init_done(self, event) -> None:
        """上下文初始化完成，通过 signal 通知 UI 线程重新加载数据"""
        self._context_event_signal.instance_changed.emit()

    def _reload_data(self) -> None:
        """加载数据到界面"""
        sim_uni_num_opts = [
            ConfigItem(label=i.value.name, value=i.name)
            for i in SimUniWorldEnum
            if i.name not in ['WORLD_00', 'WORLD_01', 'WORLD_02']
        ]
        self.weekly_sim_uni_num_opt.set_options_by_list(sim_uni_num_opts)
        self.weekly_sim_uni_num_opt.init_with_adapter(self.ctx.sim_uni_config.weekly_uni_num_adapter)

        diff_opts = [ConfigItem(label='默认难度', value=0)]
        for i in SimUniWorldEnum:
            if i.name == self.ctx.sim_uni_config.weekly_uni_num:
                for j in range(1, i.value.max_diff + 1):
                    diff_opts.append(ConfigItem(label=str(j), value=j))
        self.weekly_sim_uni_diff_opt.set_options_by_list(diff_opts)
        self.weekly_sim_uni_diff_opt.init_with_adapter(self.ctx.sim_uni_config.weekly_uni_diff_adapter)

        self.weekly_plan_times_opt.init_with_adapter(self.ctx.sim_uni_config.elite_weekly_times_adapter)
        self.daily_plan_times_opt.init_with_adapter(self.ctx.sim_uni_config.elite_daily_times_adapter)

        for idx, opt in self.challenge_opt_list.items():
            opt.set_options_by_list([
                ConfigItem(label=i.name, value='%02d' % i.idx)
                for i in self.ctx.sim_uni_challenge_config_data.load_all_challenge_config()
            ])

            opt.init_with_adapter(self.ctx.sim_uni_config.get_challenge_config_adapter(idx))