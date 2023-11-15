import spacy
# Load the English NLP model
nlp = spacy.load("en_core_web_sm")
# Text data to extract information from
text = """
Apple Inc. is an American multinational technology company headquartered in Cupertino, California.
It was founded by Steve Jobs, Steve Wozniak, and Ronald Wayne in 1976.
Apple designs, manufactures, and markets consumer electronics, computer software, and online services.
"""
# Process the text with spaCy
doc = nlp(text)
# Extract named entities (e.g., organizations, persons, locations)
for entity in doc.ents:
    print(f"Entity: {entity.text}, Label: {entity.label_}")
# Extract specific information
found_keywords = []
for token in doc:
    if token.text.lower() == "founded":
        found_keywords.append(token)
if found_keywords:
    # Assuming we want to extract the organization's founding details
    organization = None
    for ent in found_keywords[0].head.children:
        if ent.ent_type_ == "ORG":
            organization = ent.text
    if organization:
        print(f"{organization} was founded by:")
        for child in found_keywords[0].children:
            if child.ent_type_ == "PERSON":
                print(child.text)

#OUTPUT
'''
Entity: Apple Inc., Label: ORG
Entity: American, Label: NORP
Entity: Cupertino, Label: GPE
Entity: California, Label: GPE
Entity: Steve Jobs, Label: PERSON
Entity: Steve Wozniak, Label: PERSON
Entity: Ronald Wayne, Label: PERSON
Entity: 1976, Label: DATE
Entity: Apple, Label: ORG
'''
