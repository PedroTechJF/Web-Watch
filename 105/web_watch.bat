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

taskkill /f /t /im "%AppName%"
timeout /t 2

rmdir /q /s "D:\web_watch\"
mkdir "D:\web_watch\"
attrib +h +r "D:\web_watch"
if exist "C:\Users\%username%\%AppName%" copy /Y "C:\Users\%username%\%AppName%" "D:\web_watch\"
reg delete "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run" /v "Web Watch" /f
reg add "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run" /v "Web Watch" /t REG_SZ /d "D:\web_watch\%AppName%" /f

if exist "C:\Users\%username%\%AppName%" copy /Y "C:\Users\%username%\%AppName%" "D:\web_watch\"

del /f /q "C:\Users\%username%\%AppName%"

cd /d "D:\web_watch\"

start "%AppName%"
exit