def check_range(num: int) -> str:
    if num < 0:
        balance = "negative"
        return balance
    elif num == 0:
        balance = "zero"
        return balance
    elif 10 > num > 0:
        balance = "positive single digit"
        return balance
    else:
        balance = "positive multi digit"
        return balance






  
# don't modify code below this line
print(check_range(-10))
print(check_range(0))
print(check_range(9))
print(check_range(1000))
