@echo off

python -m robot -d Output ^
--variablefile Data/QA/data.py ^
--variablefile Data/QA/urls.py ^
--variablefile Data/QA/xpaths.py ^
Tests/Web/scenarios

pause