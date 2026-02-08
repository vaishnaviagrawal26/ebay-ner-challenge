import spacy

nlp = spacy.load("de_core_news_sm")

text = "BMW x5 Bremsbelag Bosch vorne"
doc = nlp(text)

print("Text:", text)
print("Entities found:")
for ent in doc.ents:
    print(ent.text, "->", ent.label_)