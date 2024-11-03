@echo off
REM Set the environment
set PYTHON_EXEC=C:\Users\Hien Ta\OneDrive\Python_100_Days\venv\Scripts\python.exe
set PROJECT_DIR=C:\Users\Hien Ta\OneDrive\Python_100_Days\Data Engineer Project Portfolio

REM Run Extract Data
echo Running Extract Data Script...
%PYTHON_EXEC% %PROJECT_DIR%\Step 1_extract_data.py
IF %ERRORLEVEL% NEQ 0 (
    echo Extract Data Script Failed. Exiting.
    exit /b %ERRORLEVEL%
)
echo Extract Data Script Completed Successfully.

REM Run Transform Data
echo Running Transform Data Script...
%PYTHON_EXEC% %PROJECT_DIR%\Step 2_transform_data.py
IF %ERRORLEVEL% NEQ 0 (
    echo Transform Data Script Failed. Exiting.
    exit /b %ERRORLEVEL%
)
echo Transform Data Script Completed Successfully.

REM Run Load Data
echo Running Load Data Script...
%PYTHON_EXEC% %PROJECT_DIR%\Step 3_load_data.py
IF %ERRORLEVEL% NEQ 0 (
    echo Load Data Script Failed. Exiting.
    exit /b %ERRORLEVEL%
)
echo Load Data Script Completed Successfully.

echo All ETL steps completed successfully.
