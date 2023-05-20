@echo off
echo INPUT: Current Sound Recording Device 1>&2
:loop
multimon-ng -a EAS
echo Restarting... >&2
timeout /t 2 /nobreak
goto loop