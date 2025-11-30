import streamlit as st
import os

# --- 1. 資料層 (Rich Content Dataset) ---
# 依照你的要求，將內容擴充為「教材等級」的深度解析
# 包含：詞彙解釋、文法分析、原文例句、額外例句

def load_rich_data():
    return {
        "U.S. NEWS": {
            "cover": "images/cat_us_news.png",
            "articles": [
                {
                    "headline": "Over 4 Million Americans Roll Up Sleeves For Omicron-Targeted COVID Boosters",
                    "short_description": "Health experts said it is too early to predict whether demand would match up with the 171 million doses of the new boosters the U.S. ordered for the fall.",
                    "image": "images/us_news_1.png",
                    "translation": "衛生專家表示，目前要預測市場需求是否會與美國政府為秋季訂購的 1.71 億劑新型加強針數量相符，還為時過早。",
                    "vocab": [
                        {
                            "word": "Roll up sleeves",
                            "type": "片語 / 雙關語",
                            "explanation": "這是一個非常生動的片語。(1) 字面意思：真的把袖子捲起來（通常是為了打針或做粗活）。(2) 慣用語意思：準備開始努力工作、大幹一場。在這則新聞標題中，作者用了雙關修辭：既是指民眾真的捲起袖子打疫苗，也暗示美國人積極採取行動對抗病毒。",
                            "original": "Over 4 Million Americans Roll Up Sleeves For... Boosters",
                            "example": "There's a lot of work to do, so let's roll up our sleeves and get started. (有很多工作要做，讓我們捲起袖子開始幹活吧。)"
                        },
                        {
                            "word": "Match up with",
                            "type": "片語",
                            "explanation": "意思是「與...相符」、「與...匹配」或「達到...（相同的水平）」。常於比較兩個數據、供需雙方或證詞是否一致。",
                            "original": "...whether demand would match up with the 171 million doses...",
                            "example": "The suspect's fingerprints matched up with those found at the scene. (嫌疑犯的指紋與現場發現的指紋相符。)"
                        },
                        {
                            "word": "Targeted",
                            "type": "形容詞 / 過去分詞",
                            "explanation": "來自名詞 Target (目標)。在這裡作為形容詞，意思是「有針對性的」、「以...為目標的」。文法解析：Omicron-Targeted 是一個複合形容詞，結構是「名詞 + 過去分詞」，表示「專攻 Omicron 的」。",
                            "original": "...For Omicron-Targeted COVID Boosters",
                            "example": "We are running a targeted advertising campaign for pet owners. (我們正在進行一項針對寵物主人的廣告活動。)"
                        }
                    ]
                },
                {
                    "headline": "American Airlines Flyer Charged, Banned For Life After Punching Flight Attendant On Video",
                    "short_description": "He was subdued by passengers and crew when he fled to the back of the aircraft after the confrontation, according to the U.S. attorney's office in Los Angeles.",
                    "image": "images/us_news_2.png",
                    "translation": "根據洛杉磯美國檢察官辦公室表示，他在衝突後逃往飛機後方時，被乘客和機組人員制伏。該名美國航空乘客因被錄影拍到毆打空服員而被起訴並終身禁飛。",
                    "vocab": [
                        {
                            "word": "Subdue",
                            "type": "動詞 (v.)",
                            "explanation": "意思是「制伏」、「壓制」或「克制（情緒）」。通常指透過武力或強勢手段使某人冷靜或停止反抗。在新聞中常用於警方逮捕嫌犯或平息騷亂的場景。",
                            "original": "He was subdued by passengers and crew...",
                            "example": "Police managed to subdue the angry crowd without using tear gas. (警方在不使用催淚瓦斯的情況下設法平息了憤怒的人群。)"
                        },
                        {
                            "word": "Flee",
                            "type": "動詞 (v.) / 不規則變化",
                            "explanation": "意思是「逃跑」、「迅速離開（危險之地）」。注意它的動詞三態是不規則變化：flee / fled / fled。這裡使用的是過去式 fled。",
                            "original": "...when he fled to the back of the aircraft...",
                            "example": "The refugees were forced to flee their homes due to the war. (難民因戰爭被迫逃離家園。)"
                        },
                        {
                            "word": "Confrontation",
                            "type": "名詞 (n.)",
                            "explanation": "意思是「對抗」、「衝突」或「對質」。通常指雙方帶有敵意的面對面接觸。動詞形態是 Confront (面對、遭遇)。",
                            "original": "...after the confrontation...",
                            "example": "She tried to avoid a direct confrontation with her boss. (她試圖避免與老闆發生正面衝突。)"
                        }
                    ]
                },
                {
                    "headline": "Woman Who Called Cops On Black Bird-Watcher Loses Lawsuit Against Ex-Employer",
                    "short_description": "Amy Cooper accused investment firm Franklin Templeton of unfairly firing her and branding her a racist after video of the Central Park encounter went viral.",
                    "image": "images/us_news_3.png",
                    "translation": "Amy Cooper 指控投資公司富蘭克林坦伯頓不公平解雇她，並在中央公園事件影片瘋傳後將她貼上種族主義者的標籤。但她最終敗訴。",
                    "vocab": [
                        {
                            "word": "Lawsuit",
                            "type": "名詞 (n.)",
                            "explanation": "意思是「訴訟」、「官司」。常見搭配詞有 file a lawsuit (提起訴訟)、win/lose a lawsuit (勝訴/敗訴)。",
                            "original": "...Loses Lawsuit Against Ex-Employer",
                            "example": "The company settled the lawsuit out of court. (該公司在庭外和解了這起訴訟。)"
                        },
                        {
                            "word": "Brand",
                            "type": "動詞 (v.)",
                            "explanation": "名詞是「品牌」，但作為動詞時，意思是「加污名於...」、「將...打上烙印」。這裡指公司公開將她定性為種族主義者，對其名譽造成影響。",
                            "original": "...branding her a racist...",
                            "example": "The media branded him a traitor. (媒體將他貼上叛徒的標籤。)"
                        },
                        {
                            "word": "Go viral",
                            "type": "片語 (phr.)",
                            "explanation": "網路世代常用語，指「（像病毒一樣）瘋傳」、「爆紅」。通常指影片或貼文在短時間內被大量轉發。",
                            "original": "...after video of the Central Park encounter went viral.",
                            "example": "Her dance video went viral on TikTok overnight. (她的跳舞影片一夜之間在 TikTok 上爆紅。)"
                        }
                    ]
                }
            ]
        },
        "COMEDY": {
            "cover": "images/cat_comedy.png",
            "articles": [
                {
                    "headline": "23 Of The Funniest Tweets About Cats And Dogs This Week",
                    "short_description": "\"Until you have a dog you don't understand what could be eaten.\"",
                    "image": "images/comedy_1.png",
                    "translation": "「除非你養了狗，否則你永遠不懂什麼東西居然能被吃掉。」",
                    "vocab": [
                        {
                            "word": "Until... don't...",
                            "type": "句型結構",
                            "explanation": "這是一個強調句型：「直到...才...」或者翻成「除非...否則不...」。強調在某個條件發生之前，某件事是不會被理解或發生的。",
                            "original": "Until you have a dog you don't understand...",
                            "example": "You don't know what you have until it's gone. (直到失去了，你才知道自己擁有了什麼。)"
                        },
                        {
                            "word": "Edible / Be eaten",
                            "type": "被動語態概念",
                            "explanation": "原文用 what could be eaten (什麼能被吃)。這是一種幽默的說法，暗示狗狗會吃下任何東西，包括那些人類認為「不可食用 (inedible)」的物品，如鞋子、遙控器等。",
                            "original": "...what could be eaten.",
                            "example": "Is this wild mushroom edible? (這種野生蘑菇可以吃嗎？)"
                        }
                    ]
                },
                {
                    "headline": "Funniest Tweets: \"That's you in the mirror\"",
                    "short_description": "“you ever bring ur pet up to a mirror and ur like ‘that's you’\"",
                    "image": "images/comedy_2.png",
                    "translation": "「你曾經把寵物抱到鏡子前，然後跟牠說『那就是你』嗎？」",
                    "vocab": [
                        {
                            "word": "ur like",
                            "type": "口語 / 網路用語",
                            "explanation": "這是 'you are like' 的縮寫。在口語敘述故事時，be like 不代表「像」，而是代表「說道...」或「心裡想...」。這是一種非常道地的美式口語表達。",
                            "original": "...and ur like ‘that's you’",
                            "example": "I was like, 'No way!' and he was like, 'Yes way!' (我說：「不可能！」他說：「就是這樣！」)"
                        },
                        {
                            "word": "Reflection",
                            "type": "名詞 (n.) - 延伸學習",
                            "explanation": "雖然文中用 mirror，但學習點是 Reflection (倒影、映像)。寵物通常認不出鏡中的倒影是自己 (Self-recognition)。",
                            "original": "(Concept related to mirror)",
                            "example": "He admired his reflection in the shop window. (他欣賞著櫥窗裡自己的倒影。)"
                        }
                    ]
                },
                {
                    "headline": "Petition to stop ringing doorbell on TV",
                    "short_description": "\"Petition to stop ringing the doorbell on TV so my dog can lead a less confusing life\"",
                    "image": "images/comedy_3.png",
                    "translation": "「請願停止在電視上播門鈴聲，讓我家的狗能過上比較不困惑的生活。」",
                    "vocab": [
                        {
                            "word": "Petition",
                            "type": "名詞 (n.)",
                            "explanation": "意思是「請願書」或「連署」。通常是為了改變某項政策或表達群體訴求。也可以當動詞用。",
                            "original": "Petition to stop ringing...",
                            "example": "They signed a petition to save the local park. (他們簽署了一份請願書以拯救當地的公園。)"
                        },
                        {
                            "word": "Lead a ... life",
                            "type": "搭配詞 (Collocation)",
                            "explanation": "意思是「過著...的生活」。Lead 在這裡是「引導」、「過（生活）」的意思，而不是「領導」。",
                            "original": "...so my dog can lead a less confusing life",
                            "example": "He wants to lead a quiet life in the countryside. (他想在鄉下過平靜的生活。)"
                        }
                    ]
                }
            ]
        },
        "PARENTING": {
            "cover": "images/cat_parenting.png",
            "articles": [
                {
                    "headline": "Funniest Tweets From Parents: The Toothpaste Incident",
                    "short_description": "\"Accidentally put grown-up toothpaste on my toddler’s toothbrush and he screamed like I was cleaning his teeth with a Carolina Reaper dipped in Tabasco sauce.\"",
                    "image": "images/parenting_1.png",
                    "translation": "「不小心把成人牙膏擠到幼兒牙刷上，他尖叫得像是我在用蘸了塔巴斯科辣醬的死神辣椒幫他刷牙。」",
                    "vocab": [
                        {
                            "word": "Accidentally",
                            "type": "副詞 (adv.)",
                            "explanation": "意思是「意外地」、「不小心」。相反詞是 Deliberately (故意地) 或 On purpose。",
                            "original": "Accidentally put grown-up toothpaste...",
                            "example": "I accidentally deleted the file. (我不小心刪除了那個檔案。)"
                        },
                        {
                            "word": "Scream like...",
                            "type": "譬喻修辭 (Simile)",
                            "explanation": "這裡使用了誇飾法 (Hyperbole)。Scream 是尖叫。作者用「死神辣椒(Carolina Reaper)」來比喻幼兒對薄荷味牙膏的過度反應，產生幽默感。",
                            "original": "...he screamed like I was cleaning his teeth with a Carolina Reaper...",
                            "example": "She screamed like she had seen a ghost. (她尖叫得像是見鬼了一樣。)"
                        }
                    ]
                },
                {
                    "headline": "Should You Freeze-Dry Your Breast Milk?",
                    "short_description": "If your freezer is overflowing, or you're tired of carrying around ice packs and bottles of pumped milk, this option could be for you.",
                    "image": "images/parenting_2.png",
                    "translation": "如果你的冷凍庫爆滿了，或者你厭倦了隨身攜帶冰袋和瓶裝母乳，這個選項可能適合你。",
                    "vocab": [
                        {
                            "word": "Overflowing",
                            "type": "形容詞 (adj.) / 現在分詞",
                            "explanation": "意思是「溢出的」、「氾濫的」或「爆滿的」。來自 Overflow (流出來)。",
                            "original": "If your freezer is overflowing...",
                            "example": "The hospital is overflowing with patients. (醫院裡擠滿了病人。)"
                        },
                        {
                            "word": "Freeze-Dry",
                            "type": "動詞 (v.)",
                            "explanation": "意思是「冷凍乾燥」。這是一種特殊的保存技術，先冷凍再抽真空去除水分。常用於太空食品或保存母乳。",
                            "original": "Should You Freeze-Dry Your Breast Milk?",
                            "example": "Freeze-dried fruit is a healthy snack. (凍乾水果是一種健康的零食。)"
                        }
                    ]
                },
                {
                    "headline": "Breastfeeding Condition: D-MER",
                    "short_description": "Moms with dysphoric milk-ejection reflex (D-MER) feel an intense but brief wave of depression, anxiety or other negative emotion before letdown.",
                    "image": "images/parenting_3.png",
                    "translation": "患有「不快溢乳反射」(D-MER) 的媽媽在噴乳反射前會感到強烈但短暫的憂鬱、焦慮或其他負面情緒。",
                    "vocab": [
                        {
                            "word": "Intense",
                            "type": "形容詞 (adj.)",
                            "explanation": "意思是「強烈的」、「劇烈的」或「熱切的」。可以用來形容情感、痛楚、光線或競爭。",
                            "original": "...feel an intense but brief wave...",
                            "example": "The heat was intense. (熱度非常強烈。)"
                        },
                        {
                            "word": "A wave of",
                            "type": "量詞 / 譬喻",
                            "explanation": "意思是「一陣...」、「一股...（情緒）」。用海浪來比喻情緒突然襲來且勢不可擋。",
                            "original": "...wave of depression, anxiety...",
                            "example": "A wave of panic swept over him. (一陣恐慌席捲了他。)"
                        }
                    ]
                }
            ]
        }
    }

