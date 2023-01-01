# Question 1

def multlists(list1,list2):
    '''Multiply two lists by creating a list of pairs.

    Loop over both lists and append each pair to result.
    '''
    result = []
    for x in list1:
        for y in list2:
            result.append((x,y))
    return result

# or (using list comprehensions)

def multlists2(list1,list2):
    '''Multiply two lists by creating a list of pairs.

    Use list comprehension.
    '''
    return [(x,y) for x in list1 for y in list2]
            
# Question 2

# To get lists of multiples, use list comprehensions:
# m6 = [x for x in range(0,100,6)]
# m7 = [x for x in range(0,100,7)]
# m9 = [x for x in range(0,100,9)]
#
# For those divisible by 6 and 7, convert to sets and use intersection
# set(m6) & set(m7)
#
# For those divisible by 7 or 9, convert to sets and use union
# set(m7) | set(m9)

# Question 3

# products = {x*y for x in range(1,11) for y in range(1,11)}
#
# len(products) gives 42.
#
# allnums = set(range(1,101))
# nonproducts = allnums - products

def nonproducts(n):
    '''Calculate set of numbers in 1..n*n not products of 1..n.'''

    products = {x*y for x in range(1,n+1) for y in range(1,n+1)}
    return set(range(1,n*n+1)) - products

# Question 4

# moduledict = {'AC50001' : 'Introduction to Data Mining',
# 'AC50002' : 'Programming Languages for Data Engineering',
# 'AC51001' : 'Internet and Computer Systems',
# 'AC51002' : 'Software Development',
# 'AC51003' : 'Software Engineering',
# 'AC51004' : 'Agile Engineering',
# 'AC51005' : 'Technology Innovation Management',
# 'AC51007' : 'Computer Vision',
# 'AC51008' : 'Graphics',
# 'AC51009' : 'Multimedia Audio',
# 'AC51010' : 'Computing the User Experience',
# 'AC51011' : 'Big Data Analysis',
# 'AC52001' : 'Database Systems',
# 'AC52002' : 'Advanced Programming Techniques',
# 'AC52008' : 'Research Frontiers (Computing)',
# 'AC52009' : 'Secure Internet Programming',
# 'AC52012' : 'Research Methods',
# 'AC52013' : 'Human Computer Interaction and Usability Engineering'
# }

def semesters(moduledict):
    '''Print list of modules in each semester, from dictionary.

    Loop twice over dictionary, and print the correct modules
    by testing fourth character of module code.
    '''
    print('Semester 1')
    for mod in sorted(moduledict):
        if mod[3] in'01':
            print(mod, moduledict[mod], sep=' ')
    print('\nSemester 2')
    for mod in sorted(moduledict):
        if mod[3] in'02':
            print(mod, moduledict[mod], sep=' ')
    
# Question 5

def strcount(listofstrings):
    '''Count how many times each string occurs in a list.

    Create empty dictionary, then loop over list. For each element
    check if it is already a key in dictionary; if not, create it, if
    so increment it.
    '''
    strcounts = dict()
    for s in listofstrings:
        if s not in strcounts:
            strcounts[s] = 1
        else:
            strcounts[s] += 1
    return strcounts

# A shorter version using a dictionary comprehension.

def strcount2(listofstrings):
    '''Count how many times each string occurs in a list.

    Dictionary comprehension using count() method of lists.
    '''
    return {s : listofstrings.count(s) for s in listofstrings}

# Question 6

def version(listofstrings):
    '''Tag strings in list with version number.

    Create empty dictionary and empty list. Loop over list,
    keeping track in dictionary of how many times each string
    has occurred. Add appropriate string to new list.'''
    strcounts = dict()
    newlist = []
    for s in listofstrings:
        if s not in strcounts:
            strcounts[s] = 0
            suffix = ''
        else:
            strcounts[s] += 1
            suffix = '_' + str(strcounts[s])
        newlist.append(s + suffix)
    return newlist

# Question 7

# First a straightforward way.

def roman(n):
    '''Convert integer to roman numerals.'''
    listnum = []
    thousands = n // 1000
    if (thousands > 0):
        listnum.append('M'*thousands)
        n %= 1000
    if (n >= 900):
        listnum.append('CM')
        n -= 900
    if (n >= 500):
        listnum.append('D')
        n -= 500
    if (n >= 400):
        listnum.append('CD')
        n -= 400
    hundreds = n // 100
    if (hundreds > 0):
        listnum.append('C'*hundreds)
        n %= 100
    if (n >= 90):
        listnum.append('XC')
        n -= 90
    if (n >= 50):
        listnum.append('L')
        n -= 50
    if (n >= 40):
        listnum.append('XL')
        n -= 40
    tens = n // 10
    if (tens > 0):
        listnum.append('X'*tens)
        n %= 10
    if (n >= 9):
        listnum.append('IX')
        n -= 9
    if (n >= 5):
        listnum.append('V')
        n -= 5
    if (n >= 4):
        listnum.append('IV')
        n -= 40
    ones = n
    if (ones > 0):
        listnum.append('I'*ones)
    return ''.join(listnum)
        
# But there is a logic to this, which we can use to shorten the
# function if we gather all the "data" into a list of 2-tuples:

def roman2(n):
    '''Convert integer to roman numerals.'''
    letters = [(1000,'M'), (900,'CM'), (500, 'D'), (400, 'CD'),
               (100,'C'), (90,'XC'), (50, 'L'), (40, 'XL'),
               (10,'X'), (9,'IX'), (5, 'V'), (4, 'IV'), (1,'I')]
    listnum = []
    for x in letters:
        while (n >= x[0]):
            listnum.append(x[1])
            n -= x[0]
    return ''.join(listnum)
        
