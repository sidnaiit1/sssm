'''
This class contains the trade details
'''

from equity.gbce.trades.constant import SymbolType

class Trade(object):
    
    def __init__(self, instrument, quantity, price, timestamp, buysell):
        self.instrument = instrument
        self.quantity = quantity
        self.price = price
        self.timestamp = timestamp
        self.buysell = buysell
        self.divyield = self._divident_yield()
        self.peratio = self._pe_ratio()

    ''' Given any price as input, calculate the dividend yield'''
    def _divident_yield(self):
        if self.price == 0:
                raise Exception("Trade price cannot be zero")
            
        if self.instrument.symboltype.upper() == SymbolType.COMMON:
            return (self.instrument.lastdivident/self.price)
        if self.instrument.symboltype.upper() == SymbolType.PREFERRED:
            return ((self.instrument.fixeddivident * self.instrument.par)/self.price)
    
    ''' Given any price as input, calculate the P/E Ratio '''
    def _pe_ratio(self):
        if self.divyield == 0:
            return 0
        return (self.price/self.divyield)
    
    def __str__(self, *args, **kwargs):
        msg = "inst:%s qty:%s price:%s timestamp:%s buysell:%s divyied:%s peratio:%s"
        return msg%(self.instrument.symbol, self.quantity, self.price, self.timestamp, self.buysell, self.divyield, self.peratio)
        
    
    