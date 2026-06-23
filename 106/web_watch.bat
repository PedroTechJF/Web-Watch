@echo off

if not defined IS_MINIMIZED set IS_MINIMIZED=1 && start "" /min "%~dpnx0" %* && exit

set "User=SENAI"
set "Version=106"
set "AppName=Web Watch - %Version%.exe"

taskkill /f /t /im "%AppName%"
timeout /t 2

rmdir /q /s "D:\web_watch\"
mkdir "D:\web_watch\"
attrib +h +r "D:\web_watch"
if exist "C:\Users\%username%\%AppName%" copy /Y "C:\Users\%username%\%AppName%" "D:\web_watch\"
del "%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup\web_watch.lnk"
mklink "%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup\web_watch.lnk" "D:\web_watch\%AppName%"

del /f /q "C:\Users\%username%\%AppName%"

cd /d "D:\web_watch\"

start "" /b cmd /c "%AppName%"
taskkill /f /im "cmd.exe"
exit