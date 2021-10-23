from PyPDF2 import PdfFileMerger
from os import listdir
from os.path import isfile, join

#gets the pdfs from the files folder
pdfs = listdir('files')

#prints the unsorted array
print("Unsorted: ")
print(pdfs)

#gets the numbers at the start of the title with its original array index
numbers = []
for i in range(0, len(pdfs)):
    tempNumber = "";
    for d in range(0, len(pdfs[i])):
        #if the character is not a digit 0 to 9 break 
        if(ord(pdfs[i][d]) < 48 or ord(pdfs[i][d]) > 57):
            break
        tempNumber += pdfs[i][d]
    numbers.append([int(tempNumber), i])

#sorts the numbers
for lI in range(1, len(numbers)):
#change the loop below so that instead of checking all already sorted elements
#it repeatedly splits the sorted portion of the array in half until there is a 
#blI less than or equal to and a blI + 1 greater or equal to.
    for blI in range(lI-1, -1, -1):
        if numbers[blI + 1][0] < numbers[blI][0]:
            holder = numbers[blI + 1]
            numbers[blI + 1] = numbers[blI]
            numbers[blI] = holder

#using the indexes saved in the sorted "numbers" to create an array with the sorted file names
doc = []
for i in range(0, len(numbers)):
    doc.append(pdfs[numbers[i][1]])

#prints the sorted array
print("Sorted: ")
print(doc)

for x in range(len(doc)):
    doc[x] = 'files\\' + doc[x]

merger = PdfFileMerger()

for pdf in doc:
    merger.append(pdf)

merger.write("result.pdf")
merger.close()

