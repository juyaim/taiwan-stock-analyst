import datetime
import requests
import yfinance as yf

def get_verified_official_data_v443(sid):
    """
    通用型台股數據抓取模組
    """
    clean_id = sid.strip()
    try:
        # 優先嘗試上市代號 (.TW)，若無資料則切換至上櫃 (.TWO)
        ticker = yf.Ticker(f"{clean_id}.TW")
        info = ticker.info
        if not info.get('regularMarketPrice'):
            ticker = yf.Ticker(f"{clean_id}.TWO")
            info = ticker.info
            market = "[上櫃]"
        else:
            market = "[上市]"

        return {
            "price": info.get('currentPrice') or info.get('regularMarketPrice'),
            "prev_close": info.get('regularMarketPreviousClose'),
            "name": info.get('shortName', '未知名稱'),
            "eps": info.get('trailingEps') or info.get('forwardEps') or 0,
            "tid": clean_id,
            "market": market,
            "date": datetime.date.today().strftime("%Y-%m-%d")
        }
    except:
        return None

def start_integrated_analysis():
    print(f"{'='*60}")
    print(f"🚀 全能台股導航 V4.43 | 所有台股通用版")
    print(f"{'='*60}")
    
    STOCK_ID = input("👉 請輸入台股代號 (如 2330, 7769, 6669): ").strip()
    now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    data = get_verified_official_data_v443(STOCK_ID)
    
    if not data or data['price'] is None:
        print(f"❌ 錯誤：無法獲取 {STOCK_ID} 數據。請檢查網路或代號。")
        return

    # 1. 報價呈現
    diff = data['price'] - data['prev_close']
    pct = (diff / data['prev_close']) * 100
    status = f"{data['price']:,.2f} ({'▲' if diff > 0 else '▼' if diff < 0 else '─'} {abs(pct):.2f}%)"
    
    print(f"\n" + "="*60)
    print(f"📈 【 監控目標：{STOCK_ID} {data['name']} {data['market']} 】")
    print(f"💰 基準收盤價：{status}")
    print(f"📅 數據基準日期：{data['date']}")
    print(f"⏰ 分析執行時間：{now_time}")
    print("="*60)

    # --- 第一部分：宏觀環境 ---
    print(f"📊 [ 第一部分：宏觀環境 ]")
    print(f"  ● 國發會_景氣燈號：https://index.ndc.gov.tw")
    print(f"  ● M平方_全球總經  ：https://www.macromicro.me")
    print(f"  🚩 評價：藍燈代表買點，紅燈代表風險。")

    # --- 第二部分：市場情緒 ---
    print(f"\n🕵️ [ 第二部分：市場情緒 ]")
    print(f"  ● 恐懼與貪婪指數  ：https://www.wantgoo.com")
    print(f"  ● 期交所_大戶未平倉：https://www.taifex.com.tw")
    print(f"  ● 證交所_借券空單  ：https://www.twse.com.tw")

    # --- 第三部分：個股深度分析 (精準網址修正版) ---
    print(f"\n🔍 [ 第三部分：個股深度分析 ]")
    print(f"  ● 1. 技術分析      ：https://www.wantgoo.com{STOCK_ID}")
    print(f"  ● 2. 籌碼/持股比例 ：https://goodinfo.tw{STOCK_ID}")
    print(f"  ● 3. 三大法人進出  ：https://goodinfo.tw{STOCK_ID}")
    print(f"  ● 4. 🏛️ 八大公股銀行 ：https://www.wantgoo.compublic-bank/buy-sell?stockno={STOCK_ID}")
    print(f"  ● 5. 💎 大戶籌碼集中度：https://www.wantgoo.com{STOCK_ID}/major-investors/concentration")
    print(f"  ● 6. ⚠️ 家數差指標    ：https://www.wantgoo.com{STOCK_ID}/major-investors/main-trend")
    print(f"  ● 7. 分點買賣排行  ：https://www.wantgoo.com{STOCK_ID}/major-investors/main-broker")
    print(f"  ● 8. 基本面(財報狗)：https://statementdog.com{STOCK_ID}")
    print(f"  ● 9. 市場討論(Cmoney)：https://www.cmoney.tw{STOCK_ID}")

    # --- 第四部分：營收獲利 ---
    print(f"\n📈 [ 第四部分：營收獲利 ]")
    print(f"  ● 公開資訊觀測站 ：https://mops.twse.com.tw")
    print(f"  🚩 重點：每月 10 號前觀察營收成長率。")
    
    # --- 第五部分：DCF 估值評比 ---
    eps_val = data['eps']
    print(f"\n💎 [ 第五部分：DCF 估值評比 ] (依據近四季 EPS：{eps_val if eps_val > 0 else 'N/A'})")
    if eps_val > 0:
        # 設定通用型合理 PE 為 20 倍 (可視不同產業自行調整)
        base_pe = 20 
        for label, g in {"低評(5%)": 0.05, "中評(10%)": 0.10, "高評(15%)": 0.15}.items():
            fair = eps_val * (1 + g) * base_pe
            diff_val = ((data['price'] - fair) / fair) * 100
            print(f"  ● {label}: {fair:>8.2f} 元 (目前{'偏高' if diff_val > 0 else '便宜'} {abs(diff_val):.1f}%)")
    else:
        print("  ⚠️ 盈餘為負或無數據，無法進行估值計算。")
    
    print("-" * 60)
    print(f"💡 提示：本報價已自動同步至最新市場交易數據。")
    print("="*60)

if __name__ == "__main__":
    start_integrated_analysis()
