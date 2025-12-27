# python-worst-sound-controller
The worst sound control have ever made to the public using Python (tkinter, pycaw).
You would need PyInstaller to create the excutable also you need pycaw, comtypes to use the code.
Install PyInstaller, pycaw, comtypes:
```cmd
pip install pyinstaller pycaw comtypes
```
Convert to exe:
```cmd
PyInstaller audio.py --onefile --noconsole --icon=aud.ico
```
The result would in `dist`
You would need Python 64-bit 3.11+
