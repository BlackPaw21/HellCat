@echo off
REM → Change to the script’s folder so Hashcat finds its OpenCL/ folder
cd /d "%~dp0"

REM → Inform the user we’re about to install/check dependencies
echo Checking for dependencies....

REM → Suppress Python deprecation warnings globally
set PYTHONWARNINGS=ignore

REM → Upgrade pip quietly and disable its self‑check
python -W ignore -m pip install --upgrade pip -q --disable-pip-version-check --no-python-version-warning

REM → Install colorama quietly, suppressing deprecation text
python -W ignore -m pip install colorama -q --no-python-version-warning

REM → Clear the screen before starting the main launcher
cls

REM → Launch the Hellcat Python frontend
python main.py %*

REM → Pause so you can read any messages
pause
@echo off
REM → Change to the script’s folder so Hashcat finds its OpenCL/ folder
cd /d "%~dp0"

REM → Inform the user we’re about to install/check dependencies
echo Checking for dependencies....

REM → Suppress Python deprecation warnings globally
set PYTHONWARNINGS=ignore

REM → Upgrade pip quietly and disable its self‑check
python -W ignore -m pip install --upgrade pip -q --disable-pip-version-check --no-python-version-warning

REM → Install colorama quietly, suppressing deprecation text
python -W ignore -m pip install colorama -q --no-python-version-warning

REM → Clear the screen before starting the main launcher
cls

REM → Launch the Hellcat Python frontend
python main.py %*

REM → Pause so you can read any messages
pause
