#!/usr/bin/env python3
# encoding: UTF-8

import os, signal
from ctypes import cdll, byref, create_string_buffer


def setName(newName):
    """
    Изменение имени процесса для ps, в top не работает.
            
    Args:
        newName:   String Новое имя.
    """

    libc = cdll.LoadLibrary('libc.so.6')
    buff = create_string_buffer(len(newName) + 1)
    buff.value = newName.encode('utf-8')
    libc.prctl(15, byref(buff), 0, 0, 0)


def getName():
    """
    Получить имя этого процесса.
            
    Returns:
        String
    """

    libc = cdll.LoadLibrary('libc.so.6')
    buff = create_string_buffer(128)
    # 16 == PR_GET_NAME from <linux/prctl.h>
    libc.prctl(16, byref(buff), 0, 0, 0)

    return buff.value.decode("utf-8")


def shutdown(signum, frame):
    os.kill(0, signal.SIGTERM)
    os._exit(1)
