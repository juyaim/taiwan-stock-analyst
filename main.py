import datetime
import requests
import yfinance as yf
from bs4 import BeautifulSoup

# --- 核心數據抓取：Google Finance 實時報價 ---
def get_google_data(sid):
    """
    V4.22 修正版：採用 Google Finance 確保 2026 報價零延遲
    """
    clean_id = "".join(filter(str.isdigit, sid))
    # 嘗試上市 (TPE) 與 上櫃 (TWO)
    for exchange in ["TPE", "TWO"]:
        url = f"https://www.google.com{clean_id}:{exchange}"
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
        try:
            resp = requests.get(url, headers=headers, timeout=10)
            if resp.status_code != 200: continue
            
            soup = BeautifulSoup(resp.text, "html.parser")
            # 抓取股價與漲跌幅
            price_box = soup.find("div", {"class": "YMl6ce"})
            name_box = soup.find("div", {"class": "zzDe9c"})
            change_box = soup.find("div", {"class": "Jw7C9b"})
            
            if price_box:
                price = float(price_box.text.replace("$", "").replace(",", ""))
                # 抓取 EPS (藉由 yfinance 輔助，確保 DCF 正常)
                ticker = yf.Ticker(f"{clean_id}.TW" if exchange=="TPE" else f"{clean_id}.TWO")
                eps = ticker.info.get('trailingEps') or ticker.info.get('forwardEps')
                
                return {
                    "price": price,
                    "status_text": change_box.text if change_box else "N/A",
                    "name": name_box.text if name_box else "台股個股",
                    "eps": eps,
                    "market": "[上市]" if exchange=="TPE" else "[上櫃]"
                }
        except:
            continue
    return None

def start_integrated_analysis():
    print(f"{'='*60}")
    print(f"🚀 全能台股導航 V4.22 | Google Finance 實時引擎")
    print(f"{'='*60}")
    
    STOCK_ID = input("👉 請輸入台股代號 (例如 3037 或 2454): ").strip()
    now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # 執行數據抓取
    data = get_google_data(STOCK_ID)
    
    if not data:
        print(f"❌ 錯誤：無法從交易所取得 {STOCK_ID} 之實時報價。")
        return

    # 1. 顯示當下精準股價
    print(f"\n" + "="*60)
    print(f"📈 【 監控目標：{STOCK_ID} {data['name']} {data['market']} 】")
    print(f"💰 Google 當下股價：{data['price']:.2f} ({data['status_text']})")
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
        scenarios = {"低評比(保守 5%)": 0.05, "中評比(中性 10%)": 0.10, "高評比(樂觀 15%)": 0.15}
        for label, g in scenarios.items():
            fair_val = data['eps'] * (1 + g) * 15 
            diff = ((data['price'] - fair_val) / fair_val) * 100
            pos = "偏高" if diff > 0 else "便宜"
            print(f"  ● {label}: {fair_val:>8.2f} 元 (目前{pos} {abs(diff):.1f}%)")
    else:
        print(f"  ⚠️ 盈餘數據不足，無法進行 DCF 估值。請參考財報狗最新 EPS。")

    print("-" * 60)
    print(f"💡 綜合提示：若股價低於「中評比」且「恐懼指數」極低，通常是極佳買點。")
    print("="*60)

if __name__ == "__main__":
    start_integrated_analysis()
