text1 = input("enter text: ")
text2 = input("enter text: ")
freq1 = { }

def _anagram(txt1, txt2):
    for x in txt1:
        if x in freq1:
            freq1[x] += 1
        else:
            freq1[x] = 1
    freq2 = { }
    for x in txt2:
        if x in freq2:
            freq2[x] += 1
        else:
            freq2[x] = 1
    if freq1 == freq2:
        print("it is a anagram")
    else:
        print("it is a non-anagram")
_anagram(text1, text2)
