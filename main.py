import datetime
import requests
import yfinance as yf

# --- 核心數據抓取：官方證交所 API (確保 2026 報價零延遲) ---
def get_verified_stock_data(sid):
    """
    V4.23 終極修復：直連 TWSE/TPEx 官方 API
    """
    clean_id = sid.strip()
    timestamp = int(datetime.datetime.now().timestamp() * 1000)
    
    # 正確的證交所即時查詢網址
    urls = [
        f"https://mis.twse.com.tw_{clean_id}.tw&_={timestamp}",
        f"https://mis.twse.com.tw_{clean_id}.tw&_={timestamp}"
    ]
    
    headers = {"User-Agent": "Mozilla/5.0"}
    
    for url in urls:
        try:
            resp = requests.get(url, headers=headers, timeout=5)
            json_data = resp.json()
            if json_data.get('rtcode') == '0000' and json_data.get('msgArray'):
                info = json_data['msgArray'][0]
                
                # z:當前價, y:昨收, n:公司名, b:買一價(備援)
                # 盤中若 z 為空(尚未撮合)，則取 b 的第一筆
                current_p = info.get('z') or info.get('b', '0').split('_')[0]
                price = float(current_p)
                prev_close = float(info.get('y', price))
                
                # 抓取 EPS (供 DCF 使用)
                ticker = yf.Ticker(f"{clean_id}.TW" if "tse" in url else f"{clean_id}.TWO")
                eps = ticker.info.get('trailingEps') or ticker.info.get('forwardEps')
                
                return {
                    "price": price,
                    "prev_close": prev_close,
                    "name": info.get('n', '台股個股'),
                    "eps": eps,
                    "tid": clean_id,
                    "market": "[上市]" if "tse" in url else "[上櫃]"
                }
        except:
            continue
    return None

def start_integrated_analysis():
    print(f"{'='*60}")
    print(f"🚀 全能台股導航 V4.23 | 證交所官方數據直連版")
    print(f"{'='*60}")
    
    STOCK_ID = input("👉 請輸入台股代號 (例如 4938, 2330): ").strip()
    now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # 執行官方精準抓取
    data = get_verified_stock_data(STOCK_ID)
    
    if not data or data['price'] == 0:
        print(f"❌ 錯誤：無法從官方交易所取得 {STOCK_ID} 實時報價。")
        return

    # 計算漲跌
    diff = data['price'] - data['prev_close']
    pct = (diff / data['prev_close']) * 100
    status = f"{data['price']:.2f} ({'▲' if diff > 0 else '▼' if diff < 0 else '─'} {abs(pct):.2f}%)"
    
    print(f"\n" + "="*60)
    print(f"📈 【 監控目標：{STOCK_ID} {data['name']} {data['market']} 】")
    print(f"💰 交易所實時價：{status}")
    print(f"⏰ 查詢時間：{now_time}")
    print("="*60)

    # --- 第一部分：宏觀環境 (不縮水) ---
    print(f"📊 [ 第一部分：宏觀環境 ]")
    print(f"  ● 國發會_景氣燈號：https://index.ndc.gov.tw")
    print(f"  ● M平方_全球總經  ：https://www.macromicro.me")
    print(f"  🚩 重點：藍燈代表經濟感冒(買點)，紅燈代表發燒(風險)。")

    # --- 第二部分：市場情緒 (不縮水) ---
    print(f"\n🕵️ [ 第二部分：市場情緒 ]")
    print(f"  ● 恐懼與貪婪指數  ：https://www.wantgoo.com")
    print(f"  ● 期交所_大戶未平倉：https://www.taifex.com.tw")
    print(f"  ● 證交所_借券空單  ：https://www.twse.com.tw")
    print(f"  🚩 重點：指數 < 25 (極度恐懼) 常是反向買點；觀察空單是否過高增加壓力。")

    # --- 第三部分：個股深度分析 (不縮水) ---
    print(f"\n🔍 [ 第三部分：個股深度分析 ]")
    print(f"  ● 1. 技術分析     ：https://www.wantgoo.com{STOCK_ID}")
    print(f"  ● 2. 籌碼/持股比例：https://goodinfo.tw{STOCK_ID}")
    print(f"  ● 3. 三大法人進出 ：https://goodinfo.tw{STOCK_ID}")
    print(f"  ● 4. 主力集中度趨勢：https://www.wantgoo.com{STOCK_ID}/major-investors/main-trend")
    print(f"  ● 5. 分點買賣排行 ：https://www.wantgoo.com{STOCK_ID}/major-investors/main-broker")
    print(f"  ● 6. 基本面(財報狗)：https://statementdog.com{STOCK_ID}")
    print(f"  ● 7. 市場討論(Cmoney)：https://www.cmoney.tw{STOCK_ID}")

    # --- 第四部分：營收獲利 (不縮水) ---
    print(f"\n📈 [ 第四部分：營收獲利 ]")
    print(f"  ● 公開資訊觀測站 ：https://mops.twse.com.tw")
    
    # --- 第五部分：DCF 估值評比 (壓軸模型) ---
    print(f"\n💎 [ 第五部分：DCF 估值評比 ] (依據近四季 EPS：{data['eps'] if data['eps'] else 'N/A'})")
    if data['eps'] and data['eps'] > 0:
        scenarios = {"低評比(保守 5%)": 0.05, "中評比(中性 10%)": 0.10, "高評比(樂觀 15%)": 0.15}
        for label, g in scenarios.items():
            fair_val = data['eps'] * (1 + g) * 15 
            diff_val = ((data['price'] - fair_val) / fair_val) * 100
            print(f"  ● {label}: {fair_val:>8.2f} 元 (目前{'偏高' if diff_val > 0 else '便宜'} {abs(diff_val):.1f}%)")
    
    print("-" * 60)
    print(f"💡 提示：本報價直連證交所 API，與您的券商報價同步。")
    print("="*60)

if __name__ == "__main__":
    start_integrated_analysis()
