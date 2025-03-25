import datetime

questions_and_answers = [
    # Stock and share market-related questions
     {"question": "What is the stock market?", "answer": "The stock market is a marketplace where securities, such as stocks, bonds, and other financial instruments, are bought and sold."},
    {"question": "Why do stocks go up and down?", "answer": "Stocks go up and down based on supply and demand, company performance, market conditions, investor sentiment, and external factors like the economy and political events."},
    {"question": "What is the role of the stock market?", "answer": "The stock market allows companies to raise capital by issuing shares, while providing investors with an opportunity to buy and sell those shares, aiming for profits."},
    {"question": "What is a stock exchange?", "answer": "A stock exchange is a marketplace where securities are traded, such as the New York Stock Exchange (NYSE) or the National Stock Exchange (NSE)."},
    {"question": "What is a stockbroker?", "answer": "A stockbroker is a professional or firm that buys and sells stocks on behalf of clients, and provides investment advice."},
    {"question": "What is market capitalization?", "answer": "Market capitalization is the total value of a company's outstanding shares, calculated by multiplying the stock price by the number of shares outstanding."},
    {"question": "What is an index?", "answer": "An index is a statistical measure of the changes in a portfolio of stocks, representing a portion of the market. Examples include the S&P 500 or the Dow Jones Industrial Average."},
    {"question": "What are blue-chip stocks?", "answer": "Blue-chip stocks are shares of well-established, financially stable companies with a long history of reliable performance, often paying regular dividends."},
    {"question": "What is a stock dividend?", "answer": "A stock dividend is a payment made by a corporation to its shareholders, typically in the form of cash or additional shares, as a portion of its profits."},
    {"question": "What is a bull market?", "answer": "A bull market refers to a period in which stock prices are rising or are expected to rise. It is often associated with optimism and investor confidence."},
    {"question": "What is a bear market?", "answer": "A bear market refers to a period in which stock prices are falling or are expected to fall. It is often characterized by pessimism and fear among investors."},
    {"question": "What is the difference between a stock and a bond?", "answer": "Stocks represent ownership in a company, while bonds are debt instruments where investors lend money to a company or government in exchange for periodic interest payments."},
    {"question": "How do I buy stocks?", "answer": "You can buy stocks through a stockbroker, either directly or via an online trading platform, by placing buy orders for specific stocks."},
    {"question": "What is a stock split?", "answer": "A stock split occurs when a company issues additional shares to its current shareholders, reducing the price per share but not affecting the total value of the investment."},
    {"question": "What is IPO?", "answer": "An IPO (Initial Public Offering) is when a company offers its shares to the public for the first time, allowing it to raise capital from investors."},
    {"question": "What are stock market indices?", "answer": "Stock market indices are groups of stocks that represent a specific sector or the entire market, such as the S&P 500, NASDAQ, or Dow Jones Industrial Average."},
    {"question": "What is the difference between growth and value stocks?", "answer": "Growth stocks are expected to grow at an above-average rate, often reinvesting profits, while value stocks are considered undervalued based on financial metrics and offer potential for price appreciation."},
    {"question": "What is short selling?", "answer": "Short selling involves borrowing shares of a stock from a broker and selling them, with the intention of buying them back at a lower price to return them and make a profit."},
    {"question": "What is a market order?", "answer": "A market order is an order to buy or sell a stock at the best available price in the market immediately."},
    {"question": "What is a limit order?", "answer": "A limit order is an order to buy or sell a stock at a specific price or better. It will only be executed if the stock reaches the specified price."},
    {"question": "What is the difference between primary and secondary markets?", "answer": "The primary market is where securities are issued and sold for the first time, while the secondary market is where previously issued securities are bought and sold among investors."},
    {"question": "What are the risks of investing in the stock market?", "answer": "Risks include market volatility, economic downturns, individual company performance, geopolitical events, and currency fluctuations."},
    {"question": "How can I manage risk in the stock market?", "answer": "Risk can be managed through diversification (investing in different assets), setting stop-loss orders, investing for the long term, and doing thorough research."},
    {"question": "What is an earnings report?", "answer": "An earnings report is a quarterly report that a publicly traded company releases to provide details on its financial performance, including revenue, profits, and losses."},
    {"question": "What is liquidity in the stock market?", "answer": "Liquidity refers to how easily an asset can be bought or sold in the market without affecting its price. Stocks with high trading volumes are typically more liquid."},
    {"question": "What is insider trading?", "answer": "Insider trading refers to the illegal practice of trading stocks based on non-public, material information about the company."},
    {"question": "What is technical analysis?", "answer": "Technical analysis involves analyzing historical price and volume data of stocks to forecast future price movements using charts and indicators."},
    {"question": "What is fundamental analysis?", "answer": "Fundamental analysis involves evaluating a company's financial health, management, and growth potential by examining financial statements and economic factors."},
    {"question": "What is a candlestick chart?", "answer": "A candlestick chart is a type of financial chart that displays the open, high, low, and close prices of a security for a specific time period."},
    {"question": "What is a stockbroker?", "answer": "A stockbroker is a professional who buys and sells stocks on behalf of clients, and may also provide investment advice."},
    {"question": "What is a margin account?", "answer": "A margin account is a type of account that allows investors to borrow money from a broker to purchase securities, using their existing investments as collateral."},
    {"question": "What is a dividend yield?", "answer": "The dividend yield is a ratio that shows how much income a stock generates in the form of dividends, expressed as a percentage of the stock's price."},
    {"question": "What is volatility?", "answer": "Volatility refers to the extent of price fluctuations of a stock or the overall market, and it is often used as a measure of risk."},
    {"question": "What is the P/E ratio?", "answer": "The P/E (Price-to-Earnings) ratio is a valuation ratio calculated by dividing the market price per share by the earnings per share, used to assess if a stock is over or under-valued."},
    {"question": "What is a stock index?", "answer": "A stock index is a statistical measure that represents the overall performance of a group of stocks in a particular market or sector."},
    {"question": "hii", "answer": "Hello! How can I assist you today?"},
    {"question": "hello", "answer": "Hi there! What can I do for you?"},
    {"question": "how are you", "answer": "I'm just a bot, but I'm here to help! How about you?"},
    {"question": "what's the time now", "answer": lambda: f"The current time is {datetime.datetime.now().strftime('%H:%M:%S')}."},
    {"question": "what is the date today", "answer": lambda: f"Today's date is {datetime.datetime.now().strftime('%Y-%m-%d')}."},
    {"question": "who are you", "answer": "I'm your chatbot assistant, here to answer your questions and help with information!"},
    {"question": "what can you do", "answer": "I can answer questions about blockchain, cryptocurrency, and general daily queries. Try asking me something!"},
    {"question": "good morning", "answer": "Good morning! I hope you have a fantastic day ahead!"},
    {"question": "good afternoon", "answer": "Good afternoon! How can I assist you today?"},
    {"question": "good evening", "answer": "Good evening! What would you like to know?"},
    {"question": "thank you", "answer": "You're welcome! Let me know if there's anything else you need."},
    {"question": "bye", "answer": "Goodbye! Have a great day!"},
    {"question": "What is the stock market?", "answer": "The stock market is a marketplace where shares of publicly traded companies are bought and sold."},
    {"question": "How does the stock market work?", "answer": "The stock market works through a network of exchanges where buyers and sellers trade shares based on supply and demand."},
    {"question": "What is a stock?", "answer": "A stock represents ownership in a company and a claim on a portion of its profits."},
    {"question": "What is a stock exchange?", "answer": "A stock exchange is a regulated marketplace for buying and selling stocks, such as the NYSE or NASDAQ."},
    {"question": "What is a stock symbol?", "answer": "A stock symbol is a unique series of letters assigned to a publicly traded company, like AAPL for Apple Inc."},
    {"question": "What is an IPO?", "answer": "IPO stands for Initial Public Offering, which is when a private company offers shares to the public for the first time."},
    {"question": "What are dividends?", "answer": "Dividends are payments made by a company to its shareholders from its profits."},
    {"question": "What is market capitalization?", "answer": "Market capitalization is the total market value of a company's outstanding shares."},
    {"question": "What is a bull market?", "answer": "A bull market is when stock prices are rising, indicating investor confidence."},
    {"question": "What is a bear market?", "answer": "A bear market is when stock prices are falling, indicating investor pessimism."},
    {"question": "What are mutual funds?", "answer": "Mutual funds are investment vehicles that pool money from multiple investors to invest in stocks, bonds, or other assets."},
    {"question": "What is a stock index?", "answer": "A stock index is a measurement of the performance of a group of stocks, such as the S&P 500 or Dow Jones."},
    {"question": "What is day trading?", "answer": "Day trading involves buying and selling stocks within the same trading day to capitalize on short-term price movements."},
    {"question": "What is a blue-chip stock?", "answer": "A blue-chip stock is a large, well-established, and financially stable company."},
    {"question": "What is the P/E ratio?", "answer": "The Price-to-Earnings (P/E) ratio measures a company's current share price relative to its per-share earnings."},
    {"question": "hi", "answer": "Hello! How can I assist you with the stock market today?"},
    {"question": "hello", "answer": "Hi there! What stock-related question do you have?"},
    {"question": "how are you", "answer": "I'm just a bot, but I'm here to help! How about you?"},
    {"question": "what's the time now", "answer": lambda: f"The current time is {datetime.datetime.now().strftime('%H:%M:%S')}."},
    {"question": "what is the date today", "answer": lambda: f"Today's date is {datetime.datetime.now().strftime('%Y-%m-%d')}."},
    {"question": "thank you", "answer": "You're welcome! Let me know if you have more stock-related queries."},
    {"question": "bye", "answer": "Goodbye! Have a great day and good luck with your investments!"},
    {"question": "What is the stock market?", "answer": "The stock market is a place where buyers and sellers trade stocks, which are shares of ownership in companies."},
    {"question": "What is a share?", "answer": "A share represents a unit of ownership in a company. Owning shares means having a stake in the company."},
    {"question": "What is an ETF?", "answer": "An ETF (Exchange-Traded Fund) is a type of investment fund and exchange-traded product, which holds assets like stocks, commodities, or bonds."},
    {"question": "What is a Mutual Fund?", "answer": "A mutual fund is an investment vehicle that pools money from many investors to purchase securities like stocks, bonds, or other assets."},
    {"question": "What is an SIP?", "answer": "SIP (Systematic Investment Plan) is a method of investing a fixed sum in mutual funds at regular intervals."},
    {"question": "What is MTF?", "answer": "MTF (Margin Trading Facility) allows traders to borrow funds to trade stocks by using their existing holdings as collateral."},
    {"question": "What is RSI?", "answer": "RSI (Relative Strength Index) is a momentum oscillator used to measure the speed and change of price movements in stock trading, ranging from 0 to 100."},
    {"question": "What is Volatility?", "answer": "Volatility refers to the degree of variation in a stock's price over time, often used to assess risk."},
    {"question": "What is Stop Loss?", "answer": "A stop loss is an order placed with a broker to buy or sell once the stock reaches a certain price, limiting potential losses."},
    {"question": "What is Target Price?", "answer": "A target price is the predicted price level of a stock, as forecasted by analysts, which investors aim for when buying or selling."},
    {"question": "What is the current price of a stock?", "answer": "The current price of a stock is the most recent price at which the stock has been traded."},
    {"question": "What are stock options?", "answer": "Stock options are financial instruments that give an investor the right, but not the obligation, to buy or sell a stock at a specific price before a certain date."},
    {"question": "What is a Dividend?", "answer": "A dividend is a portion of a company's earnings distributed to its shareholders, usually in cash or additional shares."},
    {"question": "What is a Market Order?", "answer": "A market order is an order to buy or sell a stock immediately at the current market price."},
    {"question": "What is a Limit Order?", "answer": "A limit order is an order to buy or sell a stock at a specific price or better, and it will only be executed when the stock reaches that price."},
    {"question": "What is a Bear Market?", "answer": "A bear market is a market in which stock prices are falling or are expected to fall."},
    {"question": "What is a Bull Market?", "answer": "A bull market is a market in which stock prices are rising or are expected to rise."},
    {"question": "What is the P/E Ratio?", "answer": "The P/E (Price-to-Earnings) ratio is a valuation ratio, calculated by dividing the market price per share by the earnings per share (EPS) of a company."},
    {"question": "What is the Nifty?", "answer": "The Nifty is an index representing the weighted average of 50 of the largest publicly listed companies in India."},
    {"question": "What is the Sensex?", "answer": "The Sensex is a stock market index consisting of 30 of the largest and most actively traded companies listed on the Bombay Stock Exchange (BSE)."},
    {"question": "What is an IPO?", "answer": "An IPO (Initial Public Offering) is the process through which a private company offers its shares to the public for the first time."},
    {"question": "What is a Bearish Trend?", "answer": "A bearish trend refers to a market condition where prices are consistently falling."},
    {"question": "What is a Bullish Trend?", "answer": "A bullish trend refers to a market condition where prices are consistently rising."},
    {"question": "What is a Stop Loss Order?", "answer": "A stop loss order is a tool used by investors to limit potential losses by automatically selling a stock when it reaches a certain price."},
    {"question": "What are Penny Stocks?", "answer": "Penny stocks are shares of small companies that trade at very low prices, often below $5 per share."},
    {"question": "What is a Margin Account?", "answer": "A margin account allows investors to borrow funds from a broker to purchase securities, using the securities as collateral."},
    {"question": "What is Technical Analysis?", "answer": "Technical analysis is the study of past market data, primarily price and volume, to forecast future price movements."},
    {"question": "What is Fundamental Analysis?", "answer": "Fundamental analysis involves evaluating a company's financial health and performance through metrics like earnings, revenue, and growth potential."},
    {"question": "What is a Stock Split?", "answer": "A stock split occurs when a company issues additional shares to shareholders, increasing the number of shares outstanding while reducing the stock price."},
    {"question": "What is a Dividend Yield?", "answer": "Dividend yield is a financial ratio that shows how much income a stock generates in the form of dividends, expressed as a percentage of the stock's price."},
    {"question": "What is a Blue-Chip Stock?", "answer": "A blue-chip stock is a share in a large, well-established, and financially stable company with a long track record of reliability."},
    {"question": "What is Arbitrage?", "answer": "Arbitrage refers to the practice of taking advantage of price differences in different markets by buying a stock in one market and simultaneously selling it in another."},
    {"question": "What is a Risk-Free Rate?", "answer": "The risk-free rate is the return on an investment that is considered free of risk, typically associated with government bonds."},
    {"question": "What is an Exchange?", "answer": "An exchange is a marketplace where stocks, commodities, and other financial instruments are traded, such as the NYSE or NASDAQ."},
    {"question": "What is a Trading Volume?", "answer": "Trading volume is the total number of shares or contracts traded in a specific security or market during a given period."},
    {"question": "What is a Call Option?", "answer": "A call option gives the holder the right, but not the obligation, to buy a stock at a specific price before a certain date."},
    {"question": "What is a Put Option?", "answer": "A put option gives the holder the right, but not the obligation, to sell a stock at a specific price before a certain date."},
    {"question": "What is a Short Sell?", "answer": "Short selling is the practice of selling a stock that the seller does not own, betting that the price will decline so they can buy it back at a lower price."},
    {"question": "What is Liquidity?", "answer": "Liquidity refers to how quickly and easily an asset can be bought or sold without affecting its price."},
    {"question": "What is a Capital Gain?", "answer": "A capital gain is the profit made from the sale of an asset, such as stocks, where the sale price is higher than the purchase price."},
    {"question": "What is the Beta of a Stock?", "answer": "Beta is a measure of a stock's volatility in relation to the overall market. A beta greater than 1 indicates higher volatility than the market."},
    {"question": "What is a Hedging Strategy?", "answer": "Hedging involves taking an offsetting position in an asset or security to reduce the risk of adverse price movements."},
    {"question": "What is the Difference Between Stocks and Bonds?", "answer": "Stocks represent ownership in a company, while bonds represent debt that a company or government must repay with interest."}

]
