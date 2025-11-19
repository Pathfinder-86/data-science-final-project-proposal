import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules
from tqdm.auto import tqdm

MIN_SUPPORT = 0.002 # time rquired: 0.002 < 30sec
MIN_THRESHOLD = 0.5
OUTPUT_PATH = "association_rules.csv"

tqdm.pandas()
df = pd.read_csv("Dataset_clean.csv")

df = df[["category", "authors"]]
print("Association rule target:", df.columns)
print("# of data:", len(df))
print("Example:\n", df.head(2), "\n", "." * 35)

transactions = []

for _, row in tqdm(df.iterrows(), total=len(df), desc="Building transactions"):
    category = str(row["category"]).strip()
    if not category:
        continue
    
    cat_item = f"category:{category}"
    
    authors_raw = str(row["authors"])
    authors_split = [a.strip() for a in authors_raw.split(",") if a.strip()]
    
    if not authors_split:
        continue
    
    author_items = [f"author:{a}" for a in authors_split]
    
    items = [cat_item] + author_items
    transactions.append(items)

print("# of transactions:", len(transactions))
print("Finding association rules")

te = TransactionEncoder()
te_array = te.fit(transactions).transform(transactions)
basket = pd.DataFrame(te_array, columns=te.columns_)
freq_itemsets = apriori(basket, min_support=MIN_SUPPORT, use_colnames=True)

print("frequent itemsets:", len(freq_itemsets))
print(freq_itemsets.sort_values("support", ascending=False))

rules = association_rules(freq_itemsets, metric="confidence", min_threshold=MIN_THRESHOLD)

print("# of rules:", len(rules))
print(rules.head())

def is_author_to_category(row):
    ants = row["antecedents"]
    cons = row["consequents"]
    
    if len(cons) != 1:
        return False
    if not list(cons)[0].startswith("category:"):
        return False
    
    for item in ants:
        if not item.startswith("author:"):
            return False
    return True

rules_ac = rules[rules.apply(is_author_to_category, axis=1)].copy()

print("Author -> Category:", len(rules_ac))

rules_ac = rules_ac.sort_values(["confidence", "lift"], ascending=False)

def set_to_str(s):
    return ", ".join(sorted(list(s)))

rules_ac["antecedents_str"] = rules_ac["antecedents"].apply(set_to_str)
rules_ac["consequents_str"] = rules_ac["consequents"].apply(set_to_str)

cols_show = ["antecedents_str", "consequents_str", "support", "confidence", "lift"]

print(rules_ac[cols_show].head().to_string(index=False))

rules_ac[cols_show].to_csv(OUTPUT_PATH, index=False, encoding="utf-8-sig")
print(f"Association rules saved as CSV：{OUTPUT_PATH}")