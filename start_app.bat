@echo off
echo ========================================
echo    Telegram AI Analyzer Startup
echo ========================================
echo.

REM Check if MongoDB is installed and running
echo Checking MongoDB status...
netstat -an | find "27017" > nul
if %errorlevel% equ 0 (
    echo MongoDB is already running on port 27017
) else (
    echo MongoDB is not running on port 27017
    echo.
    echo Please start MongoDB before running this application.
    echo.
    echo To install MongoDB:
    echo 1. Download MongoDB Community Server from: https://www.mongodb.com/try/download/community
    echo 2. Install it with default settings
    echo 3. Start MongoDB service
    echo.
    echo To start MongoDB service manually:
    echo - Open Command Prompt as Administrator
    echo - Run: net start MongoDB
    echo.
    echo Or start MongoDB manually:
    echo - Navigate to MongoDB bin directory (usually C:\Program Files\MongoDB\Server\6.0\bin)
    echo - Run: mongod
    echo.
    pause
    exit /b 1
)

REM Check if virtual environment exists
if not exist "venv\Scripts\activate.bat" (
    echo Virtual environment not found. Creating one...
    python -m venv venv
    echo Virtual environment created successfully.
)

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat

REM Install/update dependencies
echo Installing dependencies...
pip install -r requirements.txt

REM Start the application
echo.
echo ========================================
echo Starting the application...
echo The application will be available at: http://localhost:8000
echo Press Ctrl+C to stop the application
echo ========================================
echo.

uvicorn main:app --host 0.0.0.0 --port 8000 --reload

REM Keep the window open if there's an error
pause 