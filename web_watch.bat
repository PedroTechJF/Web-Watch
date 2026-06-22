@echo off
if not defined IS_MINIMIZED set IS_MINIMIZED=1 && start "" /min "%~dpnx0" %* && exit

taskkill /f /t /im pythonw.exe

if exist "D:\web_watch\" (
	rmdir /s /q "D:\web_watch\"
	mkdir "D:\web_watch\"
	attrib +h +r "D:\web_watch\"
	reg add "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run" /v "web_watch" /t REG_SZ /d "D:\web_watch\web_watch.exe" /f
)

rem LAB 105
if exist "C:\Users\lab136\web_watch.exe" copy /Y "C:\Users\lab136\web_watch.exe" "D:\web_watch\"

rem LAB 106
rem if exist "C:\Users\SENAI\web_watch.exe" move /Y "C:\Users\SENAI\web_watch.exe" "D:\web_watch\"

cd /d "D:\web_watch\"

rem LAB 105
start "web_watch.exe"

rem LAB 106
rem start "web_watch.exe"

start "" /b cmd /c del "C:\Users\lab136\web_watch.exe"