import json

data = json.load(open("./data.json"))

lookup = ''
while lookup != 'q':
    lookup = input("Please enter a word(q will quit): ")
    if lookup in data:
        print(data[lookup])
    else:
        print('That is not a word, please try again!')