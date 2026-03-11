# ======================================================
# 台股分析師 - 全能數據庫 V4.9 (宏觀 + 籌碼 + 分點 究極版)
# ======================================================
# 功能：宏觀環境、市場情緒、個人雲端圖表、分點統計、主力排行
# 修復：解決 GitHub Pages 網址 404 路徑問題

import webbrowser

# --- 基礎設定：您的個人雲端網站路徑 ---
GITHUB_USER = "juyaim"
REPO_NAME = "tw-institutional-stocker"
BASE_URL = f"https://{GITHUB_USER}.github.io/{REPO_NAME}"

def start_integrated_analysis():
    print("=" * 70)
    print("🚀 --- 全能台股導航 V4.9 啟動 (宏觀/情緒/個股/分點) --- 🚀")
    print("=" * 70)
    
    # 讓使用者輸入代碼
    target_stock = input("📌 請輸入想查詢的股票代碼 (直接按 Enter 預設 2330): ").strip()
    if not target_stock:
        target_stock = "2330"
        
    print(f"\n【📡 當前監控目標：{target_stock} 】")
    print("-" * 70)

    # --- 第一部分：宏觀環境與政府指標 (市場的氣血) ---
    MACRO_INDICATORS = {
        "1. 國發會_景氣燈號": "https://index.ndc.gov.tw/n/zh_tw",
        "2. M平方_全球總經": "https://www.macromicro.me/trader-insights",
        "💡 重點提醒": "藍燈買進(經濟感冒)、紅燈減碼(經濟發燒)。"
    }

    # --- 第二部分：市場情緒與大戶底牌 (多空博弈) ---
    MARKET_SENTIMENT = {
        "1. 期交所_大戶未平倉": "https://www.taifex.com.tw/cht/index",
        "2. 證交所_借券空單": "https://www.twse.com.tw/zh/page/trading/exchange/TWTASU.html",
        "💡 重點提醒": "觀察大戶是否反向佈局，空單若暴增需警戒。"
    }

    # --- 第三部分：個股深度分析 (您的個人雲端 + 外部專業數據) ---
    STOCK_ANALYSIS = {
        "1. [個人雲端] 三大法人趨勢圖": f"{BASE_URL}/index.html",
        "2. [個人雲端] 券商分點統計表": f"{BASE_URL}/broker_stats.html",
        "3. [即時數據] 玩股網分點排行": f"https://www.wantgoo.com{target_stock}/major-investors/broker-buysell",
        "4. [詳細明細] Goodinfo買賣明細": f"https://goodinfo.tw{target_stock}",
        "5. [基本面] 財報狗體質分析": f"https://statementdog.com{target_stock}"
    }

    # --- 第四部分：營收獲利 (績效成績單) ---
    EARNINGS_REPORT = {
        "1. 公開資訊觀測站": "https://mops.twse.com.tw",
        "💡 重點提醒": "每月 10 號前觀察營收成長率 (YoY/MoM)。"
    }

    # --- 輸出所有連結 ---
    print("\n🌍 [第一部分] 宏觀環境：")
    for k, v in MACRO_INDICATORS.items(): print(f"   {k}: {v}")

    print("\n🎭 [第二部分] 市場情緒：")
    for k, v in MARKET_SENTIMENT.items(): print(f"   {k}: {v}")

    print("\n🔍 [第三部分] 個股與籌碼深度分析：")
    for k, v in STOCK_ANALYSIS.items(): print(f"   {k}: {v}")

    print("\n💰 [第四部分] 營收獲利：")
    for k, v in EARNINGS_REPORT.items(): print(f"   {k}: {v}")

    print("-" * 70)
    print(f"💡 【作戰指南】")
    print(f"   1. 先看「景氣燈號」確認大環境。")
    print(f"   2. 打開連結『個人雲端圖表』，看法人是否正同步買進 {target_stock}。")
    print(f"   3. 若有異常，到『個人雲端分點表』或『玩股網』抓出是哪家分點在搞鬼。")
    print("-" * 70)

if __name__ == "__main__":
    start_integrated_analysis()
