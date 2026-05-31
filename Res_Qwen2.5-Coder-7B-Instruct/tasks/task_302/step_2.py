import spacy

# Step 2: Load a pre-trained model for named entity recognition
nlp = spacy.load("en_core_web_sm")

# Initialize a dictionary to store entity counts
entity_inventory = {}

# Process each text file and count entities
for file_path in text_files:
    with open(file_path, 'r', encoding='utf-8') as file:
        doc = nlp(file.read())
        for ent in doc.ents:
            if ent.label_ in ['DATE', 'EMAIL', 'URL', 'CARDINAL']:
                if ent.text not in entity_inventory:
                    entity_inventory[ent.text] = 0
                entity_inventory[ent.text] += 1

print(f"Processed {len(text_files)} text files and identified {len(entity_inventory)} unique entities.")