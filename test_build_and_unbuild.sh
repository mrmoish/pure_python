#!/bin/bash

# 🏗️ BUILD
python3 -m build

#удалить директории, которые появились после build
rm -r dist
rm -r mypackage.egg-info
