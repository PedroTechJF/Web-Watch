@echo off

if not defined IS_MINIMIZED set IS_MINIMIZED=1 && start "" /min "%~dpnx0" %* && exit

taskkill /f /t /im pythonw.exe
taskkill /f /t /im web_watch.exe
timeout /t 2

rmdir /q /s "D:\web_watch\"
mkdir "D:\web_watch\"
attrib +h +r "D:\web_watch"
rem reg add "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run" /v "web_watch" /t REG_SZ /d "D:\web_watch\web_watch.exe" /f

if exist "C:\Users\lab136\web_watch.exe" copy /Y "C:\Users\lab136\web_watch.exe" "D:\web_watch\"

del /f /q "C:\Users\lab136\web_watch.exe"

cd /d "D:\web_watch\"

start web_watch.exe
exit