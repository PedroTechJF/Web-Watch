@echo off

rem if not defined IS_MINIMIZED set IS_MINIMIZED=1 && start "" /min "%~dpnx0" %* && exit

:: --- CONFIGURATION ---
set "AppName=web_watch.exe"
set "AppPath=D:\web_watch\web_watch.exe"
set "CheckInterval=10"
:: ---------------------

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
