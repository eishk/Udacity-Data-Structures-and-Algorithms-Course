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

calls_caller = set()
calls_called = set()
texts_texter = set()
texts_texted = set()

for text in texts:
    texts_texter.add(text[0])
    texts_texted.add(text[1])

for call in calls:
    calls_caller.add(call[0])
    calls_called.add(call[1])
list = []
for call in calls_caller:
    if (call not in calls_called and call not in texts_texted and call not in texts_texter):
        list.append(call)
list.sort()
print("These numbers could be telemarketers: ")
for l in list:
    print(l)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""
