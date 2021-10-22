from PyPDF2 import PdfFileMerger
from os import listdir
from os.path import isfile, join

#gets the pdfs from the files folder
pdfs = listdir('files')

print("Unsorted: ")
print(pdfs)

#gets the numbers at the start of the title with its original array index
numbers = []
for i in range(0, len(pdfs)):
    temp = "";
    for d in range(0, len(pdfs[i])):
        if(ord(pdfs[i][d]) < 48 or ord(pdfs[i][d]) > 57):
            break
        temp += pdfs[i][d]
    numbers.append([int(temp), i])

#sorts the numbers
for lI in range(1, len(numbers)):
    for blI in range(lI-1, -1, -1):
        if numbers[blI + 1][0] < numbers[blI][0]:
            temp = numbers[blI + 1]
            numbers[blI + 1] = numbers[blI]
            numbers[blI] = temp

#using the indexes saved in the sorted "numbers" to create an array with the sorted file names
doc = []
for i in range(0, len(numbers)):
    doc.append(pdfs[numbers[i][1]])

print("Sorted: ")
print(doc)

for x in range(len(doc)):
    doc[x] = 'files\\' + doc[x]

merger = PdfFileMerger()

for pdf in doc:
    merger.append(pdf)

merger.write("result.pdf")
merger.close()

