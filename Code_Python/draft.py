vowels = 'aeouiy'
string = "This website is for losers LOL!"
for x in vowels:
    if x.lower() in string:
        string = string.replace(x.lower(), '')
        
print(string)        