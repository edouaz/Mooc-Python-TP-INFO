def substitue(message, abreviation):
    to_ret = []
    for words in message.split():
        if words in abreviation:
            to_ret.append(abreviation[words])
        else:
            to_ret.append(words)
    return ' '.join(to_ret)


## Test 
print(substitue('C. N. cpt 2 to inf', {'C.' : 'Chuck',
                                 'N.' : 'Norris',
                                 'cpt' : 'counted',
                                 '2' : 'two times',
                                 'inf' : 'infinity'})
)