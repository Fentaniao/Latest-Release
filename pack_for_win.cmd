@echo INFO: This is a cmd for packing this python script automatically in Windows OS
@echo INFO: First you should install python3 into your PC
python --version

@echo Process: Update pip...
python -m pip install --upgrade pip
python -m pip --version
@echo Process: Update pyinstaller...
pip install pyinstaller
python -m PyInstaller --version

@echo Process: Start packing...
python -m PyInstaller -F main.py

@echo INFO: Finish packing.
pause