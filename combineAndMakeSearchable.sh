#!/bin/sh

python3 Combine.py && ocrmypdf --redo-ocr --output-type pdf result.pdf searchablePdf.pdf
