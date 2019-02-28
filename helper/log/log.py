#!/usr/bin/env python3
#encoding: UTF-8

import re
import datetime
from helper.proc import proc

DEBUG_LEVEL = ''

class BColors:
    """
    Класс с кодами цветов для консоли.
    """
    
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    
def setDebugLevel(level):
    pass
    
def debugLevelToInt():
    """
    Приведение строкового уровня дебага к числовому.
          
    Returns:
        Int
    """     
    
    if DEBUG_LEVEL == 'critical':
        return 6
    elif DEBUG_LEVEL == 'error':
        return 5
    elif DEBUG_LEVEL == 'warning':
        return 4
    elif DEBUG_LEVEL == 'notice':
        return 3
    elif DEBUG_LEVEL == 'info':
        return 2
    else:
        return 1
    
def Print(*args) :
    """
    Функция печати, с уровнеи дебага и подсветкой критических участков.
    """   
    
    level = 1
    objs = ''

    for arg in args :
        objs += str(arg) + ' '
    
    objs = proc.getName() + ':[' + datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S") + ']' + str(objs)
    
    if re.search(r'\[critical\]', objs) :
        objs = objs.replace('[critical]', '')
        objs =  BColors.FAIL + '[critical]' + BColors.ENDC + ':' + objs
        level = 6
    elif re.search(r'\[error\]', objs) :
        objs = objs.replace('[error]', '')
        objs =  BColors.HEADER + '[error]' + BColors.ENDC + ':' + objs
        level = 5
    elif re.search(r'\[warning\]', objs) :
        objs = objs.replace('[warning]', '')
        objs =  BColors.WARNING + '[warning]' + BColors.ENDC + ':' + objs  
        level = 4
    elif re.search(r'\[notice\]', objs) :
        objs = objs.replace('[notice]', '')
        objs =  BColors.OKBLUE + '[notice]' + BColors.ENDC + ':' + objs  
        level = 3
    elif re.search(r'\[info\]', objs) :
        objs = objs.replace('[info]', '')
        objs =  BColors.OKGREEN + '[info]' + BColors.ENDC + ':' + objs
        level = 2
    else :
        level = 1
    
    if debugLevelToInt() <= level:
        print(objs)
        sys.stdout.flush()
        
