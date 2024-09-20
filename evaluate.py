import sys
from sklearn.metrics import precision_recall_fscore_support

def load_data(file_path):
    data = []
    with open(file_path, 'r') as f:
        for line in f:
            if line.strip():
                token, label = line.split()
                data.append(label)
    return data

def evaluate(ner_output, gold_standard):
    y_pred = load_data(ner_output)
    y_true = load_data(gold_standard)

    if len(y_pred) != len(y_true):
        print("Error: Files have different lengths!")
        sys.exit(1)

    precision, recall, f1, _ = precision_recall_fscore_support(y_true, y_pred, average='weighted')

    print(f"Precision: {precision:.2f}")
    print(f"Recall: {recall:.2f}")
    print(f"F1-Score: {f1:.2f}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 evaluate.py <ner-output-file> <gold-standard-file>")
        sys.exit(1)

    ner_output_file = sys.argv[1]
    gold_standard_file = sys.argv[2]

    evaluate(ner_output_file, gold_standard_file)
