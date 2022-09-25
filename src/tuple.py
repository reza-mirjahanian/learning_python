def run(name):
    # A tuple with mixed datatypes
    t = (1, 'abc', 1.23, True)
    print(t)
    T = (4,)
    print(type(T))
    # Not a tuple
    T = (4)
    print(type(T))
    # unpack
    T = ('red', 'green', 'blue', 'cyan')
    (a, b, c, d) = T
    print(a)
    # Swap
    a = 1
    b = 99
    a, b = b, a
    print(a)
    print(b)

    addr = 'bob@python.org'
    user, domain = addr.split('@')
    print(user)
    print(domain)
    # Replicate
    T = ('red',) * 3
    print(T)





# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run('tuple')