# --- 2. 輔助工具 ---

def get_image_path(path):
    if os.path.exists(path):
        return path
    else:
        filename = path.split('/')[-1]
        return f"https://placehold.co/800x400/EEE/31343C?text={filename}+Missing"

# --- 3. Streamlit GUI (Single Page Application Logic) ---

st.set_page_config(layout="wide", page_title="News Lingo Pro")

# 初始化 Session State 用於頁面導航
if 'current_view' not in st.session_state:
    st.session_state['current_view'] = 'list' # 預設顯示列表
if 'selected_article' not in st.session_state:
    st.session_state['selected_article'] = None
if 'selected_category' not in st.session_state:
    st.session_state['selected_category'] = "U.S. NEWS" # 預設分類

# 載入資料
data = load_rich_data()

# ==========================================
#  VIEW 1: 列表頁面 (List View)
# ==========================================
if st.session_state['current_view'] == 'list':
    
    # [Sidebar] 分類選擇
    st.sidebar.title("📚 News Lingo")
    st.sidebar.caption("English Learning App")
    
    # 讓 Sidebar 改變時直接更新 selected_category
    new_cat = st.sidebar.radio(
        "選擇分類", 
        list(data.keys()), 
        index=list(data.keys()).index(st.session_state['selected_category'])
    )
    st.session_state['selected_category'] = new_cat
    
    # [Main] 取得當前分類資料
    cat_data = data[st.session_state['selected_category']]
    
    # 分類封面 (使用 use_container_width 修復 Warning)
    st.image(get_image_path(cat_data['cover']), use_container_width=True)
    st.title(f"📂 {st.session_state['selected_category']}")
    st.markdown("---")
    
    # 文章列表
    for idx, article in enumerate(cat_data['articles']):
        with st.container():
            col1, col2 = st.columns([1, 2])
            
            with col1:
                st.image(get_image_path(article['image']), use_container_width=True)
            
            with col2:
                st.subheader(article['headline'])
                st.caption(article['short_description'][:100] + "...")
                
                # 點擊按鈕 -> 切換 View 到 'detail'
                # 使用 key 確保按鈕唯一性
                if st.button("👉 開始深入學習 (Start Learning)", key=f"btn_{idx}"):
                    st.session_state['selected_article'] = article
                    st.session_state['current_view'] = 'detail'
                    st.rerun() # 強制重新執行以切換畫面
        
        st.markdown("---")

