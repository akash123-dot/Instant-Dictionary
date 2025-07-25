import pandas as pd
import os

file = os.path.join("app", "data.csv")
class Dictionary:
    def __init__(self, term):
        self.term = term

    def GetData(self):
        df = pd.read_csv(file)
        term = self.term.lower().strip()
        data = df[df["word"].str.lower() == term]

        if data.empty:
            return ["No definition found."]
        else:
            return data["definition"].to_list()