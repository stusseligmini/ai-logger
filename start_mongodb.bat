@echo off
echo ========================================
echo    MongoDB Startup Helper
echo ========================================
echo.

echo Attempting to start MongoDB service...
net start MongoDB 2>nul
if %errorlevel% equ 0 (
    echo MongoDB service started successfully!
    echo MongoDB is now running on port 27017
    pause
    exit /b 0
) else (
    echo MongoDB service could not be started automatically.
    echo.
    echo This could mean:
    echo 1. MongoDB is not installed
    echo 2. MongoDB service is not configured
    echo 3. You need administrator privileges
    echo.
    echo Please try one of the following:
    echo.
    echo Option 1 - Install MongoDB:
    echo 1. Download from: https://www.mongodb.com/try/download/community
    echo 2. Install with default settings
    echo 3. Run this script again
    echo.
    echo Option 2 - Start MongoDB manually:
    echo 1. Open Command Prompt as Administrator
    echo 2. Run: net start MongoDB
    echo.
    echo Option 3 - Start MongoDB daemon directly:
    echo 1. Navigate to MongoDB bin directory
    echo 2. Run: mongod
    echo.
    pause
    exit /b 1
) 