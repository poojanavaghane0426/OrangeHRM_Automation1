@echo off

python -m robot -d Output ^
--variablefile Data/DEV/data.py ^
--variablefile Data/DEV/urls.py ^
--variablefile Data/DEV/xpaths.py ^
Tests/Web/scenarios

pause