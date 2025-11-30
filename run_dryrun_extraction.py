import pandas as pd
import json

def run_dryrun_extraction(csv_path='Dataset_clean.csv'):
    print(f"正在讀取 {csv_path} ...")
    
    try:
        # 嘗試讀取 CSV (預設逗號分隔)
        # 如果你的檔案是 Tab 分隔，請將 sep=',' 改為 sep='\t'
        df = pd.read_csv(csv_path, sep=',') 
        
        # 簡單檢查欄位名稱，將欄位名稱統一轉小寫以防萬一
        df.columns = df.columns.str.lower().str.strip()
        
        # 確保需要的欄位存在 (根據你提供的範例)
        # 假設你的 CSV 欄位是: headline, category, authors, short_description
        if 'headline' not in df.columns or 'category' not in df.columns:
            print("錯誤：找不到 'headline' 或 'category' 欄位。")
            print("你的欄位名稱是:", df.columns.tolist())
            return

        # 準備存放 3x3 資料的 Dict
        demo_data = {}
        
        # 取得所有分類
        unique_categories = df['category'].unique()
        
        # 取前 3 個分類
        target_categories = unique_categories[:3]
        
        print(f"選定的 3 個分類: {target_categories}")
        
        for cat in target_categories:
            # 篩選該分類的資料
            cat_df = df[df['category'] == cat]
            
            # 取前 3 筆，並只保留我們需要的欄位
            # fillna('') 是為了防止簡介空白導致報錯
            top_3 = cat_df[['headline', 'short_description']].fillna('').head(3).to_dict('records')
            
            demo_data[cat] = top_3

        # --- 輸出結果 ---
        print("\n" + "="*20 + " DRY RUN 結果 (請複製下方內容) " + "="*20 + "\n")
        
        # 使用 json.dumps 漂亮印出，方便你複製貼上
        print(json.dumps(demo_data, indent=4, ensure_ascii=False))
        
        print("\n" + "="*60)
        print("請將上面 JSON 格式的內容複製貼給我。")

    except FileNotFoundError:
        print(f"錯誤：找不到檔案 {csv_path}。請確認檔案位置。")
    except Exception as e:
        print(f"發生未預期的錯誤: {e}")

if __name__ == "__main__":
    run_dryrun_extraction()