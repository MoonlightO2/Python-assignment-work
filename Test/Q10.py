def subseq2(newstr):
    """Print all 2-element subsequences of a string."""
    for i in range(len(newstr)):
        for j in range(i + 1, len(newstr)):
            print(newstr[i] + newstr[j], end=' ')
    print()


def subseq3(newstr):
    """Print all 3-element subsequences of a string."""
    for i in range(len(newstr)):
        for j in range(i + 1, len(newstr)):
            for k in range(j + 1, len(newstr)):
                print(newstr[i] + newstr[j] + newstr[k], end=' ')
    print()


# Alternative definitions using enumerate() to avoid iterating over indices,
# but it is doubtful if this is clearer.

def subseq2alt(newstr):
    """Print all 2-element subsequences of a string."""
    for i, first in enumerate(newstr):
        for second in newstr[i + 1:]:
            print(first + second, end=' ')


def subseq3alt(newstr):
    """Print all 2-element subsequences of a string."""
    for i, first in enumerate(newstr):
        for j, second in enumerate(newstr[i + 1:]):
            for third in newstr[i + 1:][j + 1:]:
                print(first + second + third, end=' ')
    print()


# To produce all n-element subsequence, for parameter n, use
# recursion. The idea is as follows:
# Consider the string 'computer' with n=4. Some of the sequences contain
# the first character 'c', and some do not. To get the sequences which
# start with 'c', print all the length 3 subsequences of 'omputer', with
# 'c' added at the start of each (by appending 'c' to pre). Then to get
# the sequences which do not start with 'c', just print all length 4
# sequences of 'omputer'.

def subseqn(s, n, pre=''):
    """Print all n-element subsequences of a string.

    All strings are prefixed by argument pre, which is empty
    string by default."""

    # If n is 0, then the only string is the empty string, prefixed
    # by pre, i.e. just the string pre itself.
    if (n == 0):
        print(pre, end=' ')
    # Otherwise, provided the string is not empty, remove the first
    # character. Then print all sequences of length n-1 from rest of
    # string, with the first character appended to pre, then print all
    # sequences of length n from the rest of the string.
    elif (s != ''):
        subseqn(s[1:], n - 1, pre + s[0])
        subseqn(s[1:], n, pre)


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

def subseqnalt(newstr, n):
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
            while ((index >= -n) and (indexlist[index] == length + index)):
                index = index - 1

            # if there is no such element, then we have reached last
            # string, so break
            if (index < -n):
                break

            # otherwise, increase the element by one, and then set
            # the following elements to the minimum possible, i.e.
            # each element is one greater than the previous
            indexlist[index] = indexlist[index] + 1
            for j in range(index + 1, 0):
                indexlist[j] = indexlist[j - 1] + 1
