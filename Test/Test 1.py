def working_ascii():
    """
        G    r   e    e    t    i     n   g    s    !
        71, 114, 101, 101, 116, 105, 110, 103, 115, 33
    """

    hello = [71, 114, 101, 101, 116, 105, 110, 103, 115, 33]
    pmsg = ''.join(chr(i) for i in hello)
    print(pmsg)

    for i in range(33, 256):
        print(" ascii: {0} char: {1}".format(i, chr(i)))

working_ascii()