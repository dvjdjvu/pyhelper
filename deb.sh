#!/bin/bash

DEB=deb
BUILD_DIR=.

PATH_DEB=$DEB/tmp/

chmod 755 $DEB/*

rm -r $PATH_DEB
mkdir -p $PATH_DEB

cp -r dist/*.tar.gz $PATH_DEB/

dpkg-deb --build $DEB $BUILD_DIR
