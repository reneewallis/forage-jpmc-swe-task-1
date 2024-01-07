import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      ask_price = quote['top_ask']['price']
      bid = quote['top_bid']['price']
      self.assertEqual(getDataPoint(quote), (quote['stock'], bid, ask_price, (bid+ask_price)/2))

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      ask_price = quote['top_ask']['price']
      bid = quote['top_bid']['price']
      self.assertEqual(getDataPoint(quote), (quote['stock'], bid, ask_price, (bid+ask_price)/2 ))

  """ ------------ Add more unit tests ------------ """
  def test_getRatio(self):
    prices = {}
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
       'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
       'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    for quote in quotes:
      stock, bid_price, ask_price, price = getDataPoint(quote)
      prices[stock] = price
    """ ------------ Add the assertion below ------------ """
    self.assertEqual(getRatio(prices['ABC'], prices['DEF']), prices['ABC']/prices['DEF'])

  def test_getRatio_stockBPriceIsZero(self):
    prices = {'DEF': 0, 'ABC': 118.7}
    """ ------------ Add the assertion below ------------ """
    self.assertEqual(getRatio(prices['ABC'], prices['DEF']), None)

  def test_getRatio_stockAPriceIsZero(self):
    prices = {'ABC': 0, 'DEF' : 900.32}
    """ ------------ Add the assertion below ------------ """
    self.assertEqual(getRatio(prices['ABC'], prices['DEF']), 0)

  def test_getRatio_stockAPriceLarger(self):
    prices = {'ABC' : 100, 'DEF':50}
    self.assertEqual(getRatio(prices['ABC'], prices['DEF']), prices['ABC']/prices['DEF'])




if __name__ == '__main__':
    unittest.main()
