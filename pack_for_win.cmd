@echo INFO: This is a cmd for packing this python script automatically in Windows OS
@echo Process: Update pip...
python -m pip install --upgrade pip
@echo Process: Update pip...
pip install pyinstaller
python -m PyInstaller --version
@echo Process: Start packing...
python -m PyInstaller -F main.py
@echo Process: Finish packing.
pause