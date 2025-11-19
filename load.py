'''
Author: Capra Chu
Date: 2025/11/19

Functions:
1. Convert Dataset.json to .csv 
2. Data cleaning (emoji, empty string, meaningless subtitle...)
'''

import pandas as pd
import re

WORD_BOUNDARY = 5 # larger => longer short_description (subtitle) will be kept uwu

emoji_filter = re.compile(
    "["
    u"\U0001F300-\U0001F5FF"
    u"\U0001F600-\U0001F64F"
    u"\U0001F680-\U0001F6FF"
    u"\U0001F700-\U0001F77F"
    u"\U0001F780-\U0001F7FF"
    u"\U0001F800-\U0001F8FF"
    u"\U0001F900-\U0001F9FF"
    u"\U0001FA00-\U0001FA6F"
    u"\U0001FA70-\U0001FAFF"
    u"\u2600-\u26FF" 
    u"\u2700-\u27BF"
    "]+",
    flags=re.UNICODE,
)

def has_emoji(text: str) -> bool:
    if not isinstance(text, str):
        return False
    return bool(emoji_filter.search(text))

input_path = "Dataset.json"
df = pd.read_json(input_path, lines=True)

df["has_emoji"] = df["short_description"].apply(has_emoji) # apply emoji filtering
df["is_too_short"] = (df["short_description"].str.split().str.len() < WORD_BOUNDARY)
df = df[~(df["has_emoji"]|df["is_too_short"])].copy()
df = df[["headline", "category", "authors", "short_description"]]
df = df[df["authors"].str.strip() != ""]
df = df[df["short_description"].str.strip() != ""]

df.to_csv("Dataset_clean.csv", index=False, encoding="utf-8-sig")

print("Generated cleaned dataset as: Dataset_clean.csv")
