
import pandas as pd
import ast

def load_data(path):
    df = pd.read_csv(path)
    data = []
    
    for _, row in df.iterrows():
        text = row["text"]
        entities = ast.literal_eval(row["entities"])
        data.append((text, {"entities": entities}))
    
    return data