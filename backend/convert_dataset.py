import pandas as pd

rows = []

with open("dataset/SMSSpamCollection", "r", encoding="utf-8") as file:
    for line in file:
        parts = line.split("\t", 1)

        if len(parts) == 2:
            label, message = parts
            rows.append([label, message.strip()])

df = pd.DataFrame(rows, columns=["label", "message"])

df.to_csv("dataset/spam.csv", index=False)

print("spam.csv created successfully")
print(df.head())