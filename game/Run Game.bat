@echo off
title Run Game
cls

python --version >NUL
if errorlevel 1 goto errorNoPython

:: Game Code Below...
python "prepare.py"
cls
python "part1.py"
cls
python "part2.py"

exit 0

:errorNoPython
echo.
echo Error: Please install Python 3 first!
echo Press any key to open the installation page...
pause>nul
start "" https://www.python.org/downloads
exit 0
