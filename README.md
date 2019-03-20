As I was reading a lot of books on investingI'm really curious I found 
this awesome tutorial / playlist. His tutorials are really 
well explained so feel free to leave a subscrition on: 
https://www.youtube.com/user/sentdex

As this covers only the first part of the tutorials also special thanks
to Kyle Li for putting so much effort in Towards Data Science posts 
I'm now able to use to gain fantastic insights. 
His posts are also available on his blog kylelix7.github.io. 

Disclaimer: The Content is for informational purposes only, you should 
not construe any such information or other material as legal, tax, 
investment, financial, or other advice.

Python Version: 3.6
Packages: numpy, pandas, pandas_datareader, matplotlib, BeautifulSoup4,
scikit-learn / sklearn


PART 1 - Intro and Getting Stock Price Data

-> [Adjusted close] also takes [stock splits] into account so sometimes 
   companies make this move when their price per share is too expensive 
   they split your 1 1000$ shares in 2 500$ shares and the price drops 
   down from 1000 to 500

-> Yahoo has been immediately deprecated. They altered their API in late 
   2017 but it still works
-> Google finance has been immediately deprecated due to large breaks in 
   the API without the introduction of a stable replacement
   still it provides data until right now 
-> Set IDLE to be used as default interpreter on my raspberryPi


________As I was facing some troubles with following the tutorial I'm 
switching over to another one taken from here: https://bit.ly/2U1XJs4___


Part II - Calculating Technical Analysis Indicators with Pandas

-> In finance, technical analysis is an analysis methodology for 
   forecasting the direction of prices through study of past market data
   primarily *price* and *volume*

-> Technical analysts rely on a combination of technical indicators to 
   study a stock. Common techn. indicators are *SMA* (Simple moving 
   averages) and Bollinger Band. Here a list of all techn. indicators:
   https://bit.ly/2l5sWua

-> **Bollinger Bands** is used to define the prevailing high and low 
   prices in a market to characterize the trading band of a financial 
   instrument or commodity
   
-> Bollinger Bands are a [volatility] indicator (https://bit.ly/2qc3CVk)
   
-> Bollinger Bands bands are consists of Moving Average (MA) line, a 
   upper band and lower band. 

-> The upper and lower bands are simply MA adding and subtracting standa
   rd deviation. 

-> Standard deviation is a measurment of volatility, that's why BB are a
   volatility indicator. 
   
   Upper Band = (MA + Kσ)        | MA is typical 20 day moving average 
                                 | and K is 2
   Lower Band = (MA - Kσ)
