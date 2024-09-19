import re

def extract_entities(input_file, output_file):
    entities = []

    # Read the input file
    with open(input_file, 'r') as f:
        for line in f:
            # Split each word and its NER tag (e.g., Barack/PERSON)
            tokens = line.split()
            for token in tokens:
                # Look for words tagged with NER labels (e.g., /PERSON, /LOCATION)
                match = re.search(r'/([A-Z]+)$', token)
                if match:
                    entity = token.split('/')[0]  # Extract the word before the tag
                    entities.append(entity)

    # Write the extracted entities to the output file
    with open(output_file, 'w') as f:
        for entity in entities:
            f.write(entity + '\n')

# Extract entities from both output files
extract_entities('stanford-wikipedia.txt', 'ner-list-wikipedia.txt')
extract_entities('stanford-fanwiki.txt', 'ner-list-fanwiki.txt')

print("NER extraction completed. Lists saved in ner-list-wikipedia.txt and ner-list-fanwiki.txt.")
