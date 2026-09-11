@echo off
cd /d "%~dp0"

if not exist ".venv\Scripts\python.exe" (
    py -m venv .venv
    if errorlevel 1 exit /b 1
)

.venv\Scripts\python.exe Decision_Maker.py
pause
