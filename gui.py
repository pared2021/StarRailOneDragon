import sys
import os

# 将 src/ 目录加入 Python 路径，使 from one_dragon、from sr_od 等导入生效
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

import runpy
runpy.run_path(os.path.join(os.path.dirname(__file__), 'src', 'sr_od', 'gui', 'sr_full_app.py'), run_name='__main__')
