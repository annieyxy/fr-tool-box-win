# define method to check if input is number
def isnum(numstr):
    numstr = str(numstr)
    if numstr.isnumeric():
        return True
    else:
        if numstr.__contains__('.'):
            if numstr.count('.') == 1:
                temp = numstr.split('.')
                if temp[0].isnumeric():
                    if temp[1].isnumeric():
                        return True
                    elif temp[1] == '':
                        return True
                elif temp[0].startswith('-'):
                    if temp[1].isnumeric():
                        return True
                    elif temp[1] == '':
                        return True
        elif numstr.startswith('-'):
            if numstr[1:].isnumeric():
                return True
    return False
