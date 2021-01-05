#!/bin/bash

pyside2-rcc sketches/resources/resources.qrc -o src/UI/rc_resources.py
pyside2-uic sketches/$1.ui > src/UI/ui_$1.py

