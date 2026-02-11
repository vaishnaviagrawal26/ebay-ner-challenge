import streamlit as st
import spacy

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Product Title Intelligence",
    layout="wide"
)

# ---------------- LOAD MODEL ----------------
nlp = spacy.load("models/ner_model")

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>

/* Global */
html, body, [class*="css"] {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
}

.stApp {
    background-color: #ffffff;
    color: #000000;
}

/* Header Section */
.header-container {
    background-color: #1b263b;
    padding: 35px 20px;
    border-radius: 10px;
    margin-bottom: 30px;
    text-align: center;
}

.header-title {
    font-size: 42px;
    font-weight: 600;
    color: #ffffff;
}

.header-sub {
    font-size: 18px;
    color: #e5e5e5;
    margin-top: 5px;
}

/* Section Titles */
.section-title {
    font-size: 22px;
    font-weight: 600;
    margin-top: 20px;
    margin-bottom: 10px;
}

/* Entity Result */
.entity-box {
    background-color: #e5e5e5;
    padding: 12px 18px;
    border-left: 5px solid #fca311;
    margin-bottom: 10px;
    font-size: 16px;
}

/* Button */
.stButton>button {
    background-color: #fca311;
    color: #000000;
    border-radius: 6px;
    height: 2.8em;
    font-weight: 500;
    border: none;
}

.stButton>button:hover {
    background-color: #e59400;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #778da9;
    color: white;
}

section[data-testid="stSidebar"] * {
    color: white !important;
}

</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown("""
<div class="header-container">
    <div class="header-title">Product Title Intelligence</div>
    <div class="header-sub">AI-powered Structured Entity Extraction for E-commerce</div>
</div>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ----------------
st.sidebar.title("Navigation")
page = st.sidebar.radio("", ["Overview", "Entity Extraction", "System Details"])

# ---------------- OVERVIEW ----------------
if page == "Overview":
    st.markdown("<div class='section-title'>Problem</div>", unsafe_allow_html=True)
    st.write("""
    E-commerce product titles are often unstructured and inconsistent.
    Extracting structured attributes such as brand, model, part name,
    and manufacturer improves search quality and catalog intelligence.
    """)

    st.markdown("<div class='section-title'>Solution</div>", unsafe_allow_html=True)
    st.write("""
    This system uses a custom-trained spaCy Named Entity Recognition (NER)
    pipeline to extract domain-specific entities from German automotive product titles.
    """)

# ---------------- ENTITY EXTRACTION ----------------
elif page == "Entity Extraction":

    st.markdown("<div class='section-title'>Run Entity Extraction</div>", unsafe_allow_html=True)

    title_input = st.text_input(
        "Enter Product Title",
        "BMW 320d Ölfilter von Mann"
    )

    if st.button("Extract Entities"):

        doc = nlp(title_input)

        if len(doc.ents) == 0:
            st.warning("No entities detected.")
        else:
            for ent in doc.ents:
                st.markdown(
                    f"<div class='entity-box'>"
                    f"<strong>{ent.text}</strong> — {ent.label_}"
                    f"</div>",
                    unsafe_allow_html=True
                )

# ---------------- SYSTEM DETAILS ----------------
elif page == "System Details":

    st.markdown("<div class='section-title'>Technology Stack</div>", unsafe_allow_html=True)
    st.write("""
    • Python  
    • spaCy (Custom NER Model)  
    • Streamlit  
    """)

    st.markdown("<div class='section-title'>Use Case</div>", unsafe_allow_html=True)
    st.write("""
    Designed for automotive e-commerce platforms requiring
    structured extraction from unstructured product titles.
    """)

st.markdown("---")
st.caption("Product Title Intelligence System")