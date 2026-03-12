import datetime
import yfinance as yf

# --- 核心數據抓取：確保 2026 年報價必出與精準台股識別 ---
def get_stock_data(sid):
    clean_id = "".join(filter(str.isdigit, sid))
    # 優先嘗試 .TW (上市) 與 .TWO (上櫃)，解決 3131 等代號重複問題
    for suffix in [".TW", ".TWO"]:
        ticker_id = f"{clean_id}{suffix}"
        ticker = yf.Ticker(ticker_id)
        try:
            # 使用 download 抓取最近兩日數據，確保 2026 年報價不延遲
            df = yf.download(ticker_id, period="2d", progress=False)
            if df.empty: continue
            
            # 取得最新成交價與漲跌數據
            current_price = float(df['Close'].iloc[-1])
            prev_close = float(df['Close'].iloc[-2]) if len(df) > 1 else current_price
            
            # 獲取 EPS 與 名稱
            info = ticker.info
            eps = info.get('trailingEps') or info.get('forwardEps')
            name = info.get('shortName', '台股個股')

            return {
                "price": current_price,
                "prev_close": prev_close,
                "eps": eps,
                "tid": ticker_id,
                "name": name
            }
        except:
            continue
    return None

def start_integrated_analysis():
    print(f"{'='*60}")
    print(f"🚀 全能台股導航 V4.17 | 2026 實時數據引擎啟動")
    print(f"{'='*60}")
    
    # 步驟 1：輸入代號並立即顯示股價 (解決 3037, 2454 報價問題)
    STOCK_ID = input("👉 請輸入台股代號 (例如 2454 或 3037): ").strip()
    now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    data = get_stock_data(STOCK_ID)
    
    if not data:
        print(f"❌ 錯誤：無法連線至數據庫，請確認網路或代號是否正確。")
        return

    # 計算漲跌幅
    pct = ((data['price'] - data['prev_close']) / data['prev_close']) * 100
    status = f"{data['price']:.2f} ({'▲' if pct > 0 else '▼' if pct < 0 else '─'} {abs(pct):.2f}%)"
    market = "[上市]" if ".TW" in data['tid'] and ".TWO" not in data['tid'] else "[上櫃]"
    
    print(f"\n" + "="*60)
    print(f"📈 【 監控目標：{STOCK_ID} {data['name']} {market} 】")
    print(f"💰 今日當下股價：{status}")
    print(f"⏰ 查詢時間：{now_time}")
    print("="*60)

    # --- 第一部分：宏觀環境 (市場氣血) ---
    print(f"📊 [ 第一部分：宏觀環境 ]")
    print(f"  ● 國發會_景氣燈號：https://index.ndc.gov.tw")
    print(f"  ● M平方_全球總經  ：https://www.macromicro.me")
    print(f"  🚩 重點：藍燈代表經濟感冒(買點)，紅燈代表發燒(風險)。")

    # --- 第二部分：市場情緒 (多空博弈) ---
    print(f"\n🕵️ [ 第二部分：市場情緒 ]")
    print(f"  ● 恐懼與貪婪指數  ：https://www.wantgoo.com")
    print(f"  ● 期交所_大戶未平倉：https://www.taifex.com.tw")
    print(f"  ● 證交所_借券空單  ：https://www.twse.com.tw")
    print(f"  🚩 重點：指數 < 25 (極度恐懼) 常是反向買點；觀察空單是否過高增加壓力。")

    # --- 第三部分：個股深度分析 (精準穴位) ---
    print(f"\n🔍 [ 第三部分：個股深度分析 ]")
    print(f"  ● 1. 技術分析     ：https://www.wantgoo.com{STOCK_ID}")
    print(f"  ● 2. 籌碼/持股比例：https://goodinfo.tw{STOCK_ID}")
    print(f"  ● 3. 三大法人進出 ：https://goodinfo.tw{STOCK_ID}")
    print(f"  ● 4. 主力集中度趨勢：https://www.wantgoo.com{STOCK_ID}/major-investors/main-trend")
    print(f"  ● 5. 分點買賣排行 ：https://www.wantgoo.com{STOCK_ID}/major-investors/main-broker")
    print(f"  ● 6. 基本面(財報狗)：https://statementdog.com{STOCK_ID}")
    print(f"  ● 7. 市場討論(Cmoney)：https://www.cmoney.tw{STOCK_ID}")
    print(f"  🚩 重點：追蹤主力集中度、法人是否連買，並找關鍵分點。")

    # --- 第四部分：營收獲利 (績效成績單) ---
    print(f"\n📈 [ 第四部分：營收獲利 ]")
    print(f"  ● 公開資訊觀測站 ：https://mops.twse.com.tw")
    print(f"  🚩 重點：每月 10 號前觀察營收成長率 (YoY/MoM)。")
    
    # --- 第五部分：DCF 估值評比 (壓軸模型) ---
    print(f"\n💎 [ 第五部分：DCF 估值評比 ] (依據近四季 EPS：{data['eps'] if data['eps'] else 'N/A'})")
    if data['eps'] and data['eps'] > 0:
        # 估值公式：EPS * (1+G) * 15(基準PE)
        scenarios = {"低評比(保守5%)": 0.05, "中評比(中性10%)": 0.10, "高評比(樂觀15%)": 0.15}
        for label, g in scenarios.items():
            fair_val = data['eps'] * (1 + g) * 15 
            diff = ((data['price'] - fair_val) / fair_val) * 100
            pos = "偏高" if diff > 0 else "便宜"
            print(f"  ● {label}: {fair_val:>8.2f} 元 (目前{pos} {abs(diff):.1f}%)")
    else:
        print(f"  ⚠️ 盈餘為負或數據不足，無法進行 DCF 估值運算。")

    print("-" * 60)
    print(f"💡 綜合提示：若股價低於「中評比」且「恐懼指數」極低，通常是極佳買點。")
    print("="*60)

if __name__ == "__main__":
    start_integrated_analysis()
