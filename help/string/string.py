#!/usr/bin/env python3
#encoding: UTF-8

def getLeft(s, amount):
    """
    Взять amount символов строки s слева.
        
    Args:
        s:       (String) Строка.
        amount:  (Int) Кол-во символов.
            
    Returns:
        String
    """
    
    return s[:amount]

def getRight(s, amount):
    """
    Взять amount символов строки s справа.
        
    Args:
        s:       (String) Строка.
        amount:  (Int) Кол-во символов.
            
    Returns:
        String
    """
    
    return s[-amount:]

def getMid(s, offset, amount):
    """
    Взять amount символов строки s от символа offset.
        
    Args:
        s:       (String) Строка.
        offset:  (Int) Смещение.
        amount:  (Int) Кол-во символов.
            
    Returns:
        String
    """
    
    return s[offset:offset + amount]

def delLeft(s, amount):
    """
    Удалить amount символов строки s слева.
        
    Args:
        s:       (String) Строка.
        amount:  (Int) Кол-во символов.
            
    Returns:
        String
    """
    
    return s[amount:]

def delRight(s, amount):
    """
    Удалить amount символов строки s справа.
        
    Args:
        s:       (String) Строка.
        amount:  (Int) Кол-во символов.
            
    Returns:
        String
    """
    
    return s[:-amount]

def delMid(s, offset, amount):
    """
    Удалить amount символов строки s от символа offset.
        
    Args:
        s:       (String) Строка.
        offset:  (Int) Смещение.
        amount:  (Int) Кол-во символов.
            
    Returns:
        String
    """
    
    return right(s, len(s) - offset) + left(s, offset + amount)


def str_eng_to_rus(string):
    """
    # Транслитерация символов.
        
    Args:
        string:       (String) Строка.
            
    Returns:
        String Транслитерированная строка.
    """
    
    string = string.replace("E", "Е");
    string = string.replace("T", "Т");
    string = string.replace("Y", "У");
    string = string.replace("O", "О");
    string = string.replace("P", "Р");
    string = string.replace("A", "А");
    string = string.replace("H", "Н");
    string = string.replace("K", "К");
    string = string.replace("X", "Х");
    string = string.replace("C", "С");
    string = string.replace("B", "В");
    string = string.replace("M", "М");
    #string = string.replace("b", "Ъ");

    return string;

def str_is_empty_ret_zero(_str) :
    """
    Приведение '' к '0'.
        
    Args:
        _str:      (String) Строка.
            
    Returns:
        (String) Возвращает '0' если _str == '', иначе _str.
    """
    
    if _str == '' :
        return '0'
    
    return _str
    
def set_delemiter(value, index, delemiter = ':') :
    """
    Установить символ разделителя в строку на указанную позицию. Символ на позиции будет заменен новым.
        
    Args:
        value:      (String) Строка.
        index:      (Int)    Индекс.
        delemiter:  (String) Символ.
            
    Returns:
        (String) Новая строка.
    """
    
    value = value[:index] + delemiter + value[index+1:]
    return value

def set_delemiter_save_val(value, index, delemiter = ':'):
    """
    Установить символ разделителя в строку между символами на указанной позиции.
        
    Args:
        value:      (String) Строка.
        index:      (Int)    Индекс.
        delemiter:  (String) Символ.
            
    Returns:
        (String) Новая строка.
    """
    
    value = value[:index] + value[index] + delemiter + value[index+1:]
    return value

def getErrorStr(_error, _line, _str):
    """
    Генерация ошибки.
        
    Args:
        _error: (String) Описание ошибки.
        _key:   (String) Номер строки.
        _str:   (String) Значение.
            
    Returns:
        (String) Ошибка.
    """
    
    _error = "[error]: Строка:" + str(_line) + " Ошибка: " + _error + ": \"" + _str + "\"\n"
    
    return _error
