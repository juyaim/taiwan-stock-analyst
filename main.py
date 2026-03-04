# 台股分析師 - 全能數據庫 V4.0
# 小提示：只需修改下方的 "2330" 即可更換個股追蹤目標
STOCK_ID = "2330" 

# --- 第一部分：宏觀環境與政府指標 (市場的氣血) ---
MACRO_INDICATORS = {
    "國發會_景氣燈號": "https://index.ndc.gov.tw/n/zh_tw",
    "M平方_全球總經(CPI/非農)": "https://www.macromicro.me/trader-insights",
    "重點": "看國家體檢表。藍燈代表經濟感冒(買點)，紅燈代表發燒(風險)。"
}

# --- 第二部分：市場情緒與大戶底牌 (多空博弈) ---
MARKET_SENTIMENT = {
    "期交所_大戶未平倉": "https://www.taifex.com.tw/cht/index",
    "證交所_借券空單": "https://www.twse.com.tw/zh/page/trading/exchange/TWTASU.html",
    "重點": "觀察大戶是否偷偷買跌(空單)。空單過多時，市場壓力較大。"
}

# --- 第三部分：個股深度分析 (精準穴位) ---
STOCK_ANALYSIS = {
    "1. 技術分析": f"https://www.wantgoo.com/stock/astock/techchart?stockno={STOCK_ID}",
    "2. 籌碼追蹤(Goodinfo)": f"https://goodinfo.tw/tw/StockDirectorSharehold.asp?STOCK_ID={STOCK_ID}",
    "3. 主力足跡(NLOG)": f"f'https://nlog.cc/s/{STOCK_ID}/籌碼分析'",
    "4. 基本面(財報狗)": f"https://statementdog.com/analysis/{STOCK_ID}",
    "5. 市場討論(Cmoney)": f"https://www.cmoney.tw/forum/stock/{STOCK_ID}",
    "重點": "追蹤法人買賣超、毛利率趨勢與群眾情緒。"
}

# --- 第四部分：營收獲利 (績效成績單) ---
EARNINGS_REPORT = {
    "公開資訊觀測站": "https://mops.twse.com.tw/mops/web/t05st10_ifrs",
    "重點": "每月 10 號前觀察營收成長率 (YoY/MoM)。"
}

def start_integrated_analysis():
    print(f"--- 全能台股導航 V4.0 啟動 ---")
    print(f"當前監控目標：{STOCK_ID}。系統已整合政府指標、大戶籌碼與個股基本面。")

if __name__ == "__main__":
    start_integrated_analysis()
