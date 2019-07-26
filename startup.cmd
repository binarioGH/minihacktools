@echo off
set dest='%appdata%\Microsoft\Windows\Start Menu\Programs\Startup'
echo dir: %dest%
:movestuff
if %2 == -l goto link
copy %1 %dest%
goto ext

:link
echo start %1 >> link.bat
move link.bat %dest%
:ext
echo bye