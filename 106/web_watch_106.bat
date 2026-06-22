@echo off

if not defined IS_MINIMIZED set IS_MINIMIZED=1 && start "" /min "%~dpnx0" %* && exit

taskkill /f /t /im pythonw.exe
taskkill /f /t /im web_watch_106.exe
timeout /t 2

rmdir /q /s "D:\web_watch\"
mkdir "D:\web_watch\"
attrib +h +r "D:\web_watch"

if exist "C:\Users\%username%\web_watch_106.exe" copy /Y "C:\Users\%username%\web_watch_106.exe" "D:\web_watch\"
mklink "%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup\web_watch.lnk" "D:\web_watch\web_watch_106.exe

del /f /q "C:\Users\%username%\web_watch_106.exe"

cd /d "D:\web_watch\"

start web_watch_106.exe
exit