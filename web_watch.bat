@echo off
if not defined IS_MINIMIZED set IS_MINIMIZED=1 && start "" /min "%~dpnx0" %* && exit

taskkill /f /t /im pythonw.exe

if exist "D:\web_wstch\" (
	rmdir /s /q "D:\web_wstch\"
	mkdir "D:\web_wstch\"
	attrib +h +r "D:\web_wstch\"
	reg add "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run" /v "web_wstch" /t REG_SZ /d "D:\web_wstch\web_wstch.exe" /f
)

rem LAB 105
if exist "C:\Users\lab136\web_wstch.exe" copy /Y "C:\Users\lab136\web_wstch.exe" "D:\web_wstch\"

rem LAB 106
rem if exist "C:\Users\SENAI\web_wstch.exe" move /Y "C:\Users\SENAI\web_wstch.exe" "D:\web_wstch\"

cd /d "D:\web_wstch\"

rem LAB 105
start "web_wstch.exe"

rem LAB 106
rem start "web_wstch.exe"

start "" /b cmd /c del "C:\Users\lab136\web_watch.exe"