def locate_card(cards, query):
    # Create a variable position with the value 0
    position = 0

    # Set up a loop for repetition
    while True:

        # Check if element at the current position matche the query
        if cards[position] == query:
            # Answer found! Return and exit..
            return position

        # Increment the position
        position += 1

        # Check if we have reached the end of the array
        if position == len(cards):
            # Number not found, return -1
            return -1

def test_result(dict):
    result = locate_card(dict['input']['cards'],dict['input']['query'])
    if result==dict['output']:
        print ('Pass')
    else:
        print(f"FAILED FOR BELOW : result is {result} whereas expected {dict['output']}")
        print (f"cards are {dict['input']['cards']} and query is {dict['input']['query']}")
    pass

#test Case:

# 1. Query is somewhere in the almost middle
test = {'input':{'cards':[12,9,7,6,5,4,1],'query':6},
        'output':3}
tests =[]
tests.append(test)

# 2. Query is first element in the cards
tests.append({'input':{'cards':[12,9,7,6,5,4,1],'query':12},
        'output':0})
# 3. Query is last element in the cards
tests.append({'input':{'cards':[12,9,7,6,5,4,1],'query':1},
        'output':6})
# 4. Query is almost last element in the cards
tests.append({'input':{'cards':[12,9,7,6,5,4,1],'query':4},
        'output':5})

# 5. Query is more than one time  in the list - expected : return the first occurance
tests.append({'input':{'cards':[12,9,9,7,6,6,5,4,1],'query':6},
        'output':4})

# 6. List is negative numbers and positive number mixed
tests.append({'input':{'cards':[12,9,7,6,5,4,1,-2,-18,-20],'query':-18},
        'output':8})

# 7. Query is not in the list - expected : return -1

tests.append({'input':{'cards':[12,9,9,7,6,6,5,4,1],'query':5},
        'output':6})

# 8. List is empty i.e. there is no cards available  - expected : -2
tests.append({'input':{'cards':[12,9,9,7,6,6,5,4,1],'query':None},
        'output':-1})

# lst=[12,9,7,6,6,5,4,1]
# print(f'The position is {locate_cards(lst,2)}')
# print(test)
# result = locate_card(test['input']['cards'],test['input']['query'])
# print(result)

for x in tests:
    test_result(x)