
import spacy
from sklearn.metrics import classification_report
from src.data_loader import load_data
from src.config import OUTPUT_DIR

def evaluate():

    nlp = spacy.load(OUTPUT_DIR)
    val_data = load_data("data/val.csv")

    true_labels = []
    pred_labels = []

    for text, annotations in val_data:
        doc = nlp(text)

        true_entities = annotations["entities"]
        pred_entities = [(ent.start_char, ent.end_char, ent.label_) for ent in doc.ents]

        true_labels.extend([ent[2] for ent in true_entities])
        pred_labels.extend([ent[2] for ent in pred_entities])

    print(classification_report(true_labels, pred_labels))

if __name__ == "__main__":
    evaluate()