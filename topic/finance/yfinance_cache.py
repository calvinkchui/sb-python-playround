'''
https://pypi.org/project/yfinance-cache/


* Path
  * Window=C:/Users/<USER>/AppData/Local/py-yfinance-cache
  * Linux=/home/<USER>/.cache/py-yfinance-cache
  

'''
import yfinance_cache as yfc

msft = yfc.Ticker("DIS")

# get stock info
print(msft.info)

# get historical market data
hist = msft.history(period="1d")

hist = msft.history(period="5d")

# etc. See yfinance documentation for full API


'''
{
   "address1":"8 Canada Square",
   "city":"London",
   "zip":"E14 5HQ",
   "country":"United Kingdom",
   "phone":"44 20 7991 8888",
   "fax":"44 20 7992 4880",
   "website":"https://www.hsbc.com",
   "industry":"Banks - Diversified",
   "industryKey":"banks-diversified",
   "industryDisp":"Banks - Diversified",
   "sector":"Financial Services",
   "sectorKey":"financial-services",
   "sectorDisp":"Financial Services",
   "longBusinessSummary":"HSBC Holdings plc provides banking and financial services worldwide. The company operates through Wealth and Personal Banking, Commercial Banking, and Global Banking and Markets segments. The Wealth and Personal Banking segment offers retail banking and wealth products, including current and savings accounts, mortgages and personal loans, credit and debit cards, and local and international payment services; and wealth management services comprising insurance and investment products, global asset management services, investment management, and private wealth solutions. This segment serves personal banking and high net worth individuals. The Commercial Banking segment provides credit and lending, treasury management, payment, cash management, commercial insurance, and investment services; commercial cards; international trade and receivables finance services; foreign exchange products; capital raising services on debt and equity markets; and advisory services. It serves small and medium sized enterprises, mid-market enterprises, and corporates. The Global Banking and Markets segment offers financing, advisory, and transaction services; and credit, rates, foreign exchange, equities, money markets, and securities services; and engages in principal investment activities. It serves government, corporate and institutional clients, and private investors. HSBC Holdings plc was founded in 1865 and is headquartered in London, the United Kingdom.",
   "fullTimeEmployees":213978,
   "companyOfficers":[
      {
         "maxAge":1,
         "name":"Mr. Georges Bahjat  Elhedery",
         "age":49,
         "title":"CEO, Member of the Group Management Board & Executive Director",
         "yearBorn":1974,
         "fiscalYear":2023,
         "totalPay":34046493,
         "exercisedValue":0,
         "unexercisedValue":0
      },
      {
         "maxAge":1,
         "name":"Mr. Noel Paul Quinn",
         "age":61,
         "title":"Executive Officer",
         "yearBorn":1962,
         "fiscalYear":2023,
         "totalPay":56354599,
         "exercisedValue":0,
         "unexercisedValue":0
      },
      {
         "maxAge":1,
         "name":"Mr. Jonathan  Bingham",
         "title":"Interim CFO & Global Financial Controller",
         "fiscalYear":2023,
         "exercisedValue":0,
         "unexercisedValue":0
      },
      {
         "maxAge":1,
         "name":"Ms. Manveen Pam Kaur",
         "age":59,
         "title":"Group Chief Risk & Compliance Officer and Member of the Group Management Board",
         "yearBorn":1964,
         "fiscalYear":2023,
         "exercisedValue":0,
         "unexercisedValue":0
      },
      {
         "maxAge":1,
         "name":"Mr. Stephen Colin Moss",
         "age":56,
         "title":"CEO of Middle East North Africa & Turkey (MENAT) Region and Member of Group Management Board",
         "yearBorn":1967,
         "fiscalYear":2023,
         "exercisedValue":0,
         "unexercisedValue":0
      },
      {
         "maxAge":1,
         "name":"Mr. Colin William  Bell",
         "age":55,
         "title":"CEO of HSBC Bank plc & HSBC Europe and Member of the Group Management Board",
         "yearBorn":1968,
         "fiscalYear":2023,
         "exercisedValue":0,
         "unexercisedValue":0
      },
      {
         "maxAge":1,
         "name":"Mr. John David Stuart",
         "age":60,
         "title":"CEO of HSBC UK Bank plc & Member of the Group Management Board",
         "yearBorn":1963,
         "fiscalYear":2023,
         "exercisedValue":0,
         "unexercisedValue":0
      },
      {
         "maxAge":1,
         "name":"Ms. Elaine  Arden",
         "age":54,
         "title":"Group Chief Human Resources Officer & Member of the Group Management Board",
         "yearBorn":1969,
         "fiscalYear":2023,
         "exercisedValue":0,
         "unexercisedValue":0
      },
      {
         "maxAge":1,
         "name":"Mr. Gregory L. Guyett",
         "age":59,
         "title":"Chief Executive of Global Banking & Markets and Member of the Group Management Board",
         "yearBorn":1964,
         "fiscalYear":2023,
         "exercisedValue":0,
         "unexercisedValue":0
      },
      {
         "maxAge":1,
         "name":"Mr. Barry  O'Byrne",
         "age":47,
         "title":"CEO of Global Commercial Banking & Member of the Group Management Board",
         "yearBorn":1976,
         "fiscalYear":2023,
         "exercisedValue":0,
         "unexercisedValue":0
      }
   ],
   "auditRisk":1,
   "boardRisk":2,
   "compensationRisk":4,
   "shareHolderRightsRisk":1,
   "overallRisk":1,
   "governanceEpochDate":1725148800,
   "compensationAsOfEpochDate":1703980800,
   "irWebsite":"http://www.hsbc.com/investor-relations",
   "maxAge":86400,
   "priceHint":3,
   "previousClose":67.05,
   "open":67.3,
   "dayLow":67.25,
   "dayHigh":67.75,
   "regularMarketPreviousClose":67.05,
   "regularMarketOpen":67.3,
   "regularMarketDayLow":67.25,
   "regularMarketDayHigh":67.75,
   "dividendRate":4.77,
   "dividendYield":0.071100004,
   "exDividendDate":1723680000,
   "payoutRatio":0.5255,
   "fiveYearAvgDividendYield":6.08,
   "beta":0.524,
   "trailingPE":7.4585633,
   "forwardPE":7.068063,
   "volume":16977154,
   "regularMarketVolume":16977154,
   "averageVolume":17889245,
   "averageVolume10days":14751071,
   "averageDailyVolume10Day":14751071,
   "bid":67.45,
   "ask":67.5,
   "marketCap":1238139011072,
   "fiftyTwoWeekLow":55.5,
   "fiftyTwoWeekHigh":70.7,
   "priceToSalesTrailing12Months":21.14489,
   "fiftyDayAverage":66.666,
   "twoHundredDayAverage":64.038,
   "trailingAnnualDividendRate":0.61,
   "trailingAnnualDividendYield":0.009097688,
   "currency":"HKD",
   "enterpriseValue":862604492800,
   "profitMargins":0.39513,
   "floatShares":18097942200,
   "sharesOutstanding":18342799360,
   "heldPercentInsiders":0.0033000002,
   "heldPercentInstitutions":0.45494998,
   "impliedSharesOutstanding":18528000000,
   "bookValue":8.973,
   "priceToBook":7.522568,
   "lastFiscalYearEnd":1703980800,
   "nextFiscalYearEnd":1735603200,
   "mostRecentQuarter":1719705600,
   "earningsQuarterlyGrowth":-0.035,
   "netIncomeToCommon":22051999744,
   "trailingEps":9.05,
   "forwardEps":9.55,
   "pegRatio":0.01,
   "lastSplitFactor":"1:3",
   "lastSplitDate":931305600,
   "enterpriseToRevenue":14.732,
   "52WeekChange":0.1570319,
   "SandP52WeekChange":0.22617042,
   "lastDividendValue":0.1,
   "lastDividendDate":1723680000,
   "exchange":"HKG",
   "quoteType":"EQUITY",
   "symbol":"0005.HK",
   "underlyingSymbol":"0005.HK",
   "shortName":"HSBC HOLDINGS",
   "longName":"HSBC Holdings plc",
   "firstTradeDateEpochUtc":946863000,
   "timeZoneFullName":"Asia/Hong_Kong",
   "timeZoneShortName":"HKT",
   "uuid":"4f1f803d-11f8-343d-9544-e9779162f4c0",
   "messageBoardId":"finmb_382645",
   "gmtOffSetMilliseconds":28800000,
   "currentPrice":67.5,
   "targetHighPrice":82.59,
   "targetLowPrice":61.59,
   "targetMeanPrice":74.01,
   "targetMedianPrice":74.63,
   "recommendationMean":2.0,
   "recommendationKey":"buy",
   "numberOfAnalystOpinions":9,
   "totalCash":1057877000192,
   "totalCashPerShare":57.713,
   "totalDebt":684333989888,
   "totalRevenue":58554998784,
   "revenuePerShare":3.088,
   "returnOnAssets":0.00803,
   "returnOnEquity":0.12642999,
   "operatingCashflow":-9333999616,
   "earningsGrowth":0.005,
   "revenueGrowth":0.134,
   "operatingMargins":0.56589,
   "financialCurrency":"USD",
   "trailingPegRatio":4.875,
   "FetchDate":"Timestamp(""2024-09-10 16:41:17.899570"")"
}
'''