
import spacy
from src.config import OUTPUT_DIR

nlp = spacy.load(OUTPUT_DIR)

def predict(text):
    doc = nlp(text)
    return [(ent.text, ent.label_) for ent in doc.ents]

if __name__ == "__main__":
    text = input("Enter product title: ")
    results = predict(text)
    
    for entity, label in results:
        print(f"{entity} -> {label}")