text= " Machine learning is powerful machine learning helps analyze data data science uses machine learning "
print("original text \n")
print(text)
print("\nall values lowered\n")
print(text.lower())
print("\nin list all words seperated\n")
print(list(text.split()))
frequency ={}
for x in text.split():
    if x in frequency:
        frequency[x] += 1
    else:
        frequency[x] = 1
print("\nmost frequent word\n")
print(list(dict(sorted(frequency.items(),key=lambda item: item[1],reverse=True)).items())[0])
print("\nunique words\n")
print(set(text.split()))
print("\nwords appearing more than once\n")
print([x for x,y in frequency.items() if y > 1])