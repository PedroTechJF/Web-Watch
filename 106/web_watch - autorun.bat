@echo off

if not defined IS_MINIMIZED set IS_MINIMIZED=1 && start "" /b "%~dpnx0" %* && exit

title Web Watch - Autorun
:: --- CONFIGURATION ---
set "Version=106"
set "AppName=Web Watch - %Version%.exe"
set "AppPath=D:\web_watch\%AppName%"
set "CheckInterval=5"
:: ---------------------

taskkill /f /t /im "%AppName%"

:loop
:: Check if the process is currently running
tasklist /FI "IMAGENAME eq %AppName%" 2>NUL | find /I "%AppName%" >NUL

if %errorlevel% equ 1 (
    echo [%date% %time%] %AppName% is closed. Restarting...
    start "" "%AppPath%"
) else (
    echo [%date% %time%] %AppName% is running normally.
)

:: Wait before checking again
timeout /t %CheckInterval% /nobreak >nul
goto loop
