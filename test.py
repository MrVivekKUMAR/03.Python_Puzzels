def locateCards(cards, query):
    position = 0

    for x in cards:
        if x==cards[position]:
            break
        position+=1
    return position

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
        'output':1})
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
        'output':-1})

# 8. List is empty i.e. there is no cards available  - expected : -2
tests.append({'input':{'cards':[12,9,9,7,6,6,5,4,1],'query':None},
        'output':-2})



print(tests)