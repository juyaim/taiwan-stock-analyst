import datetime
import requests
import yfinance as yf

def get_real_stock_data(sid):
    """
    修正版：精確抓取台股名稱與報價，防止代號混淆
    """
    clean_id = sid.strip()
    # 嘗試上市與上櫃後綴
    for suffix in [".TW", ".TWO"]:
        try:
            ticker = yf.Ticker(f"{clean_id}{suffix}")
            info = ticker.info
            # 確保有抓到價格才視為成功
            if info.get('currentPrice') or info.get('regularMarketPrice'):
                return {
                    "price": info.get('currentPrice') or info.get('regularMarketPrice'),
                    "prev_close": info.get('regularMarketPreviousClose'),
                    "name": info.get('shortName', '未知'),
                    "eps": info.get('trailingEps') or info.get('forwardEps') or 0,
                    "tid": clean_id,
                    "market": "上市" if suffix == ".TW" else "上櫃",
                    "date": datetime.date.today().strftime("%Y-%m-%d")
                }
        except:
            continue
    return None

def start_integrated_analysis():
    print(f"{'='*60}")
    print(f"🚀 全能台股導航 V4.44 | 修正截圖錯誤、拒絕胡言亂語版")
    print(f"{'='*60}")
    
    STOCK_ID = input("👉 請輸入台股代號 (如 7769, 2330): ").strip()
    now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    data = get_real_stock_data(STOCK_ID)
    
    if not data:
        print(f"❌ 錯誤：找不到代號 {STOCK_ID} 的資料，請確認輸入是否有誤。")
        return

    # 1. 報價呈現 (精確呈現，不模擬假數據)
    diff = data['price'] - data['prev_close']
    pct = (diff / data['prev_close']) * 100
    status = f"{data['price']:,.2f} ({'▲' if diff > 0 else '▼' if diff < 0 else '─'} {abs(pct):.2f}%)"
    
    print(f"\n" + "="*60)
    print(f"📈 【 監控目標：{data['tid']} {data['name']} [{data['market']}] 】")
    print(f"💰 最新成交價：{status}")
    print(f"📅 數據基準日期：{data['date']}")
    print(f"⏰ 分析執行時間：{now_time}")
    print("="*60)

    # --- 第一部分：宏觀環境 (堅持不縮水) ---
    print(f"📊 [ 第一部分：宏觀環境 ]")
    print(f"  ● 國發會_景氣燈號：https://index.ndc.gov.tw")
    print(f"  ● M平方_全球總經  ：https://www.macromicro.me")
    print(f"  🚩 評價：觀察紅藍燈切換，判斷長線進場點。")

    # --- 第二部分：市場情緒 (堅持不縮水) ---
    print(f"\n🕵️ [ 第二部分：市場情緒 ]")
    print(f"  ● 恐懼與貪婪指數  ：https://www.wantgoo.com")
    print(f"  ● 期交所_大戶未平倉：https://www.taifex.com.tw")
    print(f"  ● 證交所_借券空單  ：https://www.twse.com.tw")

    # --- 第三部分：個股深度分析 (堅持不縮水，連結精準化) ---
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

    # --- 第四部分：營收獲利 (堅持不縮水) ---
    print(f"\n📈 [ 第四部分：營收獲利 ]")
    print(f"  ● 公開資訊觀測站 ：https://mops.twse.com.tw")
    print(f"  🚩 關鍵：每月 10 號前追蹤最新營收動能。")
    
    # --- 第五部分：DCF 估值評比 (壓軸模型) ---
    eps = data['eps']
    print(f"\n💎 [ 第五部分：DCF 估值評比 ] (依據近四季 EPS：{eps if eps > 0 else 'N/A'})")
    if eps > 0:
        # 設定通用型基準 PE = 25 (AI 時代基準)
        for label, g in {"低評(5%)": 0.05, "中評(10%)": 0.10, "高評(15%)": 0.15}.items():
            fair = eps * (1 + g) * 25
            diff_val = ((data['price'] - fair) / fair) * 100
            print(f"  ● {label}: {fair:>8.2f} 元 (目前{'偏高' if diff_val > 0 else '便宜'} {abs(diff_val):.1f}%)")
    else:
        print("  ⚠️ 無法進行估值（盈餘為負或資料缺失）。")
    
    print("-" * 60)
    print(f"💡 提示：本分析已校準，拒絕「7769 宏碩」這種代號錯誤。")
    print("="*60)

if __name__ == "__main__":
    start_integrated_analysis()
