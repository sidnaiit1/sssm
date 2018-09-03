
from equity.gbce.trades.constant import InstAttr, TradeAttr
from equity.gbce.trades.instrument import GetInstrument
from equity.gbce.trades.trade import Trade
import logging
import functools
import math

'''
This is assumption the message would be dictionary format,
it could be xml/json/fix format, parse message should be able to 
parse and get the required attributes
'''
def parsemessage(message):
    return (message.get(InstAttr.SYMBOL,None),
            message.get(TradeAttr.QUANTITY,None),
            message.get(TradeAttr.PRICE,None),
            message.get(TradeAttr.TIMESTAMP,None),
            message.get(TradeAttr.BUYSELL,None))

class TradeCapture(object):
    
    def __init__(self):
        self.tradesbyinst = {} # inmemmory storage structure for trades received
    
    
    '''
    Record a trade, with timestamp, quantity, buy or sell indicator and price
    if any attribute is missing then log error
    '''
    def recordtrade(self,message):
        symbol, qty, price, timestamp, buysell = parsemessage(message)
        if not all([symbol, qty, price, timestamp, buysell]):
            logging.error("Not a valid trade")
            return
        i = GetInstrument(symbol)
        t = Trade(i, qty, price, timestamp, buysell)
        l = self.tradesbyinst.get(i,[])
        l.append(t)
        self.tradesbyinst[i] = l
    
    '''
    get last 5 mins trades done referencing from the timestamp of last trade
    '''
    def _get_last5min_trades(self,symbol):
        i = GetInstrument(symbol)
        trades = self.tradesbyinst.get(i,[])
        if not trades:
            return trades
        
        now = trades[-1].timestamp
        past5mintrades = [t for t in trades if ((now - t.timestamp) < 300)] # getting past 5 min trades
        return past5mintrades
        
    ''' Calculate Volume Weighted Stock Price based on trades in past 5 minutes '''
    def calc_vol_weight_stk_price(self,symbol):
        trades = self._get_last5min_trades(symbol)
        if not trades:
            logging.error('No trades executed for this symbol %s'%symbol)
            return None
        
        nominalamt = sum([t.price*t.quantity for t in trades])
        totalamt = sum([t.quantity for t in trades])
        return (nominalamt/totalamt) if totalamt else 0
    
    '''
    Calculate the GBCE All Share Index using the geometric mean of the 
    Volume Weighted Stock Price for all stocks
    '''
    def calc_all_share_index(self):
        vol_weights = []
        for i in self.tradesbyinst.keys():
            v = self.calc_vol_weight_stk_price(i.symbol)
            if v:
                vol_weights.append(v)
        if not vol_weights:
            return None
        sum = functools.reduce(lambda x,y:x*y,vol_weights)
        return math.pow(sum, 1/len(vol_weights))
    
    