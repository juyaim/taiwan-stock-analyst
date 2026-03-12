import datetime
import yfinance as yf

# ==========================================
# 小提示：只需修改下方的 "2330" 即可更換個股
STOCK_ID = "2330" 
# ==========================================

def get_taiwan_stock_data(sid):
    """自動偵測上市(.TW)或上櫃(.TWO)並抓取股價"""
    for suffix in [".TW", ".TWO"]:
        ticker_id = f"{sid}{suffix}"
        ticker = yf.Ticker(ticker_id)
        try:
            # 嘗試抓取即時資訊
            info = ticker.fast_info
            if info.last_price > 0:
                price = info.last_price
                prev_close = info.previous_close
                change = price - prev_close
                pct = (change / prev_close) * 100
                return price, pct, ticker_id
        except:
            continue
    return None, None, None

def start_integrated_analysis():
    # 1. 取得當下時間與股價數據
    now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    price, pct, full_id = get_taiwan_stock_data(STOCK_ID)
    
    # 2. 判斷漲跌符號與顏色 (提示用)
    if price:
        status = f"{price:.2f} ({'▲' if pct > 0 else '▼' if pct < 0 else '─'} {abs(pct):.2f}%)"
    else:
        status = "查無資料 (請確認代號是否正確)"

    print(f"{'='*60}")
    print(f"🚀 全能台股導航 V4.4 | 查詢時間：{now_time}")
    print(f"📈 【 監控目標：{STOCK_ID} 】 目前報價：{status}")
    print(f"{'='*60}")

    # --- 第一部分：宏觀環境 (市場氣血) ---
    print(f"● 國發會景氣燈號：https://index.ndc.gov.tw")
    print(f"● M平方全球總經 ：https://www.macromicro.me")

    # --- 第二部分：市場情緒 (多空博弈) ---
    print(f"● 期交所大戶籌碼：https://www.taifex.com.tw")
    print(f"● 證交所借券賣出：https://www.twse.com.tw")

    # --- 第三部分：個股深度分析 (精準穴位) ---
    print("-" * 60)
    print(f"● 技術分析(玩股) ：https://www.wantgoo.com{STOCK_ID}")
    print(f"● 主力動向(集中度)：https://www.wantgoo.com{STOCK_ID}/major-investors/main-trend")
    print(f"● 關鍵分點(找大咖)：https://www.wantgoo.com{STOCK_ID}/major-investors/main-broker")
    print(f"● 法人籌碼(持股比)：https://goodinfo.tw{STOCK_ID}")
    print(f"● 基本面(財報狗) ：https://statementdog.com{STOCK_ID}")
    print(f"● 市場討論(Cmoney)：https://www.cmoney.tw{STOCK_ID}")
    print("-" * 60)

    # --- 第四部分：營收獲利 (績效成績單) ---
    print(f"● 公開資訊觀測站 ：https://mops.twse.com.tw")
    print(f"💡 重點：每月10號前看營收 YoY；觀察關鍵分點是否在低檔吃貨。")
    print(f"{'='*60}")

if __name__ == "__main__":
    start_integrated_analysis()
