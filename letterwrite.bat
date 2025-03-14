@echo on
REM Activate Anaconda Environment
call "C:\Users\don_m\Anaconda3\Scripts\activate.bat"

REM Change to the working directory
cd C:\Users\don_m\Python\ZDAnalytics\temp

REM Optional: Activate virtual environment if required
call venv\Scripts\activate

REM Run the letterwrite program (uncomment and adjust as needed)
letterwrite

REM Keep the command prompt open
REM pause



