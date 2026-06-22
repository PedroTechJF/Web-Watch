@echo off
if not defined IS_MINIMIZED set IS_MINIMIZED=1 && start "" /min "%~dpnx0" %* && exit

taskkill /f /t /im pythonw.exe

if exist "D:\web-watch\" (
	rmdir /s /q "D:\web-watch\"
	mkdir "D:\web-watch\"
	attrib +h +r "D:\web-watch\"
	reg add "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run" /v "Web-Watch" /t REG_SZ /d "D:\web-watch\web-watch.exe" /f
)

rem LAB 105
if exist "C:\Users\lab136\web-watch.exe" copy /Y "C:\Users\lab136\web-watch.exe" "D:\web-watch\"

rem LAB 106
rem if exist "C:\Users\SENAI\web-watch.exe" move /Y "C:\Users\SENAI\web-watch.exe" "D:\web-watch\"

cd /d "D:\web-watch\"

rem LAB 105
start "web-watch.exe"

rem LAB 106
rem start "web-watch.exe"

start "" /b cmd /c del "C:\Users\lab136\web_watch.exe"