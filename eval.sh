#!/bin/bash

# Ensure that two arguments are provided
if [ "$#" -ne 2 ]; then
    echo "Usage: ./eval.sh <ner-output-file> <gold-standard-file>"
    exit 1
fi

# Define directories
NER_DIR="/workspaces/Assessed-task-1-/stanford_ner/stanford-ner-2020-11-17"
GOLD_DIR="/workspaces/Assessed-task-1-"
OUTPUT_DIR="/workspaces/Assessed-task-1-"

# Define input files with full paths
NER_OUTPUT="$NER_DIR/$1"
GOLD_STANDARD="$GOLD_DIR/$2"

# Output file should be in the OUTPUT_DIR
EVAL_OUTPUT="$OUTPUT_DIR/${1%.tsv}-eval.txt"

# Run evaluation script (assuming you have a Python script to compute metrics)
python3 evaluate.py "$NER_OUTPUT" "$GOLD_STANDARD" > "$EVAL_OUTPUT"

echo "Evaluation complete. Results saved to $EVAL_OUTPUT"
