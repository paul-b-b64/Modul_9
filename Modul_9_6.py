def  all_variants(text):
    n = 0
    while n != len(text):
        i = 0
        while i != len(text) - n:
            yield text[i:i + 1 + n]
            i += 1
        n += 1

a = all_variants("abc")
for i in a:
    print(i)
