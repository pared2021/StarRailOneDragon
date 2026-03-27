from typing import Optional

from PySide6.QtWidgets import QWidget
from qfluentwidgets import FluentIcon

from one_dragon.base.operation.application_base import Application
from one_dragon_qt.view.app_run_interface import AppRunInterface
from one_dragon_qt.widgets.column import Column
from sr_od.app.sr_application import SrApplication
from sr_od.app.quest.quest_app import QuestApp
from sr_od.context.sr_context import SrContext


class QuestRunInterface(AppRunInterface):

    def __init__(self,
                 ctx: SrContext,
                 parent=None):
        self.ctx: SrContext = ctx
        self.app: Optional[SrApplication] = None

        AppRunInterface.__init__(
            self,
            ctx=ctx,
            app_id='quest',
            object_name='sr_quest_run_interface',
            nav_text_cn='运行',
            parent=parent,
        )

    def get_widget_at_top(self) -> QWidget:
        content = Column()
        return content

    def get_app(self) -> Application:
        return QuestApp(self.ctx)
