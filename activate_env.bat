REM filepath: /E:/ai.projects/paper-cast/activate_env.bat
@echo off
setlocal enabledelayedexpansion

REM Check for Python in common paths
set "PATHS_TO_CHECK=C:\Python39;C:\Python38;%LOCALAPPDATA%\Programs\Python\Python39;%LOCALAPPDATA%\Programs\Python\Python38;%PROGRAMFILES%\Python39;%PROGRAMFILES%\Python38;%PROGRAMFILES(X86)%\Python39;%PROGRAMFILES(X86)%\Python38"

for %%p in ("%PATHS_TO_CHECK:;=";"%") do (
    if exist "%%~p\python.exe" (
        set "PYTHON_PATH=%%~p\python.exe"
        goto :found_python
    )
)

REM If not found in common paths, try PATH
where python >nul 2>&1
if %errorlevel% equ 0 (
    for /f "tokens=*" %%i in ('where python') do (
        set "PYTHON_PATH=%%i"
        goto :found_python
    )
)

:python_not_found
echo Python not found in common locations or PATH.
echo Please install Python 3.8 or 3.9 (64-bit) from https://www.python.org/downloads/
echo Make sure to check "Add Python to PATH" during installation.
echo.
echo IMPORTANT: Do NOT install from Microsoft Store!
start https://www.python.org/downloads/
pause
exit /b 1

:found_python
echo Found Python at: "%PYTHON_PATH%"

REM Create virtual environment if it doesn't exist
if not exist "ncmenv\Scripts\activate.bat" (
    echo Creating virtual environment...
    "%PYTHON_PATH%" -m venv "ncmenv"
    if errorlevel 1 (
        echo Failed to create virtual environment
        pause
        exit /b 1
    )
)

REM Activate virtual environment
call "ncmenv\Scripts\activate.bat"
if errorlevel 1 (
    echo Failed to activate virtual environment
    pause
    exit /b 1
)

echo Virtual environment activated successfully.

REM Install dependencies using python -m pip
python -m pip install --no-cache-dir --upgrade pip setuptools wheel
if errorlevel 1 (
    echo Failed to upgrade pip, setuptools, and wheel
    pause
    exit /b 1
)

REM Install all requirements directly
python -m pip install --no-cache-dir -r requirements.txt
if errorlevel 1 (
    echo Failed to install requirements
    pause
    exit /b 1
)

echo All dependencies installed successfully!
endlocal