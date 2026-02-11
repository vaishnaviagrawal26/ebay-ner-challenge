import streamlit as st
import spacy

nlp = spacy.load("models/ner_model")

st.title("German E-commerce NER Demo")

text = st.text_input("Enter product title:")

if text:
    doc = nlp(text)

    for ent in doc.ents:
        st.write(f"{ent.text} → {ent.label_}")