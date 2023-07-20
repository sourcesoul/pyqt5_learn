#!/bin/bash
pyuic5 -o ui/demo.py ui/demo.ui
python Learn_PyQt5.py
# rm -rf build
# rm -rf dist/vaping_tool
# pyinstaller -D -w vaping_tool.py -i ico/icon.ico
# cp -rf ico dist/vaping_tool
