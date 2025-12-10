@echo off
echo ========================================
echo   PBA Function Checker - Build Script
echo ========================================
echo.

echo [1/4] Cleaning previous build...
if exist "build" rmdir /s /q "build"
if exist "dist" rmdir /s /q "dist"
if exist "__pycache__" rmdir /s /q "__pycache__"
echo      Done!
echo.

echo [2/4] Checking PyInstaller...
python -m pip show pyinstaller >nul 2>&1
if errorlevel 1 (
    echo      PyInstaller not found. Installing...
    python -m pip install pyinstaller
) else (
    echo      PyInstaller found!
)
echo.

echo [3/4] Building executable with PyInstaller...
python -m PyInstaller Main.spec --clean --noconfirm
if errorlevel 1 (
    echo.
    echo ========================================
    echo   BUILD FAILED!
    echo ========================================
    pause
    exit /b 1
)
echo      Done!
echo.

echo [4/4] Copying additional files...
if exist "dist\Main.exe" (
    xcopy /E /I /Y "Resource" "dist\Resource\" >nul
    xcopy /E /I /Y "Logo" "dist\Logo\" >nul
    copy /Y "config.json" "dist\" >nul
    copy /Y "version.txt" "dist\" >nul
    echo      Done!
    echo.
    echo ========================================
    echo   BUILD SUCCESSFUL!
    echo ========================================
    echo.
    echo   Output: dist\Main.exe
    echo.
    echo   Files included:
    echo   - Main.exe
    echo   - config.json
    echo   - version.txt
    echo   - Resource folder
    echo   - Logo folder
    echo.
) else (
    echo.
    echo ========================================
    echo   BUILD FAILED - EXE not found!
    echo ========================================
)

echo.
pause
