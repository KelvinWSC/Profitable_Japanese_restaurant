import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def filter_district(address):
    return address.split(",")[-1].strip()

df = pd.read_csv("openrice.csv")
df = df.drop_duplicates(["res_id"]).reset_index(drop=True)
df = df[df["review"] > 5] 

df["district"] = df["address"].apply(filter_district)

counts = df["district"].value_counts().rename("counts")
means = df.groupby("district")[["likes","dislikes","bookmarks","review"]].mean()
japan = means.join(counts)
japan["like_percetage"] = japan["likes"]/(japan["likes"] + japan["dislikes"])
japan["popularity"] = japan["like_percetage"]*japan["bookmarks"]
japan = japan.sort_values(by="popularity")
fig,ax = plt.subplots(figsize=(12,6))
ax.barh(japan.index, japan["popularity"],color="navy")
# ax.bar(japan.index, japan["popularity"])
ax.set_xlabel('Popularity')
ax.set_ylabel('District')
plt.tight_layout()
plt.show()
