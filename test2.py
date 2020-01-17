from collections import Counter , defaultdict , OrderedDict


#Counter gives a dictionary with frequencies of elements of list as dictionary

li = [1,2,3,4,5,6,7,7,1]
sentence = 'blah blah blah'
print(Counter(li))
print(Counter(sentence))

#defaultdict gives the inaacessible keys of a dictionory a default value

dict = defaultdict(lambda: 5,{'a':1 , 'b':2})
print(dict['c'])


#OrderedDict makes a ordered dictionary..when we compare two dictionaries then order will matter

d1= OrderedDict()
d1['a']=1
d1['b']=2

d2= OrderedDict()
d2['b']=2
d2['a']=1


print(d1==d2)