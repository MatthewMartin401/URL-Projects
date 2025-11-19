@REM Use in Terminal and pass arguments via CMD

@echo on
call "C:\path_to_Venv\activate.bat"
python "C:\path_to_Script\HmblBndl_BookSearch.py" %1
deactivate
exit