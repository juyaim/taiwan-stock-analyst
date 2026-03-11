# 台股分析師 - 全能數據庫 V4.6
# 新增功能：將您的個人 GitHub Pages 分點統計網址直接與股票代碼連動

import webbrowser

# 您的個人雲端網站基礎路徑 (確保路徑正確避免 404)
USER_BASE_URL = "https://juyaim.github.io"

def start_integrated_analysis():
    print("🚀 --- 全能台股導航 V4.6 啟動 --- 🚀")
    
    # 讓使用者輸入代碼
    target_stock = input("請輸入想查詢的股票代碼 (例如 2330): ").strip()
    if not target_stock:
        target_stock = "2330"
        
    print(f"\n【目前監控目標】：{target_stock}")
    print("-" * 50)

    # --- 核心深度分析連結 ---
    # 整合您的個人分點網頁與外部專業網站
    analysis_links = {
        "1. 您的雲端_三大法人趨勢": f"{USER_BASE_URL}/index.html", # 您的法人持股圖
        "2. 您的雲端_券商分點統計": f"{USER_BASE_URL}/broker_stats.html", # 您的分點統計頁
        "3. 玩股網_即時分點排行": f"https://www.wantgoo.com{target_stock}/major-investors/broker-buysell",
        "4. Goodinfo_分點買賣明細": f"https://goodinfo.tw{target_stock}",
        "5. 財報狗_獲利體質": f"https://statementdog.com{target_stock}"
    }

    # 輸出連結清單
    print(f"📈 [法人趨勢] 個人雲端圖表： {analysis_links['1. 您的雲端_三大法人趨勢']}")
    print(f"📊 [分點統計] 個人雲端統計： {analysis_links['2. 您的雲端_券商分點統計']}")
    print(f"🔍 [分點查詢] 玩股網即時排行：{analysis_links['3. 玩股網_即時分點排行']}")
    print(f"📋 [詳細明細] Goodinfo進出：  {analysis_links['4. Goodinfo_分點買賣明細']}")
    print("-" * 50)
    
    print(f"💡 戰術建議：")
    print(f"   1. 先看『個人雲端圖表』確認外資/投信是大買還是大賣。")
    print(f"   2. 若有異常，再到『個人雲端分點統計』或玩股網，輸入 {target_stock} 抓出帶頭的主力券商。")
    
    # 若想自動開啟個人網站，可將下面這行取消註解
    # webbrowser.open(analysis_links['2. 您的雲端_券商分點統計'])

if __name__ == "__main__":
    start_integrated_analysis()
