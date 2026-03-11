# 台股分析師 - 全能數據庫 V4.4 (整合個人雲端籌碼庫)
# 小提示：只需修改下方的 "2330" 即可更換個股追蹤目標
STOCK_ID = "2330" 

# 您的個人雲端籌碼庫網址 (這是您剛剛建立的 GitHub Pages)
MY_DASHBOARD = "https://juyaim.github.io/tw-institutional-stocker/"

# --- 第一部分：宏觀環境與政府指標 ---
MACRO_INDICATORS = {
    "國發會_景氣燈號": "https://index.ndc.gov.tw/n/zh_tw",
    "M平方_全球總經": "https://www.macromicro.me/trader-insights",
    "重點": "藍燈買進、紅燈減碼。"
}

# --- 第二部分：市場情緒與大戶底牌 ---
MARKET_SENTIMENT = {
    "期交所_大戶未平倉": "https://www.taifex.com.tw/cht/index",
    "證交所_借券空單": "https://www.twse.com.tw/zh/page/trading/exchange/TWTASU.html",
    "重點": "觀察大戶是否反向佈局。"
}

# --- 第三部分：個股深度分析 (新增個人數據庫) ---
STOCK_ANALYSIS = {
    "1. 個人雲端籌碼圖": f"{MY_DASHBOARD}", # <--- 整合您的專屬分點網頁
    "2. 技術分析(玩股)": f"https://www.wantgoo.com{STOCK_ID}",
    "3. 法人進出(Goodinfo)": f"https://goodinfo.tw/tw/StockDirectorSharehold.asp?STOCK_ID={STOCK_ID}",
    "4. 分點買賣排行": f"https://www.wantgoo.com{STOCK_ID}/major-investors/main-broker",
    "5. 基本面(財報狗)": f"https://statementdog.com/analysis/{STOCK_ID}",
    "重點": "先看【個人雲端圖】確認三大法人長期持股水位，再看【分點排行】找關鍵分點。"
}

# --- 第四部分：營收獲利 ---
EARNINGS_REPORT = {
    "公開資訊觀測站": "https://mops.twse.com.tw/mops/web/t05st10_ifrs",
    "重點": "每月 10 號前觀察 YoY/MoM。"
}

def start_integrated_analysis():
    print(f"🚀 --- 全能台股導航 V4.4 啟動 --- 🚀")
    print(f"【目前監控目標】：{STOCK_ID}")
    print("-" * 50)
    print(f"📈 1. 您的專屬籌碼走勢圖：{STOCK_ANALYSIS['1. 個人雲端籌碼圖']}")
    print(f"📊 2. 關鍵分點進出排行：{STOCK_ANALYSIS['4. 分點買賣排行']}")
    print(f"🏢 3. 法人長期持股比例：{STOCK_ANALYSIS['3. 法人進出(三大法人)']}")
    print("-" * 50)
    print("💡 操作密技：")
    print(f"   先點開您的 GitHub Pages，在搜尋框輸入 {STOCK_ID}，")
    print("   觀察外資與投信是否在『黃金交叉』或『同步買進』！")

if __name__ == "__main__":
    start_integrated_analysis()
