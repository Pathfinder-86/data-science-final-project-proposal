import google.generativeai as genai
import os

# 設定 API Key
# 建議將 API Key 設為環境變數，或直接填入字串 (注意資安)
# os.environ["GOOGLE_API_KEY"] = "YOUR_API_KEY"
# genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

# 這裡直接使用你提供的 Key (請注意不要將此檔案公開到 GitHub 等平台)
API_KEY = "AIzaSyCy4siQ7xx2afvwmOwMM04s2D5gkbSRoXY"
genai.configure(api_key=API_KEY)

# 初始化模型 (使用 gemini-2.0-flash)
model = genai.GenerativeModel('gemini-2.0-flash')

def analyze_news_english(headline, category, short_description):
    """
    使用 Gemini 分析新聞標題與簡介，提取重要單字並解釋。
    """
    
    # 構建 Prompt (提示詞)
    prompt = f"""
    我正在開發一個英語學習 App。請針對以下的新聞資料進行分析，目標是幫助使用者學習英語。

    新聞資料：
    - Category (類別): {category}
    - Headline (標題): {headline}
    - Short Description (簡介): {short_description}

    請完成以下任務：
    1. **重要單字評估**：從標題和簡介中挑選 3-5 個適合學習的重要單字或片語 (難度適中或新聞常用)。
    2. **單字解釋與例句**：針對每個挑選的單字，提供：
       - 中文解釋
       - 詞性
       - 在新聞中的用法解釋
       - 一個新的例句 (不同於新聞內容)
    3. **整體難度評估**：請給這則新聞的英語閱讀難度打分 (1-5分，1為最簡單)，並簡述原因。

    請以結構清晰、易於閱讀的格式輸出 (例如 Markdown)。
    """

    try:
        # 發送請求給 Gemini
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"發生錯誤: {str(e)}"

# --- 範例測試 ---
if __name__ == "__main__":
    # 範例輸入
    sample_headline = "Over 4 Million Americans Roll Up Sleeves For Omicron-Targeted COVID Boosters"
    sample_category = "U.S. NEWS"
    sample_short_description = "Health experts said it is too early to predict whether demand would match up with the 171 million doses of the new boosters the U.S. ordered for the fall."

    print("正在分析新聞英語內容...\n")
    result = analyze_news_english(sample_headline, sample_category, sample_short_description)
    print(result)
