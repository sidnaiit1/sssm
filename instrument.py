
import functools
import math

from equity.gbce.trades.constant import InstAttr, SymbolType


def singleton(theClass):
    """ decorator for a class to make a singleton out of it """
    classInstances = {}

    def getInstance(*args, **kwargs):
        key = (theClass, args, str(kwargs))
        if key not in classInstances:
            classInstances[key] = theClass(*args, **kwargs)
        return classInstances[key]

    return getInstance

@singleton
class Instrument(object):
    
    def __init__(self, symbol='', symboltype='', lastdivident=0,fixeddivident=0,parvalue=0):
        self.symbol = symbol
        self.symboltype = symboltype
        self.lastdivident = lastdivident
        self.fixeddivident = fixeddivident
        self.parvalue = parvalue

'''
there are the below static list of instruments on which trading is done
'''
instruments = {
    'TEA': {InstAttr.SYMBOL:'TEA',
            InstAttr.SYMBOLTYPE:SymbolType.COMMON, 
            InstAttr.LASTDIVIDENT:0,
            InstAttr.FIXEDDIVIDENT:0,
            InstAttr.PARVALUE:100},
    'POP' : {InstAttr.SYMBOL:'POP',
             InstAttr.SYMBOLTYPE:SymbolType.COMMON, 
             InstAttr.LASTDIVIDENT:8,
             InstAttr.FIXEDDIVIDENT:0,
             InstAttr.PARVALUE:100},
    'ALE' : {InstAttr.SYMBOL:'ALE',
             InstAttr.SYMBOLTYPE:SymbolType.COMMON, 
             InstAttr.LASTDIVIDENT:0,
             InstAttr.FIXEDDIVIDENT:0,
             InstAttr.PARVALUE:100},
    'GIN' : {InstAttr.SYMBOL:'GIN',
             InstAttr.SYMBOLTYPE:SymbolType.COMMON, 
             InstAttr.LASTDIVIDENT:0,
             InstAttr.FIXEDDIVIDENT:0,
             InstAttr.PARVALUE:100},
    'JOE' : {InstAttr.SYMBOL:'JOE',
             InstAttr.SYMBOLTYPE:SymbolType.COMMON, 
             InstAttr.LASTDIVIDENT:0,
             InstAttr.FIXEDDIVIDENT:0,
             InstAttr.PARVALUE:100},
    }

def GetInstrument(symbol):
    d = instruments.get(symbol)
    return Instrument(**d)

