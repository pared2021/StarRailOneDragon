@echo off
chcp 65001 >nul 2>&1

rem 检查是否以管理员权限运行
net session >nul 2>&1
if %errorlevel% neq 0 (
    echo -------------------------------
    echo 尝试获取管理员权限中...
    echo -------------------------------
    timeout /t 2
    PowerShell -Command "Start-Process '%~dpnx0' -Verb RunAs"
    exit /b
)

echo -------------------------------
echo 正在以管理员权限运行...
echo -------------------------------

REM 调用环境配置脚本
call "%~dp0env.bat"
set "PYTHONPATH=%~dp0src"
set "PYTHONUSERBASE=%~dp0.venv"

echo [PASS] PYTHON: %PYTHON%
echo [PASS] PYTHONPATH: %PYTHONPATH%

REM 检查 Python 可执行文件路径
if not exist "%PYTHON%" (
    echo [WARN] 未配置Python.exe，请先运行一键安装
    pause
    exit /b 1
)

echo 启动中...大约需要5+秒
"%PYTHON%" "%~dp0gui.py"

timeout /t 5
exit 0
