def valid_par(combination):
    diff = 0
    for par in combination:
        if par == '(':
            diff += 1
        else:
            if diff == 0:
                return False
            else:
                diff -= 1
    return diff == 0

string = "()(()))"
print(valid_par(string))