def reverse(str) :
    result =""
    for ch in str :
        result = ch + result
    return result	

str = "kashish"
print(reverse(str))