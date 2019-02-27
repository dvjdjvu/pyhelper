#!/usr/bin/env python3.2
#encoding: UTF-8

import time
import datetime

def date_min_day(date_text, date_format):
    """
    Вычесть из даты одни сутки.
        
    Args:
        date_text:      (String) Дата.
        date_format:    (String) Формат.
            
    Returns:
        (String) Новая дата.
        
    Examples:
        >>> date_min_day('1990 12 15 16 59 22', '%Y %m %d %H %M %S')
        '1990 12 14 16 59 22'
    """
    
    #date_format = date_format.replace('H.N', 'H.M').replace('D.M.y', '%d.%m.%y')
    
    #tmb = datetime.datetime.strptime(date_text, date_format) - datetime.timedelta(days=1)
    tmb = datetime.datetime(*(time.strptime(date_text, date_format)[0:6])) - datetime.timedelta(days=1)
    
    return tmb.strftime(date_format)

def date_plus_year(date_text, date_format):
    """
    Прибавить к дате один год.
        
    Args:
        date_text:      (String) Дата.
        date_format:    (String) Формат.
            
    Returns:
        (String) Новая дата.
        
    Examples:
        >>> date_plus_year('1990 12 15 16 59 22', '%Y %m %d %H %M %S')
        '1991 12 14 16 59 22'
    """
    
    #date_format = date_format.replace('H.N', 'H.M').replace('D.M.y', '%d.%m.%y')
    
    #tmb = datetime.datetime.strptime(date_text, date_format) + datetime.timedelta(years=1)
    #tmb = datetime.datetime(*(time.strptime(date_text, date_format)[0:6])) + datetime.timedelta(years=1)
    tmb = datetime.datetime(*(time.strptime(date_text, date_format)[0:6]))
    tmb = tmb.replace(tmb.year + 1)
    
    return tmb.strftime(date_format)

def date_compare(date1, date2, date_format1, date_format2):
    """
    Сравнение дат.
        
    Args:
        date1:      (String) Дата 1.
        date2:      (String) Дата 2.
        date_format1:    (String) Формат 1.
        date_format2:    (String) Формат 2.
            
    Returns:
        (Bool) True Если date1 новее чем date2. False иначе.
        
    Examples:
        >>> is_date('1989 12 15 16 59 22', '1990 12 15 16 59 22', '%Y %m %d %H %M %S', '%Y %m %d %H %M %S')
        False
    """
    
    #if datetime.datetime.strptime(date1, date_format1) > datetime.datetime.strptime(date2, date_format2) :
    if datetime.datetime(*(time.strptime(date1, date_format1)[0:6])) > datetime.datetime(*(time.strptime(date2, date_format2)[0:6])) :
        return True
    
    return False

def date_mouths_rus_to_eng(_str):
    """
    Приведение в строке полных русских месяцев к коротким английским.
        
    Args:
        _str:   (String) Строка.
            
    Returns:
        (String) Строка с англ. месяцами.
        
    Examples:
        >>> date_mouths_rus_to_eng('апрель Май')
        'Apr May'
    """
    
    _str = _str.lower()
    
    _str = _str.replace('январь', 'Jan')
    _str = _str.replace('февраль', 'Feb')
    _str = _str.replace('март', 'Mar')
    _str = _str.replace('апрель', 'Apr')
    _str = _str.replace('май', 'May')
    _str = _str.replace('июнь', 'June')
    _str = _str.replace('июль', 'July')
    _str = _str.replace('август', 'Aug')
    _str = _str.replace('сентябрь', 'Sept')
    _str = _str.replace('октябрь', 'Oct')
    _str = _str.replace('ноябрь', 'Nov')
    _str = _str.replace('декабрь', 'Dec')
    
    return _str.lower()