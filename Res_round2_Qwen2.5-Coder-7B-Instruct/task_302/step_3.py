import spacy

nlp = spacy.load("en_core_web_sm")

entity_types = {
    "DATE": [],
    "EMAIL": [],
    "URL": [],
    "CARDINAL": []
}

for file in text_files:
    with open(file, 'r') as f:
        text = f.read()
        doc = nlp(text)
        
        for ent in doc.ents:
            if ent.label_ in entity_types:
                entity_types[ent.label_].append(ent.text)

print(entity_types)