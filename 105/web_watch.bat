@echo off

if not defined IS_MINIMIZED set IS_MINIMIZED=1 && start "" /min "%~dpnx0" %* && exit

set "User="
set "Version=105"
if /I "%username%"=="lab136" (
    set "User=lab105"
) else (
    set "User=lab"
)
set "AppName=Web Watch - %Version%.exe"

taskkill /f /t /im "%AppName%" 2>nul
timeout /t 2>nul

rmdir /q /s "D:\web_watch\" 2>nul
mkdir "D:\web_watch\"
attrib +h +r "D:\web_watch"
if exist "C:\Users\%username%\%AppName%" copy /Y "C:\Users\%username%\%AppName%" "D:\web_watch\"
reg delete "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run" /v "Web Watch" /f 2>nul
reg add "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run" /v "Web Watch" /t REG_SZ /d "D:\web_watch\%AppName%" /f

del /f /q "C:\Users\%username%\%AppName%" 2>nul

start "" "D:\web_watch\%AppName%"
exit