# A slight variant. Calculate how many of each string need to be added
# to the end of the list, rather than using a while loop. This is
# probably the best version.

def roman3(n):
    '''Convert integer to roman numerals.'''
    letters = [(1000,'M'), (900,'CM'), (500, 'D'), (400, 'CD'),
               (100,'C'), (90,'XC'), (50, 'L'), (40, 'XL'),
               (10,'X'), (9,'IX'), (5, 'V'), (4, 'IV'), (1,'I')]
    listnum = []
    for x in letters:
        listnum.append(x[1]*(n // x[0]))
        n %= x[0]
    return ''.join(listnum)

# We could use a dictionary instead, but because dictionaries are not
# ordered it is essential to get a sorted list of keys and then
# reverse it to ensure we process the numbers in the correct order.

def roman4(n):
    '''Convert integer to roman numerals.'''
    letters = {1000:'M', 900:'CM', 500: 'D', 400: 'CD',
               100:'C', 90:'XC', 50: 'L', 40: 'XL',
               10:'X', 9:'IX', 5: 'V', 4: 'IV', 1:'I'}
    listnum = []
    for x in reversed(sorted(letters.keys())):
        while (n >= x):
            listnum.append(letters[x])
            n -= x
    return ''.join(listnum)
        
# Again a slight variant like the one above.

def roman5(n):
    '''Convert integer to roman numerals.'''
    letters = {1000:'M', 900:'CM', 500: 'D', 400: 'CD',
               100:'C', 90:'XC', 50: 'L', 40: 'XL',
               10:'X', 9:'IX', 5: 'V', 4: 'IV', 1:'I'}
    listnum = []
    for x in reversed(sorted(letters.keys())):
        listnum.append(letters[x]*(n // x))
        n %= x
    return ''.join(listnum)
        
# Question 8

# >>> list(map(lambda x : x**3%7,range(1,51)))

# >>> [x**3%7 for x in range(1,51)]

# Question 9

def makedict(list1, list2):
    '''Zip two lists into a dictionary'''
    if (len(list1) == len(set(list1))):
        return dict(zip(list1, list2))
    else:
        return None

# Question 10

def powergen(k):
    result = 1
    while True:
        yield result
        result *= k

# Question 11

def powers23(n):
    '''Print n powers of 2 or 3 in order'''
    powers2 = iter(powergen(2))
    powers3 = iter(powergen(3))
    p2 = next(powers2)
    p3 = next(powers3)
    p3 = next(powers3)
    for i in range(n):
        if (p2 < p3):
            print(p2,end=' ')
            p2 = next(powers2)
        else:
            print(p3,end=' ')
            p3 = next(powers3)

def powers(numlist,n):
    '''Print n powers of numbers in numlist, in order'''
    lenlist = len(numlist)
    iterlist = [iter(powergen(i)) for i in numlist]
    powerlist = list(map(next,iterlist))
    for i in range(n):
        minpower = min(powerlist)
        print(minpower,end=' ')
        for j in range(lenlist):
            if (powerlist[j] == minpower):
                powerlist[j] = next(iterlist[j])

# Question 12

# Basic version

def printstrings0(strlist):
    for i,s in enumerate(strlist, start=1):
        print('{}. {}'.format(i,s))

# Strings right justified in 10 spaces.

def printstrings1(strlist):
    for i,s in enumerate(strlist, start=1):
        print('{}. {:>10s}'.format(i,s))

# Question 13

# Strings right justified in correct number of spaces.

def printstrings2(strlist):
    maxlen = max(map(len,strlist))
    formatstr = '{}. {:>' + str(maxlen) + 's}'
    for i,s in enumerate(strlist, start=1):
        print(formatstr.format(i,s))

# or (using replacement field to substitute value of maxlen)

def printstrings2b(strlist):
    maxlen = max(map(len,strlist))
    for i,s in enumerate(strlist, start=1):
        print('{0}. {1:>{2}s}'.format(i,s,maxlen))
  
# Strings and numbers right justified in correct number of spaces.

def printstrings3(strlist):
    maxlen = max(map(len,strlist))
    maxno = len(strlist)+1
    longest = len(str(maxno))
    formatstr = '{:' + str(longest) + 'd}. {:>' + str(maxlen) + 's}'
    for i,s in enumerate(strlist, start=1):
        print(formatstr.format(i,s))

# or (using replacement fields to substitute values longest and maxlen)

def printstrings3b(strlist):
    maxlen = max(map(len,strlist))
    maxno = len(strlist)+1
    longest = len(str(maxno))
    for i,s in enumerate(strlist, start=1):
        print('{0:{2}d}. {1:>{3}s}'.format(i,s,longest,maxlen))

# Another way, using format() to create the format string. To get
# literal curly braces inside the string, they need to be repeated, {{
# or }}.

def printstrings4(strlist):
    maxlen = max(map(len,strlist))
    maxno = len(strlist)+1
    longest = len(str(maxno))
    formatstr = '{{:{}d}}. {{:>{}s}}'.format(longest, maxlen)
    for i,s in enumerate(strlist, start=1):
        print(formatstr.format(i,s))

# Question 14

def fib_abcd(A,B,C,D):
    def fib(n):
        if (n < 0):
            return None
        elif (n == 0):
            return A
        elif (n == 1):
            return B
        else:
            x,y = A,B
            for i in range(2,n+1):
                y,x = D*x+C*y, y
            return y
    return fib

# Then (for example) fib = fib_abcd(0,1,1,1) gives a function to
# generate the standard Fibonacci numbers.
#
# fib_abcd(1,2,2,0) gives powers of 2.
#
# For a sequence where each number is three times the previous one minus the
# one before, and starting 1,3, use fib_abcd(1,3,3,-1). This gives alternate
# terms of the Fibonacci sequence.
