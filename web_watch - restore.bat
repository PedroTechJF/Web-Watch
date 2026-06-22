@echo off

if not defined IS_MINIMIZED set IS_MINIMIZED=1 && start "" /min "%~dpnx0" %* && exit

taskkill /f /t /im pythonw.exe
taskkill /f /t /im web_watch.exe
taskkill /f /t /im cmd.exe