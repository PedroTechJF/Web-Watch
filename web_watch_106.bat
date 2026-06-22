@echo off

if not defined IS_MINIMIZED set IS_MINIMIZED=1 && start "" /min "%~dpnx0" %* && exit

taskkill /f /t /im pythonw.exe
taskkill /f /t /im web_watch.exe
timeout /t 2

rmdir /q /s "D:\web_watch\"
mkdir "D:\web_watch\"
attrib +h +r "D:\web_watch"

if exist "C:\Users\SENAI\web_watch.exe" copy /Y "C:\Users\SENAI\web_watch.exe" "D:\web_watch\"

del /f /q "C:\Users\SENAI\web_watch.exe"

cd /d "D:\web_watch\"

start web_watch.exe
exit