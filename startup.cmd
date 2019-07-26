@echo off
set dest=%appdata%\Microsoft\Windows\Start Menu\Programs\Startup		
set filename=%1
set path=%2
set linkname=%3
if "%linkname%"=="" set linkname=link.bat
if "%path%"=="" set path=%cd%
cd %dest%
echo cd %path% > %linkname%
echo start %filename% >> %linkname%