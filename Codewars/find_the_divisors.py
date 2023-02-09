def divisors(integer):
    divisors = []
    count = 2
    while count != integer:
        if integer % count == 0:
            divisors.append(count)    
        count += 1
    if len(divisors) >= 1:
        return divisors
    else:
        return f"{integer} is prime"