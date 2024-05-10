@echo off
cmd /k "cd /d %~dp0 & call venv\Scripts\activate & python app.py"