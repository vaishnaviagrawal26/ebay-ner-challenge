# eBay ML Challenge – Named Entity Recognition (NER)

This project implements a Named Entity Recognition (NER) model using spaCy to extract structured information from German e-commerce product titles.

Example  
```
BMW 320d Ölfilter von Mann
```

Output  
- BMW → CAR_BRAND  
- 320d → CAR_MODEL  
- Ölfilter → PART_NAME  
- Mann → MANUFACTURER  

---

## Tech Stack
- Python  
- spaCy 3.7.2  
- NLP (German)

---

## Entities
- CAR_BRAND  
- CAR_MODEL  
- PART_NAME  
- MANUFACTURER  

---

## How to Run
```
pip install -r requirements.txt
python train_ner.py
python test_german.py
```

---

## Notes
- Uses a custom German NER model  
- Training data is manually annotated  

---

## Author
Vaishnavi