# Question 5

# Using raw strings.

# It is not possible to define this string just using a raw string,
# without any concatenation etc. In particular there is no way to get
# a new line using raw strings.


# Question 6

# (a) s[0] gives 'D'
# (b) s[7] gives 'g'
# (c) s[-3] gives 'i'
# (d) len(s) gives 16
# (e) s[16] gives an IndexError: string index out of range
# (f) s[5:8] gives 'Eng'
# (g) s[-3:-6] gives '' (start index is after last index)
# (h) s[-6:-3] gives 'eer'
# (i) s[:-3] gives 'Data Engineer'
# (j) s[5:] gives 'Engineering'
# (k) s[5:500] gives 'Engineering' (out of range index allowed when slicing)
# (l) s[:] gives 'Data Engineering' (copy of whole string)
# (m) s[1:8:2] gives 'aaEg'
# (n) s[::2] gives 'Dt niern'
# (o) s[::-1] gives 'gnireenignE ataD' (reverse of string; when
# increment is negative, first two arguments default to end and start
# respectively, not start and end.)

# Question 8

def codes(newstr):
    """Print a list of ASCII codes in a string."""
    for char in newstr:
        print(ord(char))
        

# Question 9

def firstlast():
    """Replace all but first and last letter of string with underscore.

    Repeatly prompt for string and print required string
    """
    newstr = input('Enter first string: ')
    while (newstr != ''):
        lenstr = len(newstr)
        if (lenstr <= 2):
            print(newstr)
        else:
            dashstr = newstr[0] + '_' * (lenstr-2) + newstr[-1]
            print(dashstr)
        newstr = input('Enter next string: ')

# Note: In Python 3.8 (released in October 2019), you can use
# assignment expressions (written with :=) to write this a bit more
# neatly, avoiding the need for the input statement at the end, and 
# a separate statement to store the length of the string, like
# this:
#
# def firstlast():
#     """Replace all but first and last letter of string with underscore.
# 
#     Repeatly prompt for string and print required string
#     """
#     while ((newstr := input('Enter string: ')) != ''):
#         if ((lenstr := len(newstr)) <= 2):
#             print(newstr)
#         else:
#             dashstr = newstr[0] + '_' * (lenstr-2) + newstr[-1]
#             print(dashstr)
#
# Note that it is advisable to put the assignment expression in
# parentheses:
# 
# (newstr := input('Enter string: '))
#
# Note that this version will not work in version 3.7.

def firstlastk(k=1):
    """Replace all but first and last k letters of string with underscore.

    Repeatly prompt for string and print required string
    """
    newstr = input('Enter first string: ')
    while (newstr != ''):
        lenstr = len(newstr)
        if (lenstr <= 2*k):
            print(newstr)
        else:
            dashstr = newstr[:k] + '_' * (lenstr-2*k) + newstr[-k:]
            print(dashstr)
        newstr = input('Enter next string: ')
		

# Question 10

def subseq2(newstr):
    """Print all 2-element subsequences of a string."""
    for i in range(len(newstr)):
        for j in range(i+1,len(newstr)):
            print(newstr[i]+newstr[j], end=' ')
    print()

def subseq3(newstr):
    """Print all 3-element subsequences of a string."""
    for i in range(len(newstr)):
        for j in range(i+1,len(newstr)):
            for k in range(j+1,len(newstr)):
                print(newstr[i]+newstr[j]+newstr[k], end=' ')
    print()

# Alternative definitions using enumerate() to avoid iterating over indices,
# but it is doubtful if this is clearer.

def subseq2alt(newstr):
    """Print all 2-element subsequences of a string."""
    for i,first in enumerate(newstr):
        for second in newstr[i+1:]:
            print(first+second, end=' ')

def subseq3alt(newstr):
    """Print all 2-element subsequences of a string."""
    for i,first in enumerate(newstr):
        for j,second in enumerate(newstr[i+1:]):
            for third in newstr[i+1:][j+1:]:
                print(first+second+third, end=' ')
    print()

