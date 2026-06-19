@echo off
if not defined IS_MINIMIZED set IS_MINIMIZED=1 && start "" /min "%~dpnx0" %* && exit

taskkill /f /t /im pythonw.exe

pip install pywin32 pyautogui requests schedule pip-system-certs pywinauto -qqq

if not exist "D:\III\" (
	mkdir "D:\III\"
)

attrib +h +r "D:\III\"

rem LAB 105
if exist "C:\Users\lab136\III.pyw" move /Y "C:\Users\lab136\III.pyw" "D:\III\"

rem LAB 106
rem if exist "C:\Users\SENAI\III.pyw" move /Y "C:\Users\SENAI\III.pyw" "D:\III\"

cd /d "D:\III\"

rem LAB 105
start "C:\Program Files\Python314\pythonw.exe" "III.pyw"

rem LAB 106
rem start C:\Users\lab136\AppData\Local\Programs\Python\Python38\pythonw.exe "III.pyw"

exit