#!/bin/bash

# Define the absolute path to the Stanford NER directory
NER_DIR="/workspaces/Assessed-task-1-/stanford_ner/stanford-ner-2020-11-17"

# Input files
WIKIPEDIA_INPUT="wikipedia.txt"
FANWIKI_INPUT="fanwiki.txt"

# Output files
WIKIPEDIA_OUTPUT="stanford-wikipedia.txt"
FANWIKI_OUTPUT="stanford-fanwiki.txt"

# Run the Stanford NER on wikipedia.txt
bash "$NER_DIR/ner.sh" $WIKIPEDIA_INPUT > $WIKIPEDIA_OUTPUT

# Run the Stanford NER on fanwiki.txt
bash "$NER_DIR/ner.sh" $FANWIKI_INPUT > $FANWIKI_OUTPUT

echo "NER tagging completed. Outputs saved to $WIKIPEDIA_OUTPUT and $FANWIKI_OUTPUT."
