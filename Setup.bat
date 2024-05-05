@echo off

echo Checking for Python3 installation...

if exist "%ProgramFiles%\Python311\python.exe" (
echo Python3 already installed. Skipping installation.
) else (
echo Installing Python3...
curl https://www.python.org/ftp/python/3.11.0/python-3.11.0-amd64.exe -o python-3.11.0-amd64.exe
start python-3.11.0-amd64.exe /quiet InstallAllUsers=1 PrependPath=1
)

timeout /t 7

echo Updating Pip
python -m pip install --upgrade pip

echo Installing libraries...

echo Installing libraries...

pip install pyautogui
pip install time
pip install pynput
pip install PIL
pip install numpy

echo Installation complete!
pause