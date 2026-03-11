# 台股分析師 - 全能數據庫 V4.5 
# 新增功能：啟動後手動輸入股票代碼，自動生成券商分點與個人雲端連結

import webbrowser # 用於自動開啟網頁(選配)

# 您的個人雲端籌碼庫網址
MY_DASHBOARD_BASE = "https://juyaim.github.io"

def start_integrated_analysis():
    print("🚀 --- 全能台股導航 V4.5 啟動 --- 🚀")
    
    # --- 新增：動態輸入功能 ---
    target_stock = input("請輸入想查詢的股票代碼 (例如 2330): ").strip()
    if not target_stock:
        target_stock = "2330" # 若未輸入則預設為台積電
        
    print(f"\n【目前監控目標】：{target_stock}")
    print("-" * 50)

    # --- 第三部分：個股深度分析 (動態生成連結) ---
    analysis_links = {
        "1. 個人雲端籌碼圖": f"{MY_DASHBOARD_BASE}",
        "2. 玩股網_券商分點排行": f"https://www.wantgoo.com{target_stock}/major-investors/broker-buysell",
        "3. Goodinfo_分點進出明細": f"https://goodinfo.tw{target_stock}",
        "4. 玩股網_主力動向(集中度)": f"https://www.wantgoo.com{target_stock}/major-investors/main-trend",
        "5. 財報狗_基本面分析": f"https://statementdog.com{target_stock}"
    }

    # 輸出連結
    print(f"📈 [個人雲端] 籌碼走勢總覽： {analysis_links['1. 個人雲端籌碼圖']}")
    print(f"🔍 [分點查詢] 玩股網排行：   {analysis_links['2. 玩股網_券商分點排行']}")
    print(f"📋 [詳細明細] Goodinfo進出： {analysis_links['3. Goodinfo_分點進出明細']}")
    print(f"🎯 [大戶動向] 主力集中度：   {analysis_links['4. 玩股網_主力動向(集中度)']}")
    print("-" * 50)
    
    print(f"💡 操作提示：")
    print(f"   1. 先點開「個人雲端圖」，在搜尋框輸入 {target_stock} 看法人大趨勢。")
    print(f"   2. 若法人有大動作，再點「券商分點排行」看是哪間分點在買賣。")
    
    # 選配：自動打開最重要的分點網頁 (若不需要可註解掉)
    # webbrowser.open(analysis_links['2. 玩股網_券商分點排行'])

if __name__ == "__main__":
    start_integrated_analysis()
