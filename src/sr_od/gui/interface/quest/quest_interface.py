from qfluentwidgets import FluentIcon

from one_dragon_qt.widgets.pivot_navi_interface import PivotNavigatorInterface
from sr_od.context.sr_context import SrContext
from sr_od.gui.interface.quest.quest_run_interface import QuestRunInterface


class QuestInterface(PivotNavigatorInterface):

    def __init__(self, ctx: SrContext, parent=None):
        self.ctx: SrContext = ctx
        PivotNavigatorInterface.__init__(self, object_name='sr_quest_interface', parent=parent,
                                         nav_text_cn='任务', nav_icon=FluentIcon.FLAG)

    def create_sub_interface(self):
        """
        创建下面的子页面
        :return:
        """
        self.add_sub_interface(QuestRunInterface(ctx=self.ctx))
