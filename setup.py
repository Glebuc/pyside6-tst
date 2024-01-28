import sys
import os
from cx_Freeze import setup, Executable


files = ['icon.ico','themes/']

# TARGET
target = Executable(
    script="main.py",
    base="Win32GUI",
    icon="icon.ico"
)

setup(
    name = "Aramid TsT Graph",
    version = "1.0",
    description = "Application for view data functional testing in operating system Aramid",
    author = "Deryugin Gleb",
    options = {'build_exe' : {'include_files' : files}},
    executables = [target]
    
)
