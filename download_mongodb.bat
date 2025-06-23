@echo off
echo ========================================
echo    MongoDB Download Helper
echo ========================================
echo.

echo This script will download MongoDB Community Server for Windows
echo.

REM Create downloads directory if it doesn't exist
if not exist "downloads" mkdir downloads

REM Download MongoDB Community Server (latest version)
echo Downloading MongoDB Community Server...
echo This may take a few minutes depending on your internet connection...
echo.

REM Using PowerShell to download the file
powershell -Command "& {Invoke-WebRequest -Uri 'https://fastdl.mongodb.org/windows/mongodb-windows-x86_64-6.0.14-signed.msi' -OutFile 'downloads\mongodb-installer.msi'}"

if %errorlevel% equ 0 (
    echo.
    echo ========================================
    echo Download completed successfully!
    echo ========================================
    echo.
    echo MongoDB installer is saved as: downloads\mongodb-installer.msi
    echo.
    echo To install MongoDB:
    echo 1. Navigate to the downloads folder
    echo 2. Double-click mongodb-installer.msi
    echo 3. Follow the installation wizard
    echo 4. Choose "Complete" installation
    echo 5. Install MongoDB as a service (recommended)
    echo.
    echo After installation, run start_mongodb.bat to start the service
    echo.
) else (
    echo.
    echo Download failed. Please try again or download manually from:
    echo https://www.mongodb.com/try/download/community
    echo.
)

pause 