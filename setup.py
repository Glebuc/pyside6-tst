import sys
import os
from cx_Freeze import setup, Executable


# TARGET
target = Executable(
    script="main.py",
    base="Win32GUI"
)

setup(
    name="Aramid TsT Graph",
    version="1.0",
    description="Application for view data functional testing in operating system Aramid",
    author="Deryugin Gleb",
    executables=[target]

)
