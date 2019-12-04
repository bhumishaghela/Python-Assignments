ApniDictionary={"Autotune":"A device or facility for tuning something automatically, especially a computer program which enables the correction of an out-of-tune vocal performance.","Big Data":"Extremely large data sets that may be analyzed computationally to reveal patterns, trends, and associations, especially relating to human behavior and interactions","DIY":"The activity of decorating, building, and making repairs at home by oneself rather than employing a professional.","Hater":"A person who greatly dislikes a specified person or thing."}
print("Ask meaning of a word")
word=raw_input()
print(word)
if word in ApniDictionary.keys():
    w1=ApniDictionary[word]
    print(w1)
