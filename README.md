# Predicting-the-Stock-Market-DataQuest

In this project, I worked with data from the [S&P500 Index](https://en.wikipedia.org/wiki/S%26P_500_Index). The S&P500 is a stock market index.

Some companies are publicly traded, which means that anyone can buy and sell their shares on the open market. A share entitles the owner to some control over the direction of the company and to a percentage (or share) of the earnings of the company. When you buy or sell shares, it's common known as trading a stock.

The price of a share is based on supply and demand for a given stock. For example, Apple stock has a price of 120 dollars per share as of December 2015 -- http://www.nasdaq.com/symbol/aapl. A stock that is in less demand, like Ford Motor Company, has a lower price -- http://finance.yahoo.com/q?s=F. Stock price is also influenced by other factors, including the number of shares a company has issued.

Stocks are traded daily and the price can rise or fall from the beginning of a trading day to the end based on demand. Stocks that are in more in demand, such as Apple, are traded more often than stocks of smaller companies.

Indexes aggregate the prices of multiple stocks together, and allow you to see how the market as a whole performs. For example, the [Dow Jones Industrial Average](https://en.wikipedia.org/wiki/Dow_Jones_Industrial_Average) aggregates the stock prices of 30 large American companies together. The S&P500 Index aggregates the stock prices of 500 large companies. When an index fund goes up or down, you can say that the primary market or sector it represents is doing the same. For example, if the Dow Jones Industrial Average price goes down one day, you can say that American stocks overall went down (ie, most American stocks went down in price).

Historical data on the price of the S&P500 Index was used to make predictions about future prices. Predicting whether an index goes up or down helps forecast how the stock market as a whole performs. Since stocks tend to correlate with how well the economy as a whole is performs, it can also help with economic forecasts.

There are thousands of traders who make money by buying and selling [Exchange Traded Funds](https://en.wikipedia.org/wiki/Exchange-traded_fund). ETFs allow you to buy and sell indexes like stocks. This means that you could "buy" the S&P500 Index ETF when the price is low and sell when it's high to make a profit. Creating a predictive model could allow traders to make money on the stock market.

The columns of the dataset are:

- `Date` -- The date of the record.
- `Open` -- The opening price of the day (when trading starts).
- `High` -- The highest trade price during the day.
- `Low` -- The lowest trade price during the day.
- `Close` -- The closing price for the day (when trading is finished).
- `Volume` -- The number of shares traded.
- `Adj Close` -- The daily closing price, adjusted retroactively to include any corporate actions. Read more [here](http://www.investopedia.com/terms/a/adjusted_closing_price.asp).
