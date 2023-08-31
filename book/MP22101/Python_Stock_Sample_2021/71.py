# 載入必要模組
from haohaninfo import GOrder
from order import Record
import numpy as np
from talib.abstract import SMA,EMA
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
LongMAPeriod=int(sys.argv[4])
ShortMAPeriod=int(sys.argv[5])
MoveStopLoss=float(sys.argv[6])
# 回測取報價物件
KBar=GOrder.GetTAKBar(StartDate,EndDate,ProdInfo,'Stock','0','5')
KBar['MA_long']=SMA(KBar,timeperiod=LongMAPeriod)
KBar['MA_short']=EMA(KBar,timeperiod=ShortMAPeriod)
# 開始回測
for n in range(0,len(KBar['time'])-1):
    # 先判斷long MA的上一筆值是否為空值 再接續判斷策略內容
    if not np.isnan( KBar['MA_long'][n-1] ) :
        # 如果無未平倉部位 
        if OrderRecord.GetOpenInterest()==0 :
            # short MA 向上突破 long MA
            if KBar['MA_short'][n-1] <= KBar['MA_long'][n-1] and KBar['MA_short'][n] > KBar['MA_long'][n] :
                OrderRecord.Order('Buy', KBar['product'][n+1],KBar['time'][n+1],KBar['open'][n+1],1)
                OrderPrice = KBar['open'][n+1]
                StopLossPoint = OrderPrice * (1 - MoveStopLoss)
                continue
            # short MA 向下突破 long MA
            if KBar['MA_short'][n-1] >= KBar['MA_long'][n-1] and KBar['MA_short'][n] < KBar['MA_long'][n] :
                OrderRecord.Order('Sell', KBar['product'][n+1],KBar['time'][n+1],KBar['open'][n+1],1)
                OrderPrice = KBar['open'][n+1]
                StopLossPoint = OrderPrice * (1 + MoveStopLoss)
                continue
        # 如果有多單部位 
        elif OrderRecord.GetOpenInterest()==1 :
            # short MA 向下反轉突破 long MA
            if KBar['MA_short'][n-1] >= KBar['MA_long'][n-1] and KBar['MA_short'][n] < KBar['MA_long'][n] :
                OrderRecord.Cover('Sell', KBar['product'][n+1],KBar['time'][n+1],KBar['open'][n+1],1)
                OrderRecord.Order('Sell', KBar['product'][n+1],KBar['time'][n+1],KBar['open'][n+1],1)
                OrderPrice = KBar['open'][n+1]
                StopLossPoint = OrderPrice * (1 + MoveStopLoss)
                continue
            # 逐筆更新移動停損價位
            if KBar['close'][n] * (1 - MoveStopLoss) > StopLossPoint :
                StopLossPoint = KBar['close'][n] * (1 - MoveStopLoss)
            # 如果上一根K的收盤價觸及停損價位，則在最新時間出場
            elif KBar['close'][n] < StopLossPoint :
                OrderRecord.Cover('Sell', KBar['product'][n+1],KBar['time'][n+1],KBar['open'][n+1],1)
                continue
        # 如果有空單部位  
        elif OrderRecord.GetOpenInterest()==-1 :
            # short MA 向上反轉突破 long MA
            if KBar['MA_short'][n-1] <= KBar['MA_long'][n-1] and KBar['MA_short'][n] > KBar['MA_long'][n] :
                OrderRecord.Cover('Buy', KBar['product'][n+1],KBar['time'][n+1],KBar['open'][n+1],1)
                OrderRecord.Order('Buy', KBar['product'][n+1],KBar['time'][n+1],KBar['open'][n+1],1)
                OrderPrice = KBar['open'][n+1]
                StopLossPoint = OrderPrice * (1 - MoveStopLoss)
                continue
            # 逐筆更新移動停損價位
            if KBar['close'][n] * (1 + MoveStopLoss) < StopLossPoint :
                StopLossPoint = KBar['close'][n] * (1 + MoveStopLoss)
            # 如果上一根K的收盤價觸及停損價位，則在最新時間出場
            elif KBar['close'][n] > StopLossPoint :
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
from chart import ChartOrder_MA
ChartOrder_MA(KBar,OrderRecord.GetTradeRecord())
