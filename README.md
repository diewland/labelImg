# labelImg (python3 build from Windows)

### Installation
```
python3 -m venv venv
venv\Scripts\activate.bat
pip install -r requirements\requirements-include-installer.txt
pyrcc5 -o resources.py resources.qrc
```

### Build exe
```
cd build-tools
build-windows-binary-python3.bat
```
build files will created in dist/ folder

### References
* https://github.com/tzutalin/labelImg
* https://www.cryptlife.com/coding-series/convert-py-to-exe-python-3
