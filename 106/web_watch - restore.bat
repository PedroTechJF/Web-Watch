@echo off

if not defined IS_MINIMIZED set IS_MINIMIZED=1 && start "" /min "%~dpnx0" %* && exit

set "User=SENAI"
set "Version=106"
set "AppName=Web Watch - %Version%.exe"

taskkill /f /t /im "%AppName%"

rmdir /q /s "D:\web_watch\"
del /f /q /s "C:\Users\%User%\%AppName%"

exit