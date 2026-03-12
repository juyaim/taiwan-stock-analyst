import datetime
import yfinance as yf

# --- 台股分析師 - 全能數據庫 V4.6 (終極整合版) ---

def get_stock_price(sid):
    """自動偵測上市(.TW)或上櫃(.TWO)並呈現當下股價"""
    for suffix in [".TW", ".TWO"]:
        ticker_id = f"{sid}{suffix}"
        ticker = yf.Ticker(ticker_id)
        try:
            # 抓取即時行情
            info = ticker.fast_info
            if info.last_price > 0:
                price = info.last_price
                prev_close = info.previous_close
                change_pct = ((price - prev_close) / prev_close) * 100
                return price, change_pct
        except:
            continue
    return None, None

def start_integrated_analysis():
    # 讓使用者直接輸入代號
    STOCK_ID = input("👉 請輸入台股代號 (例如 2330): ").strip()
    
    # 取得當下查詢時間與股價
    now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    price, pct = get_stock_price(STOCK_ID)
    
    # 建立漲跌呈現
    if price:
        price_display = f"{price:.2f} ({'▲' if pct > 0 else '▼' if pct < 0 else '─'} {abs(pct):.2f}%)"
    else:
        price_display = "查無即時股價資料"

    print(f"\n" + "="*60)
    print(f"🚀 全能台股導航 V4.6 | 查詢時間：{now_time}")
    print(f"📈 【 監控目標：{STOCK_ID} 】 當下股價：{price_display}")
    print("="*60)

    # --- 第一部分：宏觀環境與政府指標 (市場的氣血) ---
    print(f"[ 1. 宏觀環境 - 國家體檢表 ]")
    print(f" ● 國發會景氣燈號：https://index.ndc.gov.tw")
    print(f" ● M平方全球總經 ：https://www.macromicro.me")
    print(f"   🚩 重點：藍燈代表經濟感冒(買點)，紅燈代表發燒(風險)。")

    # --- 第二部分：市場情緒與大戶底牌 (多空博弈) ---
    print(f"\n[ 2. 市場情緒 - 大戶底牌 ]")
    print(f" ● 期交所大戶未平倉：https://www.taifex.com.tw")
    print(f" ● 證交所借券空單  ：https://www.twse.com.tw/zh/page/trading/exchange/TWTASU.html")
    print(f"   🚩 重點：觀察大戶是否偷買跌。空單過多時，市場壓力較大。")

    # --- 第三部分：個股深度分析 (精準穴位) ---
    print(f"\n[ 3. 個股深度分析 - 精準穴位 ]")
    print(f" ● 1. 技術分析     ：https://www.wantgoo.com{STOCK_ID}")
    print(f" ● 2. 籌碼/法人進出：https://goodinfo.tw/tw/StockDirectorSharehold.asp?STOCK_ID={STOCK_ID}")
    print(f" ● 3. 主力動向趨勢 ：https://www.wantgoo.com{STOCK_ID}/major-investors/main-trend")
    print(f" ● 4. 關鍵分點排行 ：https://www.wantgoo.com{STOCK_ID}/major-investors/main-broker")
    print(f" ● 5. 基本面財報狗 ：https://statementdog.com/analysis/{STOCK_ID}")
    print(f" ● 6. 市場討論同學會：https://www.cmoney.tw/forum/stock/{STOCK_ID}")
    print(f"   🚩 重點：追蹤主力集中度、法人是否連買，並找出帶頭拉抬的分點券商。")

    # --- 第四部分：營收獲利 (績效成績單) ---
    print(f"\n[ 4. 營收獲利 - 績效成績單 ]")
    print(f" ● 公開資訊觀測站 ：https://mops.twse.com.tw")
    print(f"   🚩 重點：每月 10 號前觀察營收成長率 (YoY/MoM)。")
    
    print("="*60)
    print(f"💡 提示：點擊「主力動向」確認大戶是否持續吃貨。")
    print("="*60)

if __name__ == "__main__":
    start_integrated_analysis()
