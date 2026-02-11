
import spacy
import random
from spacy.training.example import Example
from spacy.util import minibatch
from sklearn.model_selection import train_test_split
from src.config import *
from src.data_loader import load_data

def train_model():

    random.seed(RANDOM_SEED)

    nlp = spacy.blank(MODEL_LANG)
    ner = nlp.add_pipe("ner")

    for label in LABELS:
        ner.add_label(label)

    data = load_data("data/train.csv")

    train_data, val_data = train_test_split(
        data, test_size=0.2, random_state=RANDOM_SEED
    )

    optimizer = nlp.initialize()

    for epoch in range(EPOCHS):
        random.shuffle(train_data)
        losses = {}

        batches = minibatch(train_data, size=BATCH_SIZE)

        for batch in batches:
            examples = []
            for text, annotations in batch:
                doc = nlp.make_doc(text)
                example = Example.from_dict(doc, annotations)
                examples.append(example)

            nlp.update(examples, drop=0.3, losses=losses)

        print(f"Epoch {epoch+1}/{EPOCHS} — Loss: {losses}")

    nlp.to_disk(OUTPUT_DIR)
    print("Model saved successfully.")

if __name__ == "__main__":
    train_model()