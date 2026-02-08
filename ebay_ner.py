import spacy
from spacy.training.example import Example
import random

# 1. Blank German model
nlp = spacy.blank("de")

# 2. Add NER pipeline
ner = nlp.add_pipe("ner")

# 3. Define labels
LABELS = ["CAR_BRAND", "CAR_MODEL", "PART_NAME", "MANUFACTURER"]

for label in LABELS:
    ner.add_label(label)

# 4. Training data
TRAIN_DATA = [
    ("BMW 320d Ölfilter von Mann", {
        "entities": [
            (0, 3, "CAR_BRAND"),
            (4, 8, "CAR_MODEL"),
            (9, 17, "PART_NAME"),
            (22, 26, "MANUFACTURER")
        ]
    }),
    ("Audi A4 Bremsbeläge Bosch", {
        "entities": [
            (0, 4, "CAR_BRAND"),
            (5, 7, "CAR_MODEL"),
            (8, 19, "PART_NAME"),
            (20, 25, "MANUFACTURER")
        ]
    }),
    ("Mercedes C200 Luftfilter von Mahle", {
        "entities": [
            (0, 8, "CAR_BRAND"),
            (9, 13, "CAR_MODEL"),
            (14, 24, "PART_NAME"),
            (29, 34, "MANUFACTURER")
        ]
    })
]

# 5. Disable other pipelines
optimizer = nlp.initialize()

# 6. Training loop
for epoch in range(8):
    random.shuffle(TRAIN_DATA)
    losses = {}

    for text, annotations in TRAIN_DATA:
        example = Example.from_dict(nlp.make_doc(text), annotations)
        nlp.update([example], losses=losses)

    print(f"Epoch {epoch+1}, Losses: {losses}")

# 7. Test the trained model
print("\n--- Model Test ---")
test_text = "BMW 320d Ölfilter von Mann"
doc = nlp(test_text)

for ent in doc.ents:
    print(ent.text, "->", ent.label_)