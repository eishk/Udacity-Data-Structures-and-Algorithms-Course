"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

ultimate_dict = {}
for call in calls:
    phones = []
    phones.append(call[0])
    phones.append(call[1])
    time = call[3]
    time = int(time)
    for phone in phones:
        ultimate_dict[phone] = ultimate_dict.get(phone,0) + time

max_number = max(ultimate_dict, key = ultimate_dict.get)
max_seconds = ultimate_dict[max_number]


print(max_number + " spent the longest time, " + str(max_seconds) + " seconds, on the phone" +
" during September 2016.")



"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during
September 2016.".
"""
