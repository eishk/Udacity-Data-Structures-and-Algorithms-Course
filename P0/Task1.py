"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

telephone_book = set()

for text in texts:
    phone1 = text[0]
    telephone_book.add(phone1)
    phone2 = text[1]
    telephone_book.add(phone2)

for call in calls:
    phone1 = call[0]
    telephone_book.add(phone1)
    phone2 = call[1]
    telephone_book.add(phone2)

print("There are " + str(len(telephone_book)) + " different telephone numbers" +
      " in the records.")

"""
TASK 1:
How many different telephone numbers are there in the records?
Print a message:
"There are <count> different telephone numbers in the records."
"""
