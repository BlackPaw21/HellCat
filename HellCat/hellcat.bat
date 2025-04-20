@echo off
REM → Switch to the batch file’s own folder, so Hashcat finds OpenCL/
cd /d "%~dp0"

REM → Make sure pip is up to date (optional)
python -m pip install --upgrade pip

REM → Automatically install colorama (idempotent)
python -m pip install colorama

REM → Launch Hellcat (passes along any CLI args)
python main.py %*

REM → Keep the window open so you can read output
pause
