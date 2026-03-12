import datetime

# --- 核心設定：修改此處代號即可 ---
STOCK_ID = "6274"  # 例如：2330, 7769, 6274, 3406

def start_integrated_analysis():
    now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    print(f"{'='*60}")
    print(f"🚀 全能台股分析導航 V4.51 | 深度工具箱模式")
    print(f"🎯 監控目標：{STOCK_ID}")
    print(f"⏰ 分析執行時間：{now_time}")
    print(f"{'='*60}")

    # --- 第一部分：宏觀環境 (不縮水) ---
    print(f"📊 [ 第一部分：宏觀環境 ]")
    print(f"  ● 國發會_景氣燈號：https://index.ndc.gov.tw")
    print(f"  ● M平方_全球總經  ：https://www.macromicro.me")
    print(f"  🚩 重點：看國家體檢表。藍燈代表經濟感冒(買點)，紅燈代表發燒(風險)。")

    # --- 第二部分：市場情緒 (不縮水) ---
    print(f"\n🕵️ [ 第二部分：市場情緒 ]")
    print(f"  ● 恐懼與貪婪指數  ：https://www.wantgoo.com")
    print(f"  ● 期交所_大戶未平倉：https://www.taifex.com.tw")
    print(f"  ● 證交所_借券空單  ：https://www.twse.com.tw")
    print(f"  🚩 重點：觀察大戶是否偷偷買跌(空單)。空單過多時，市場壓力較大。")

    # --- 第三部分：個股深度分析 (連結路徑精準修正) ---
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
    print(f"  🚩 重點：追蹤法人買賣超、毛利率趨勢；觀察家數差是否為負，找出關鍵分點。")

    # --- 第四部分：營收獲利 (不縮水) ---
    print(f"\n📈 [ 第四部分：營收獲利 ]")
    print(f"  ● 公開資訊觀測站 ：https://mops.twse.com.tw")
    print(f"  🚩 提醒：每月 10 號前觀察營收 YoY 與 MoM 成長動能。")

    # --- 第五部分：DCF 估值評比 (手動輸入模式) ---
    print(f"\n💎 [ 第五部分：DCF 估值公式參考 ]")
    print(f"  ● 公式：Fair Value = EPS * (1 + Growth) * PE")
    print(f"  ● 建議 PE：AI/半導體設備(25-35x)、傳產金融(12-15x)")

    print("-" * 60)
    print(f"💡 提示：本版本已剔除不穩定報價，連結已全數導通，點擊即可查看。")
    print("="*60)

if __name__ == "__main__":
    start_integrated_analysis()
