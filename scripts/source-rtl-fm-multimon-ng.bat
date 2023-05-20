@echo off
echo INPUT: rtl_fm Device 1>&2
IF EXIST .\rtl-sdr-release SET PATH=%PATH%;.\rtl-sdr-release
IF EXIST .\rtl-sdr-release\sox-14-4-2 SET PATH=%PATH%;.\rtl-sdr-release\sox-14-4-2
set PPM=0
set FREQ=162.475M
set GAIN=42
:loop
rtl_fm -f %FREQ% -M fm -s 22050 -E dc -p %PPM% -g %GAIN% |  multimon-ng -t raw -a EAS - 
echo Restarting... >&2
timeout /t 2 /nobreak
goto loop
