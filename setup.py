import sys
from cx_Freeze import setup, Executable


build_exe_options = {
    "packages": ["os", "sys", "PySide6"],
    "includes": ["loger", "Application", "pages", "ui_modules", "SettingApp", "utils"],
    "include_files": [],
}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="Arami-TsT Graph",
    version="0.1",
    description="Your application description",
    options={"build_exe": build_exe_options},
    executables=[Executable("main.py", base=base, icon="./images/icons/aramid.svg")],
)
