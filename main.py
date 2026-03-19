import datetime

# --- 核心設定：修改此處代號即可 ---
STOCK_ID = "2367"  # 例如：2330, 7769, 6274, 3406

def start_integrated_analysis_v6():
    now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    print(f"{'='*65}")
    print(f"🚀 全能台股分析導航 V6.0 | 旗艦工具箱 & 大戶警報")
    print(f"🎯 監控目標：{STOCK_ID}")
    print(f"⏰ 分析執行時間：{now_time}")
    print(f"{'='*65}")

    # --- 第一部分：宏觀與市場 (繼承自你的 main.py) ---
    print(f"📊 [ 第一部分：宏觀環境 ]")
    print(f"  ● 國發會_景氣燈號：https://index.ndc.gov.tw")
    print(f"  ● M平方_全球總經  ：https://www.macromicro.me")
    
    print(f"\n🕵️ [ 第二部分：市場情緒 ]")
    print(f"  ● 恐懼與貪婪指數  ：https://www.wantgoo.com")
    print(f"  ● 期交所_大戶未平倉：https://www.taifex.com.tw")
    print(f"  ● 證交所_借券空單  ：https://www.twse.com.tw")

    # --- 第三部分：個股深度分析 (連結全面優化導通) ---
    print(f"\n🔍 [ 第三部分：個股深度分析 ]")
    # 技術面
    print(f"  ● 1. 技術分析      ：https://www.wantgoo.com/stock/{STOCK_ID}")
    # 籌碼面
    print(f"  ● 2. 💎 大戶/持股比例：https://goodinfo.tw/tw/EquityDistributionChart.asp?STOCK_ID={STOCK_ID}")
    print(f"  ● 3. 💎 集中度/法人  ：https://www.wantgoo.com/stock/{STOCK_ID}/major-investors/concentration")
    print(f"  ● 4. ⚠️ 家數差指標    ：https://www.wantgoo.com/stock/{STOCK_ID}/major-investors/main-trend")
    # 官股與分點
    print(f"  ● 5. 🏛️ 八大公股銀行 ：https://www.wantgoo.com/public-bank/buy-sell?stockno={STOCK_ID}")
    print(f"  ● 6. 分點買賣排行  ：https://www.wantgoo.com/stock/{STOCK_ID}/major-investors/main-broker")
    # 基本面與討論
    print(f"  ● 7. 基本面(財報狗)：https://statementdog.com/analysis/{STOCK_ID}")
    print(f"  ● 8. 市場討論(Cmoney)：https://www.cmoney.tw/follow/channel/stock-{STOCK_ID}")

    # --- 第四部分：自動警報與生意點評 ---
    print(f"\n🚨 [ 第四部分：大戶行為模擬診斷 ]")
    print(f"  💡 請手動比對上述連結數據，進入以下診斷流程：")
    
    print(f"  [ 🟢 偏多訊號 ] 400張大戶 > 35% 或 家數差連續為負數 (籌碼極度集中)。")
    print(f"  [ 🟡 觀望訊號 ] 股價高檔但主力賣超、家數差轉正 (散戶進場，需注意回檔)。")
    print(f"  [ 🔴 偏空訊號 ] 跌破月線 (MA20) 且大戶比例顯著下滑。")

    # --- 第五部分：戰略總結 (Ref: 2367 專屬邏輯) ---
    print(f"\n📝 [ 第五部分：生意經戰略點評 ]")
    strategy = [
        f"這不是普通的股票，這是低軌衛星的門票。目前的 77.9 元買的是『機會』。",
        "守住 74.4 元盤中支撐，絕不能收破。",
        "若大戶比例衝破 35%，100 元的目標將更有把握。",
        "每月 10 號前觀察營收 YoY 是否持續雙位數成長。"
    ]
    for i, s in enumerate(strategy, 1):
        print(f"  {i}. {s}")

    # --- 第六部分：DCF 估值評比 (手動輸入模式參考) ---
    print(f"\n💎 [ 第六部分：DCF 估值公式參考 ]")
    print(f"  ● 公式：Fair Value = EPS * (1 + Growth) * PE")
    print(f"  ● 建議 PE：")
    print(f"    - 高成長/衛星 (18-25x) → 燿華適用參考")
    print(f"    - AI/半導體設備 (25-35x)")
    print(f"    - 傳統產業/金融 (12-15x)")
    print(f"  🚩 練習：若 2367 預期 EPS 為 5.5，給予 18 倍 PE，則目標價約為 99 元。")

    print("-" * 65)
    print(f"💡 提示：本版本已修正所有 URL 格式，點擊即可直達該個股之分頁。")
    print("="*65)

if __name__ == "__main__":
    start_integrated_analysis_v6()