# ==========================================
#  VIEW 2: 學習詳情頁面 (Detail View)
# ==========================================
elif st.session_state['current_view'] == 'detail':
    article = st.session_state['selected_article']
    
    # [Top Bar] 返回按鈕
    if st.button("⬅️ 返回文章列表 (Back to List)"):
        st.session_state['current_view'] = 'list'
        st.session_state['selected_article'] = None
        st.rerun()
        
    st.markdown("---")
    
    # 兩欄佈局：左側大圖，右側標題與翻譯
    col_hero, col_info = st.columns([1, 1])
    
    with col_hero:
        st.image(get_image_path(article['image']), use_container_width=True)
        
    with col_info:
        st.title(article['headline'])
        st.markdown("### 📝 簡介與翻譯")
        st.info(f"**原文：** {article['short_description']}")
        st.success(f"**中文：** {article['translation']}")

    st.markdown("---")
    st.header("🔑 核心詞彙與片語學習 (Key Vocabulary)")
    
    # 遍歷豐富的單字卡內容
    for v in article['vocab']:
        # 使用容器把它包起來，讓視覺更像一張卡片
        with st.container():
            st.markdown(f"#### 📌 {v['word']}")
            st.caption(f"詞性：{v['type']}")
            
            # A. 詞彙解釋
            st.markdown("**A. 詞彙解釋：**")
            st.write(v['explanation'])
            
            # B. 來自原文
            st.markdown("**B. 來自原文的句子：**")
            st.code(v['original'], language="text")
            
            # C. 額外例句
            st.markdown("**C. 額外例句：**")
            st.write(f"> *{v['example']}*")
            
            st.divider() # 分隔線
            
    # 底部再次提供返回按鈕，方便操作
    if st.button("⬅️ 完成學習，返回列表", key="btn_bottom_back"):
        st.session_state['current_view'] = 'list'
        st.rerun()