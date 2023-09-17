def get_count(sentence):
    vowels,count=set(['a','e','i','o','u']),0
    for c in sentence:
        if(c in vowels):
            count+=1
    return count