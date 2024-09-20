# Assessed-task-1-
# Named Entity Recognition (NER) Assignment

This repository holds the code and data required for completing the assignment.

## Setting up the Environment

*   This project was developed in a virtual machine (VM) environment, utilizing GitHub Codespaces.
*   Ensure that Java is installed in the VM.
*   Install Python in the VM as well.

## Installing the NER System

*   The Stanford Named Entity Recognizer (NER) system was obtained by downloading:
```bash
$ wget https://nlp.stanford.edu/software/stanford-ner-4.2.0.zip
After downloading, the file was unzipped with:
$ unzip stanford-ner-4.2.0.zip
Navigate to the Stanford NER directory and test the system using a sample file:
$ cd stanford-ner-2020-11-17
$ ./ner.sh sample.txt

** Collecting Data
Wikipedia
A Wikipedia article about the singer The Weeknd was selected.
The script extract-wikipedia.py was used to pull content from the article.
The output was saved in a file named wikipedia.txt.
Fandom
The fandom-py library was utilized to access the Fandom wiki for "Jojo's Bizarre Adventure."

Based on the last digit of the student number 47745290, the character Jonathan Joestar was chosen, as shown in the following table:

Last Digit	Character
0	Jonathan Joestar
1	Robert E. O. Speedwagon
2	Dio Brando
3	Jotaro Kujo
4	Noriaki Kakyoin
5	Jean Pierre Polnareff
6	Iggy
7	Hol Horse
8	Josuke Higashikata
9	Koichi Hirose
The script extract-fanwiki.py was used to gather the wiki content for the selected character.

This content was saved in fanwiki.txt.

** Applying NER
The stanford-ner.sh script was used to apply the Stanford NER system to both wikipedia.txt and fanwiki.txt.
The output was stored in stanford-wikipedia.txt and stanford-fanwiki.txt.

** Extracting Named Entities
The ner-list.py script was used to extract the named entities from the NER output files.
The lists of entities were saved in ner-list-wikipedia.txt and ner-list-fanwiki.txt.

** Evaluating NER
The script standard-ner.sh was used to create manually annotated gold standard versions of wikipedia.txt and fanwiki.txt.
The gold standard files were saved as wikipedia-gold.txt and fanwiki-gold.txt.
The Stanford NER system was evaluated against the gold standards using the eval.sh script and evaluate.py.
The evaluation results were saved in wikipedia-ner-output-eval.txt and fanwiki-ner-output-eval.txt.
The results, focusing on metrics like precision, recall, and F1-score, were analyzed and discussed in discussion.txt
use  this command to run evaluation:
./eval.sh fanwiki-ner-output.tsv fanwiki-gold.txt 
./eval.sh wikipedia-ner-output.tsv wikipedia-gold.txt

Fanwiki Evaluation Results
============================

CRFClassifier tagged 84 words in 5 documents at 525.25 words per second.
              precision    recall  f1-score   support

           O     1.0000    1.0000    1.0000        72
      PERSON     1.0000    1.0000    1.0000        12

    accuracy                         1.0000        84
   macro avg     1.0000    1.0000    1.0000        84
weighted avg     1.0000    1.0000    1.0000        84

         Totals 1.0000  1.0000  1.0000

** Wikipedia Evaluation Results
The CRFClassifier tagged 9399 words in 380 documents at a speed of 3682.99 words per second.

** Fanwiki Evaluation Results
The CRFClassifier tagged 52 words in 5 documents at 525.25 words per second.

Wikipedia Evaluation Results
============================

CRFClassifier tagged 10376 words in 380 documents at 3682.99 words per second.
              precision    recall  f1-score   support

    LOCATION     1.0000    1.0000    1.0000       121
           O     1.0000    1.0000    1.0000      9577
ORGANIZATION     1.0000    1.0000    1.0000       228
      PERSON     1.0000    1.0000    1.0000       450

    accuracy                         1.0000     10376
   macro avg     1.0000    1.0000    1.0000     10376
weighted avg     1.0000    1.0000    1.0000     10376

         Totals 1.0000  1.0000  1.0000

** Fixing Named Entity Errors
The fix-ner.sh script was developed to fix common errors, such as punctuation being wrongly tagged as part of an entity.
The fixed outputs were re-evaluated using the NER system and the fixed-fanwiki.txt and fixed-wikipedia.txt are the output for the fix-ner.sh output.
use  this command to run fix-ner.sh:
./fix-ner.sh stanford-fanwiki.txt fixed-fanwiki.txt
./fix-ner.sh stanford-wikipedia.txt fixed-wikipedia.txt


** Discussion
The evaluation results indicate that the Stanford NER system achieved perfect precision, recall, and F1-scores for both Wikipedia and Fanwiki texts. While the results are promising, caution should be taken due to the small dataset size and limited number of entity types. Broader evaluations are necessary to gain a comprehensive understanding of the system's capabilities.

** AI Tools Utilized
Tool: chatGPT
Assisted in creating boilerplate code for extract-wikipedia.py and extract-fanwiki.py.
