import pprint

from yahoo_ff.database import stocks_database
from yahoo_ff.yahoo_ff import yahoo_ff

def main():
    stocks_database('sp500')
    # pp = pprint.PrettyPrinter(indent=0)
    #
    # aapl = yahoo_ff('aapl')
    #
    # pp.pprint(aapl.keystats)
    #
    # # go through all stocks
    # sp500 = stocks_database('sp500')
    #
    # # assign the stock to object
    # aapl = sp500.take('aapl')
    #
    # # get variables
    # pp.pprint(aapl)
    # pp.pprint(aapl.infos)
    # pp.pprint(aapl.infos['sector'])
    #
    # ends = list(reversed(aapl.incomestatement_annual['endofperiod']))
    # pp.pprint(ends)
    #
    # p = aapl.pricehistory['Adj. Close'].asof(ends)
    # pp.pprint(p.values)
    #
    # e = list(reversed(aapl.incomestatement_annual['Earnings Before Interest And Taxes']))
    # pp.pprint(e)
    #
    # pe = [price/earnings for price, earnings in zip(p, e)]
    # pp.pprint(pe)


def empty_space():
    print '\n'


if __name__ == "__main__":
    main()
