#!/usr/bin/env python3
# encoding: UTF-8

import datetime


def is_int(s):
    """
    # Проверка строки на int.
        
    Args:
        s:       (String) Строка.
            
    Returns:
        (Bool) True/False
    """

    if s == '':
        return True

    try:
        int(s)
        return True
    except Exception:
        return False

    return False


def is_float(s):
    """
    # Проверка строки на float.
        
    Args:
        s:       (String) Строка.
            
    Returns:
        (Bool) True/False
    """

    if s == '':
        return True

    try:
        float(s)
        return True
    except Exception:
        return False

    return False


def is_date(date_text):
    """
    Проверка даты. По формату '%Y-%m-%d'
        
    Args:
        date_text:  (String) Дата.
            
    Returns:
        (Bool) True/False
        
    Examples:
        >>> is_date('1990-12-15')
        True
    """

    try:
        datetime.datetime.strptime(date_text, '%Y-%m-%d')
        return True
    except Exception:
        return False


def is_date(date_text, date_format):
    """
    Проверака даты и времени по формату.
        
    Args:
        date_text:      (String) Дата.
        date_format:    (String) Формат.
            
    Returns:
        (Bool) True/False
        
    Examples:
        >>> is_date('1990 12 15 15 59 22', '%Y %m %d %H %M %S')
        True
    """

    try:
        # dt = datetime.datetime.strptime(date_text, date_format)
        dt = datetime.datetime(*(time.strptime(date_text, date_format)[0:6]))
        return True
    except Exception:
        return False
