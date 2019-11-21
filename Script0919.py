#09/19/2019 Valarie Harrison
#Lecture script practice for List data type

L = ["apple","kiwi","orange","banana","pear"]
L.append("watermelon")
print L
print L.count("apple")
print len(L)
x = L.count("apple")
print x
>>> L = [1,2,3,4,5]
>>> print L
[1, 2, 3, 4, 5]
>>> L = [1,2,3,4,"five"]
>>> print L
[1, 2, 3, 4, 'five']
>>> P = ['apple',"kiwi","orange"]
>>> print P
['apple', 'kiwi', 'orange']
>>> G = [1,2,3,P]
>>> print G
[1, 2, 3, ['apple', 'kiwi', 'orange']]
>>> print[0]
[0]
>>> print G[0]
1
>>> print G[3]
['apple', 'kiwi', 'orange']
>>> print G[3][1]
kiwi
>>> print G[3][1][1]
i
>>> print G[-2:-1]
[3]
>>> print G
[1, 2, 3, ['apple', 'kiwi', 'orange']]
>>> print L + P
[1, 2, 3, 4, 'five', 'apple', 'kiwi', 'orange']
>>> print L * 2
[1, 2, 3, 4, 'five', 1, 2, 3, 4, 'five']
>>> ['apple', 'kiwi', 'orange', 'banana', 'pear', 'watermelon']
['apple', 'kiwi', 'orange', 'banana', 'pear', 'watermelon']
>>> ['apple', 'kiwi', 'orange', 'banana', 'pear', 'watermelon']
>>> import math
>>> dir(math)
['__doc__', '__name__', '__package__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'copysign', 'cos', 'cosh', 'degrees', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'hypot', 'isinf', 'isnan', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'modf', 'pi', 'pow', 'radians', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'trunc']
>>> print math.sqrt.__doc__
sqrt(x)

Return the square root of x.
>>> import random
>>> dir(random)
['BPF', 'LOG4', 'NV_MAGICCONST', 'RECIP_BPF', 'Random', 'SG_MAGICCONST', 'SystemRandom', 'TWOPI', 'WichmannHill', '_BuiltinMethodType', '_MethodType', '__all__', '__builtins__', '__doc__', '__file__', '__name__', '__package__', '_acos', '_ceil', '_cos', '_e', '_exp', '_hashlib', '_hexlify', '_inst', '_log', '_pi', '_random', '_sin', '_sqrt', '_test', '_test_generator', '_urandom', '_warn', 'betavariate', 'choice', 'division', 'expovariate', 'gammavariate', 'gauss', 'getrandbits', 'getstate', 'jumpahead', 'lognormvariate', 'normalvariate', 'paretovariate', 'randint', 'random', 'randrange', 'sample', 'seed', 'setstate', 'shuffle', 'triangular', 'uniform', 'vonmisesvariate', 'weibullvariate']
>>> random.randrange(0,10)
5
>>> range(0,10)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> random.randrange(0,10)
0
>>> random.randrange(0,10)
0
>>> random.randrange(0,10)
4
>>> random.randrange(0,10)
8
>>> random.randrange(0,10)
6
>>> random.randrange(0,10)
6
>>> random.randrange(0,10)
9
>>> random.randrange(0,10)
1
>>> random.randint(0,10)
8
>>> random.randint(0,10)
3
>>> random.randint(0,10)
3
>>> random.randint(0,10)
4
>>> random.randint(0,10)
7
>>> random.randint(0,10)
1
>>> random.randint(0,10)
0
>>> random.randint(0,10)
6
>>> random.randint(0,10)
2
>>> random.randint(0,10)
9
>>> random.randint(0,10)
1
>>> random.choice(L)
'banana'
>>> print L
['apple', 'kiwi', 'orange', 'banana', 'pear', 'watermelon']
>>> random.choice(L)
'apple'
>>> random.choice(L)
'kiwi'
>>> random.choice(L)
'apple'
>>> random.choice(L)
'apple'
>>> random.choice(L)


# **IMPORTANT TOPICS:  Make a decision / Make a loop************
x = 1
if x > 2:
    print "The number is greater than two"
elif x == 1:
    print "The number is one"
print "haha"


#Study if, elif, else