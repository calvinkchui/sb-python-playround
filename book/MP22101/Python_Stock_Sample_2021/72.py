# 載入必要模組
from haohaninfo import GOrder
from order import Record
import numpy as np
from talib.abstract import RSI
import sys

# 登入帳號密碼(讀者須修正該帳號密碼為自己的，否則無法執行策略)
# GOrder.Login('TestAccount','TestPasswd') # 如果開啟GOrder可以不需要該行
# 建立部位管理物件
OrderRecord=Record() 
# 取得商品名稱
ProdInfo=sys.argv[1]
# 取得回測參數、移動停損點數
StartDate=sys.argv[2]
EndDate=sys.argv[3]
RSIPeriod=int(sys.argv[4])
Ceil=float(sys.argv[5])
Floor=float(sys.argv[6])
MoveStopLoss=float(sys.argv[7])
# 回測取報價物件
KBar=GOrder.GetTAKBar(StartDate,EndDate,ProdInfo,'Stock','0','20')
KBar['RSI']=RSI(KBar,timeperiod=RSIPeriod)
KBar['Ceil']=np.array([Ceil]*len(KBar['time']))
KBar['Floor']=np.array([Floor]*len(KBar['time']))
# 開始回測
for n in range(0,len(KBar['time'])-1):
    # 先判斷long MA的上一筆值是否為空值 再接續判斷策略內容
    if not np.isnan( KBar['RSI'][n-1] ) :
        # 如果無未平倉部位
        if OrderRecord.GetOpenInterest()==0 :
            # RSI 向上突破超賣界線
            if KBar['RSI'][n-1] <= KBar['Floor'][n] and KBar['RSI'][n] > KBar['Floor'][n]:
                OrderRecord.Order('Buy', KBar['product'][n+1],KBar['time'][n+1],KBar['open'][n+1],1)
                OrderPrice = KBar['open'][n+1]
                StopLossPoint = OrderPrice * ( 1 - MoveStopLoss )
                continue
            # RSI 向下突破超買界線
            if KBar['RSI'][n-1] >= KBar['Ceil'][n] and KBar['RSI'][n] < KBar['Ceil'][n] :
                OrderRecord.Order('Sell', KBar['product'][n+1],KBar['time'][n+1],KBar['open'][n+1],1)
                OrderPrice = KBar['open'][n+1]
                StopLossPoint = OrderPrice * ( 1 + MoveStopLoss )
                continue
        # 如果有多單部位   
        elif OrderRecord.GetOpenInterest()==1 :
            # 逐筆更新移動停損價位
            if KBar['close'][n] * ( 1 - MoveStopLoss ) > StopLossPoint :
                StopLossPoint = KBar['close'][n] * ( 1 - MoveStopLoss )
            # 如果上一根K的收盤價觸及停損價位，則在最新時間出場
            elif KBar['close'][n] < StopLossPoint :
                OrderRecord.Cover('Sell', KBar['product'][n+1],KBar['time'][n+1],KBar['open'][n+1],1)
                continue
            # 若  RSI 大於 超買界線 則停利出場
            if KBar['RSI'][n] > KBar['Ceil'][n]:
                OrderRecord.Cover('Sell', KBar['product'][n+1],KBar['time'][n+1],KBar['open'][n+1],1)
                continue
        # 如果有空單部位
        elif OrderRecord.GetOpenInterest()==-1 :
            # 逐筆更新移動停損價位
            if KBar['close'][n] * ( 1 + MoveStopLoss ) < StopLossPoint :
                StopLossPoint = KBar['close'][n] * ( 1 + MoveStopLoss )
            # 如果上一根K的收盤價觸及停損價位，則在最新時間出場
            elif KBar['close'][n] > StopLossPoint :
                OrderRecord.Cover('Buy', KBar['product'][n+1],KBar['time'][n+1],KBar['open'][n+1],1)
                continue
            # 若  RSI 低於 超賣界線 則停利出場
            if KBar['RSI'][n] < KBar['Floor'][n]:
                OrderRecord.Cover('Buy', KBar['product'][n+1],KBar['time'][n+1],KBar['open'][n+1],1)
                continue

# 顯示交易績效
print('總績效',OrderRecord.GetTotalProfit())      
print('平均交易績效',OrderRecord.GetAverageProfit()) 
print('勝率',OrderRecord.GetWinRate()) 
print('最大連續虧損',OrderRecord.GetAccLoss()) 
print('最大資金回落(MDD)',OrderRecord.GetMDD()) 
print('平均獲利 ',OrderRecord.GetAverEarn()) 
print('平均虧損',OrderRecord.GetAverLoss()) 

# 繪製走勢圖加上MA以及下單點位
from chart import ChartOrder_RSI
ChartOrder_RSI(KBar,OrderRecord.GetTradeRecord())

