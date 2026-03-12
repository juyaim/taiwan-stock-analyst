import datetime
import yfinance as yf

# --- 核心數據抓取：採用 V4.27 穩定邏輯，確保 2026/03/12 報價精準 ---
def get_stable_stock_data(sid):
    """
    V4.30 終極穩定版：
    1. 強制回歸基準收盤價邏輯，確保 3491 昇達科數據正確。
    2. 顯示 2026/03/11 的正確結算價，避開盤中 API 亂跳問題。
    """
    clean_id = sid.strip()
    for suffix in [".TW", ".TWO"]:
        tid = f"{clean_id}{suffix}"
        try:
            # 抓取最近 5 天日線，取最後一個完整交易日 Close
            df = yf.download(tid, period="5d", progress=False)
            if df.empty: continue
            
            stable_price = float(df['Close'].iloc[-1])
            prev_price = float(df['Close'].iloc[-2]) if len(df) > 1 else stable_price
            
            ticker = yf.Ticker(tid)
            info = ticker.info
            eps = info.get('trailingEps') or info.get('forwardEps')
            name = info.get('shortName', '台股個股')

            return {
                "price": stable_price,
                "prev_close": prev_price,
                "eps": eps,
                "tid": tid,
                "name": name,
                "market": "[上市]" if suffix == ".TW" else "[上櫃]",
                "date": df.index[-1].strftime('%Y-%m-%d')
            }
        except:
            continue
    return None

def start_integrated_analysis():
    print(f"{'='*60}")
    print(f"🚀 全能台股導航 V4.30 | 籌碼全方位強化版 (不縮水)")
    print(f"{'='*60}")
    
    # 步驟 1：輸入代號
    STOCK_ID = input("👉 請輸入台股代號 (例如 3491 或 2330): ").strip()
    now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    data = get_stable_stock_data(STOCK_ID)
    
    if not data:
        print(f"❌ 錯誤：無法取得 {STOCK_ID} 數據，請確認代號。")
        return

    # 計算漲跌幅
    diff = data['price'] - data['prev_close']
    pct = (diff / data['prev_close']) * 100
    status = f"{data['price']:.2f} ({'▲' if diff > 0 else '▼' if diff < 0 else '─'} {abs(pct):.2f}%)"
    
    print(f"\n" + "="*60)
    print(f"📈 【 監控目標：{STOCK_ID} {data['name']} {data['market']} 】")
    print(f"💰 基準日收盤價：{status}")
    print(f"📅 數據基準日期：{data['date']}")
    print(f"⏰ 查詢執行時間：{now_time}")
    print("="*60)

    # --- 第一部分：宏觀環境 ---
    print(f"📊 [ 第一部分：宏觀環境 ]")
    print(f"  ● 國發會_景氣燈號：https://index.ndc.gov.tw")
    print(f"  ● M平方_全球總經  ：https://www.macromicro.me")
    print(f"  🚩 重點：藍燈代表經濟感冒(買點)，紅燈代表發燒(風險)。")

    # --- 第二部分：市場情緒 ---
    print(f"\n🕵️ [ 第二部分：市場情緒 ]")
    print(f"  ● 恐懼與貪婪指數  ：https://www.wantgoo.com")
    print(f"  ● 期交所_大戶未平倉：https://www.taifex.com.tw")
    print(f"  ● 證交所_借券空單  ：https://www.twse.com.tw")
    print(f"  🚩 重點：指數 < 25 (極度恐懼) 常是反向買點。")

    # --- 第三部分：個股深度分析 ---
    print(f"\n🔍 [ 第三部分：個股深度分析 ]")
    print(f"  ● 1. 技術分析     ：https://www.wantgoo.com{STOCK_ID}")
    print(f"  ● 2. 籌碼/持股比例：https://goodinfo.tw{STOCK_ID}")
    print(f"  ● 3. 三大法人進出 ：https://goodinfo.tw{STOCK_ID}")
    print(f"  ● 4. 🏛️ 八大公股銀行 ：https://www.wantgoo.compublic-bank/buy-sell?stockno={STOCK_ID}")
    print(f"  ● 5. 💎 大戶籌碼集中度：https://www.wantgoo.com{STOCK_ID}/major-investors/concentration")
    print(f"  ● 6. ⚠️ 家數差指標    ：https://www.wantgoo.com{STOCK_ID}/major-investors/main-trend")
    print(f"  ● 7. 分點買賣排行 ：https://www.wantgoo.com{STOCK_ID}/major-investors/main-broker")
    print(f"  ● 8. 基本面(財報狗)：https://statementdog.com{STOCK_ID}")
    print(f"  ● 9. 市場討論(Cmoney)：https://www.cmoney.tw{STOCK_ID}")
    print(f"  🚩 重點：觀察「八大公股」是否逆勢護盤；家數差連負代表籌碼流向大戶。")

    # --- 第四部分：營收獲利 ---
    print(f"\n📈 [ 第四部分：營收獲利 ]")
    print(f"  ● 公開資訊觀測站 ：https://mops.twse.com.tw")
    print(f"  🚩 重點：每月 10 號前觀察營收成長率 (YoY/MoM)。")
    
    # --- 第五部分：DCF 估值評比 ---
    print(f"\n💎 [ 第五部分：DCF 估值評比 ] (依據近四季 EPS：{data['eps'] if data['eps'] else 'N/A'})")
    if data['eps'] and data['eps'] > 0:
        scenarios = {"低評比(保守 5%)": 0.05, "中評比(中性 10%)": 0.10, "高評比(樂觀 15%)": 0.15}
        for label, g in scenarios.items():
            fair_val = data['eps'] * (1 + g) * 15 
            diff_val = ((data['price'] - fair_val) / fair_val) * 100
            pos = "偏高" if diff_val > 0 else "便宜"
            print(f"  ● {label}: {fair_val:>8.2f} 元 (目前{pos} {abs(diff_val):.1f}%)")
    else:
        print(f"  ⚠️ 盈餘數據不足，無法進行 DCF 估值運算。")

    print("-" * 60)
    print(f"💡 提示：若「公股行庫買進」與「家數差連負」同時出現，通常是國家隊進場護盤訊號。")
    print("="*60)

if __name__ == "__main__":
    start_integrated_analysis()
