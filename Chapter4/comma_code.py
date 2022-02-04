def comma(param):
    string = ''
    for item in param[:-1]:
        string += (str(item) + ', ')

    string += ('and ' + str(param[-1]))
    return string

var = ['almonds', 'm&ms', 'raisins', 'peanuts', 'cashews']
varComma = comma(var)
print(varComma)
        
