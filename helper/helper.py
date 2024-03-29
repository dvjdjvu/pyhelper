#!/usr/bin/env python3
# encoding: UTF-8

import sys
import inspect

from .date import date
from .proc import proc
from .string import string
from .type import type
from .log import log


def getDigit(number, n):
    """
    Взять n-ю цифру из N-значного числа.
        
    Args:
        s:       (Int) Число.
        amount:  (Int) n-ая цифра.
            
    Returns:
        (Int).
    """

    return number // 10 ** n % 10


def LINE():
    try:
        raise Exception
    except:
        return sys.exc_info()[2].tb_frame.f_back.f_lineno


def FILE():
    """
    Имя текущего файла.
          
    Returns:
        String
    """

    return inspect.currentframe().f_code.co_filename
