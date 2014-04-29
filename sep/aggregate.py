"""
Agreggate conta quantas entradas para um determinado valor X
existem em um conjunto de dados Y (linha por linha)
"""

import re

PATTERN_NAME = ['ARF', 'EADI','ARMAZEM', 'FISCALIZACAO' , 'GERAIS', 'DRJ', 'DRF', 'RFB', 'CAC', 'DEFIS', 'DEINF', 'DEMAC', 'DMA', 'PSR', 'PSF', 'IRF', 'CUF', 'SRRF', 'DERAT', 'POSTO', 'FISCAL', 'PTN', 'PORTO'] 
UFS = 'AC,AL,AM,AP,BA,CE,DF,ES,GO,MA,MG,MS,MT,PA,PB,PE,PI,PR,RJ,RN,RO,RR,RS,SC,SE,SP,TO'.split(',') 

def load_file(filename):
    """Load file csv"""
    f = open(filename, 'r')
    return f

def check_exist(term, line):
    """Check if exist value in line"""
    m = re.search(term, line, re.IGNORECASE) 
    if m:
        return True
    else:
        return False

def iterate(callback_function, term, f):
    f.seek(0)
    
    for line in f.readlines():
        response = callback_function(term, line)
        if response:
            return response

    return False

def remove_pattern_name(name):
    """
    Remove padroes de nomes repetidos e retorna uma lista de termos,
    possivelmente, significante para a busca.

    Ex.: RFB_EADI_SANTOS -> SANTOS
    """
    removed = name.replace('_', ',')
    for pattern in PATTERN_NAME:
        if removed:
            removed = removed.replace(pattern, '')
        else:
            removed = name.replace(pattern, '')
    
    return filter(None, removed.split(','))

