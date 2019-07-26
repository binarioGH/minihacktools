@echo off
set dest=%appdata%\Microsoft\Windows\Start Menu\Programs\Startup
cd %dest%	
echo dir: %dest%
:movestuff
if %2 == -l goto link
echo Copying!
copy %1 %dest%
goto ext
:link
echo Linking!
echo start %1 > link.bat
:ext
echo bye