# To produce all n-element subsequence, for parameter n, use
# recursion. The idea is as follows:
# Consider the string 'computer' with n=4. Some of the sequences contain
# the first character 'c', and some do not. To get the sequences which
# start with 'c', print all the length 3 subsequences of 'omputer', with
# 'c' added at the start of each (by appending 'c' to pre). Then to get
# the sequences which do not start with 'c', just print all length 4
# sequences of 'omputer'.

def subseqn(s,n,pre=''):
    """Print all n-element subsequences of a string.

    All strings are prefixed by argument pre, which is empty 
    string by default."""
    
    # If n is 0, then the only string is the empty string, prefixed
    # by pre, i.e. just the string pre itself.
    if (n==0):
        print(pre, end=' ')
    # Otherwise, provided the string is not empty, remove the first
    # character. Then print all sequences of length n-1 from rest of 
    # string, with the first character appended to pre, then print all
    # sequences of length n from the rest of the string.
    elif (s!=''):
        subseqn(s[1:],n-1,pre+s[0])
        subseqn(s[1:],n,pre)

# An alternative version, this time not using recursion
# The idea is to store a list of indices and then update at each step
# For example, suppose the string is 'computer' with length 8, and n = 4.
# Then we want to work through all sets of indices, starting with 0,1,2,3
# 'comp' and eventually ending at 4,5,6,7 ('uter').
# If we have reached, say, the string 'cmer', corresponding to positions
# 0,2,6,7 then scan from the right looking for the first element which
# has not reached its maximum, which is 2 in this case. Increase this to
# 3, then change the following positions to the smallest possible, i.e.
# 4 and 5. Thus 0,2,6,7 changes to 0,3,4,5. Repeating this gives the
# required sequence.

def subseqnalt(newstr,n):
    length = len(newstr)
    if (n <= length):
        # create list of indices, initially 0,...,n-1
        indexlist = list(range(n))
        
        while True:
            # create list of characters at these indices, then
            # join to form string
            outlist = []
            for i in indexlist:
                outlist.append(newstr[i])
            print(''.join(outlist), end=' ')

            # now update list of indices. Start from end of list
            # and work back until you find an element that has not
            # reached its largest possible value
            index = -1
            while ((index >= -n) and (indexlist[index] == length+index)):
                index = index-1

            # if there is no such element, then we have reached last
            # string, so break
            if (index < -n):
                break

            # otherwise, increase the element by one, and then set
            # the following elements to the minimum possible, i.e.
            # each element is one greater than the previous
            indexlist[index] = indexlist[index]+1
            for j in range(index+1,0):
                indexlist[j] = indexlist[j-1]+1
           
# Question 12

def dashify(newstr):
    """Return string with hyphens separating characters."""
    return '-'.join(list(newstr))


# Question 13

def avlen():
    """Calculate average length of a list of words entered."""
    instr = input('Enter some words: ')
    words = instr.split()
    total = 0
    for w in words:
        total += len(w)
    print('Average word length:', float(total)/float(len(words)))


# Question 14

def guessstring(newstr):
    """Print string with only guessed letters shown.

    Argument is a string. Repeatly prompts for a letter to be
    entered, and prints string with only the letters guessed
    so far shown, the others replaced by underscores. Stops
    when all the letters have been guessed.
    """
    guessstr = '_'*len(newstr)
    listguess = list(guessstr)
    print(guessstr)
    while (newstr != guessstr):
        guess = input('Guess a letter: ')
        letter = guess[0]  # ignore any extra input after first letter
        for i in range(len(newstr)):
            if (newstr[i] == letter):
                listguess[i] = letter
        guessstr = ''.join(listguess)
        print(guessstr)

# Version which ignores the case of letters:

def guessstring2(newstr):
    """Print string with only guessed letters shown.

    Argument is a string. Repeatly prompts for a letter to be
    entered, and prints string with only the letters guessed
    so far shown, the others replaced by underscores. Stops
    when all the letters have been guessed. Letters can be 
    entered in either case.
    """
    guessstr = '_'*len(newstr)
    lowerstr = newstr.lower()
    listguess = list(guessstr)
    print(guessstr)
    while (newstr != guessstr):
        guess = input('Guess a letter: ')
        letter = guess[0].lower()
        for i in range(len(newstr)):
            if (lowerstr[i] == letter):
                listguess[i] = newstr[i]
        guessstr = ''.join(listguess)
        print(guessstr)


