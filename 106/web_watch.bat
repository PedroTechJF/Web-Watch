@echo off

if not defined IS_MINIMIZED set IS_MINIMIZED=1 && start "" /min "%~dpnx0" %* && exit

set "Version=106"
set "AppName=Web Watch - %Version%.exe"

taskkill /f /t /im "%AppName%" 2>nul
timeout /t 2

rmdir /q /s "D:\web_watch\" 2>nul
mkdir "D:\web_watch\"
attrib +h +r "D:\web_watch"
if exist "C:\Users\%username%\%AppName%" copy /Y "C:\Users\%username%\%AppName%" "D:\web_watch\"
rem del "%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup\web_watch.lnk" 2>nul
rem mklink "%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup\web_watch.lnk" "D:\web_watch\%AppName%" 2>nul

del /f /q "C:\Users\%username%\%AppName%" 2>nul

start "" "D:\web_watch\%AppName%"
exit