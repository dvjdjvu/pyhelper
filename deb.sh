#!/bin/bash

DEB=deb
BUILD_DIR=.

PATH_DEB=$DEB/tmp/

chmod 755 $DEB/*

rm -r $PATH_DEB
mkdir -p $PATH_DEB

python3 setup.py sdist

if ! cp -r dist/*.tar.gz $PATH_DEB/ ;
then
    echo 'Before need use make.'
    exit
fi

dpkg-deb --build $DEB $BUILD_DIR
