#!/bin/bash
scriptdir=`dirname $0`

java -mx500m -cp "$scriptdir/stanford-ner.jar:$scriptdir/lib/*" edu.stanford.nlp.ie.crf.CRFClassifier -loadClassifier "$scriptdir/classifiers/english.all.3class.distsim.crf.ser.gz" -textFile /workspaces/Assessed-task-1-/$1 -outputFormat tsv
