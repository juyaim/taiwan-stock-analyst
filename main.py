# 台股分析師 - 深度數據庫 V1.1
# 小提示：如果要換股票，只需將下方的 "2330" 改成其他代碼（如 "2317"）
STOCK_ID = "2330" 

TW_STOCK_RESOURCES = {
    "1. 技術分析 (Technical)": {
        "玩股網_即時圖表": f"https://www.wantgoo.com/stock/astock/techchart?stockno={STOCK_ID}",
        "TradingView_大盤": "https://tw.tradingview.com/symbols/TWSE-TAIEX/",
        "重點": "觀察多空排列、支撐壓力位與大盤走勢"
    },
    "2. 籌碼面追蹤 (Chips)": {
        "Goodinfo_法人持股": f"https://goodinfo.tw/tw/StockDirectorSharehold.asp?STOCK_ID={STOCK_ID}",
        "NLOG_主力足跡": f"https://nlog.cc/s/{STOCK_ID}/籌碼分析",
        "重點": "追蹤三大法人買賣超、大戶持股比例變化"
    },
    "3. 基本面與財務 (Fundamental)": {
        "財報狗_獲利分析": f"https://statementdog.com/analysis/{STOCK_ID}",
        "股市爆料同學會": f"https://www.cmoney.tw/forum/stock/{STOCK_ID}",
        "重點": "看毛利率、ROE 趨勢以及市場討論情緒"
    },
    "4. 營收獲利 (Earnings)": {
        "公開資訊觀測站": "https://mops.twse.com.tw/mops/web/t05st10_ifrs",
        "重點": "每月 10 號前觀察營收 YoY/MoM 成長率"
    }
}

def start_analysis():
    print(f"--- 台股分析模組已啟動：當前目標 {STOCK_ID} ---")
    print("已整合技術、籌碼、基本面與營收四大核心維度。")

if __name__ == "__main__":
    start_analysis()
