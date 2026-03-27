"""Quest 任务功能主应用"""
from typing import List, ClassVar

from one_dragon.base.operation.operation_edge import node_from
from one_dragon.base.operation.operation_node import operation_node
from one_dragon.base.operation.operation_round_result import OperationRoundResult
from one_dragon.utils.i18_utils import gt
from one_dragon.utils.log_utils import log
from sr_od.app.sr_application import SrApplication
from sr_od.context.sr_context import SrContext
from sr_od.operations.back_to_normal_world_plus import BackToNormalWorldPlus


class QuestApp(SrApplication):
    """Quest 任务功能的主应用"""

    STATUS_ALL_FINISHED: ClassVar[str] = '所有任务已完成'

    def __init__(self, ctx: SrContext):
        SrApplication.__init__(self, ctx, 'quest', op_name=gt('任务自动化'),
                               run_record=ctx.quest_record if hasattr(ctx, 'quest_record') else None,
                               need_notify=True)
        self.quest_list: List[str] = []  # 待执行的任务列表
        self.current_idx: int = 0  # 当前执行的任务索引

    @operation_node(name='加载任务', is_start_node=True)
    def load_quest_list(self) -> OperationRoundResult:
        """加载待执行的任务列表"""
        # TODO: 实现任务加载逻辑
        log.info('开始加载任务列表')
        self.quest_list = []  # 空壳，后续实现加载逻辑
        self.current_idx = 0

        if len(self.quest_list) == 0:
            log.info('没有待执行的任务')
            return self.round_success(QuestApp.STATUS_ALL_FINISHED)
        else:
            log.info(f'共加载 {len(self.quest_list)} 个任务')
            return self.round_success()

    @node_from(from_name='加载任务')
    @operation_node(name='进入大世界')
    def back_to_normal_world(self) -> OperationRoundResult:
        """返回大世界，准备执行任务"""
        op = BackToNormalWorldPlus(self.ctx)
        return self.round_by_op_result(op.execute())

    @node_from(from_name='进入大世界')
    @node_from(from_name='执行任务')
    @operation_node(name='执行任务')
    def run_quest(self) -> OperationRoundResult:
        """执行当前任务"""
        if self.current_idx >= len(self.quest_list):
            return self.round_success(QuestApp.STATUS_ALL_FINISHED)

        quest_id = self.quest_list[self.current_idx]
        log.info(f'执行任务 [{self.current_idx + 1}/{len(self.quest_list)}]: {quest_id}')

        # TODO: 实现具体任务执行逻辑
        # 空壳实现：直接标记完成并进入下一个
        self.current_idx += 1
        return self.round_success()

    @node_from(from_name='加载任务', status=STATUS_ALL_FINISHED)
    @node_from(from_name='执行任务', status=STATUS_ALL_FINISHED)
    @operation_node(name='完成')
    def finished(self) -> OperationRoundResult:
        """任务全部完成"""
        log.info('所有任务执行完成')
        return self.round_success()


def __debug():
    ctx = SrContext()
    ctx.init()
    app = QuestApp(ctx)
    app.execute()


if __name__ == '__main__':
    __debug()
