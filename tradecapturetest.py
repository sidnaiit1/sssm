from equity.gbce.trades.tradecapture import TradeCapture

trades = [
    {'symbol':'TEA','quantity': 200,'price':10,'timestamp':200,'buysell':1},
    {'symbol':'POP','quantity': 200,'price':10,'timestamp':200,'buysell':1},
    {'symbol':'ALE','quantity': 200,'price':10,'timestamp':200,'buysell':1},
    {'symbol':'GIN','quantity': 200,'price':10,'timestamp':200,'buysell':1},
    {'symbol':'JOE','quantity': 200,'price':10,'timestamp':200,'buysell':1},
    {'symbol':'TEA','quantity': 100,'price':10,'timestamp':300,'buysell':-1},
    {'symbol':'POP','quantity': 100,'price':20,'timestamp':300,'buysell':-1},
    {'symbol':'ALE','quantity': 100,'price':30,'timestamp':300,'buysell':-1},
    {'symbol':'GIN','quantity': 100,'price':40,'timestamp':300,'buysell':-1},
    {'symbol':'JOE','quantity': 100,'price':50,'timestamp':300,'buysell':-1},
    ]

class TradeCaptureTest(object):
    
    def __init__(self):
        self.tc = TradeCapture()
        self.populate_trades()
    
    def populate_trades(self):
        for t in trades:
            self.tc.recordtrade(t)
    
    def printtrades(self):
        for i,ts in self.tc.tradesbyinst.items():
            print(i)
            for t in ts:
                print(t)
    
    def printtradecapture(self):
        for i in self.tc.tradesbyinst.keys():
            print(self.tc.calc_vol_weight_stk_price(i.symbol))
        print(self.tc.calc_all_share_index())
        
def main():
    ttest = TradeCaptureTest()
    ttest.printtrades()
    ttest.printtradecapture()

if __name__== "__main__":
  main()
                