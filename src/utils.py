
def print_entities(doc):
    for ent in doc.ents:
        print(f"Text: {ent.text}")
        print(f"Label: {ent.label_}")
        print(f"Start: {ent.start_char}")
        print(f"End: {ent.end_char}")
        print("-" * 20)