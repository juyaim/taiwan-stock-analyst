# 台股分析師 - 深度數據庫 V1.0
TW_STOCK_RESOURCES = {
    "1. 技術與大盤 (Technical)": {
        "玩股網_即時圖表": "https://www.wantgoo.com/stock/astock/techchart?stockno=0050",
        "TradingView_台股": "https://tw.tradingview.com/symbols/TWSE-TAIEX/",
        "重點": "觀察多空排列、趨勢線與大盤走勢"
    },
    "2. 籌碼面追蹤 (Chips)": {
        "Goodinfo_法人持股": "https://goodinfo.tw/tw/StockDirectorSharehold.asp?STOCK_ID=2330",
        "NLOG_主力足跡": "https://nlog.cc/s/2330/籌碼分析",
        "重點": "追蹤三大法人買賣超、大戶持股比例變化"
    },
    "3. 基本面與財務 (Fundamental)": {
        "財報狗_獲利分析": "https://statementdog.com/analysis/2330",
        "股市爆料同學會": "https://www.cmoney.tw/forum/stock/2330",
        "重點": "看毛利率、ROE 趨勢以及市場討論熱度"
    },
    "4. 營收與獲利 (Earnings)": {
        "公開資訊觀測站": "https://mops.twse.com.tw/mops/web/t05st10_ifrs",
        "重點": "每月 10 號前的營收公告 (YoY/MoM 成長)"
    }
}

def init_analyst():
    print("--- 台股分析模組已就緒 ---")
    print("已整合技術、籌碼、基本面與營收四大核心維度。")

if __name__ == "__main__":
    init_analyst()
