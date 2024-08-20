@echo off

echo Checking for Python3 installation...

rem Check common Python installation directories
if exist "%ProgramFiles%\Python312\python.exe" (
    set PYTHON_PATH=%ProgramFiles%\Python312\python.exe
) else if exist "%LocalAppData%\Programs\Python\Python312\python.exe" (
    set PYTHON_PATH=%LocalAppData%\Programs\Python\Python312\python.exe
) else if exist "%ProgramFiles%\Python310\python.exe" (
    set PYTHON_PATH=%ProgramFiles%\Python310\python.exe
) else if exist "%LocalAppData%\Programs\Python\Python310\python.exe" (
    set PYTHON_PATH=%LocalAppData%\Programs\Python\Python310\python.exe
) else (
    rem Check if Python is in the PATH environment variable
    where python >nul 2>&1
    if %errorlevel% == 0 (
        for /f "tokens=*" %%i in ('where python') do (
            set PYTHON_PATH=%%i
            goto :found_python
        )
    )
)

:found_python
if defined PYTHON_PATH (
    echo Python3 already installed at %PYTHON_PATH%. Skipping installation.
) else (
    echo Installing Python3...
    curl https://www.python.org/ftp/python/3.12.5/python-3.12.5-amd64.exe -o python-3.12.5-amd64.exe
    start python-3.12.5-amd64.exe /quiet InstallAllUsers=1 PrependPath=1
    timeout /t 10
    rem Verify installation
    where python >nul 2>&1
    if %errorlevel% == 0 (
        for /f "tokens=*" %%i in ('where python') do (
            set PYTHON_PATH=%%i
            echo Python3 installed at %PYTHON_PATH%.
        )
    ) else (
        echo Python3 installation failed. Please install manually.
        pause
        exit /b 1
    )
)

timeout /t 7

echo Updating Pip
python -m pip install --upgrade pip

echo Installing libraries...
pip install pyautogui
pip install pillow
pip install pynput
pip install numpy
pip install opencv-python

echo Installation complete!
pause
