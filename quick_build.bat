@echo off
REM Quick build - Just run PyInstaller
python -m PyInstaller Main.spec --clean --noconfirm
echo.
echo Build complete! Check dist\ folder
pause
