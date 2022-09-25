def run(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    array = []
    for x in range(5):
        array.append(x ** 2)
    print(array)
    array = [x ** 2 for x in range(5)]
    print(array)
    array = [(x, x ** 2) for x in range(4)]
    print(array)
    # Filter list to exclude negative numbers
    vec = [-4, -2, 0, 2, 4]
    array = [x for x in vec if x >= 0]
    print(array)
    # Nested List
    vector = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    array = [number for items in vector for number in items]
    print(array)
    # transpose
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]
    array = [[row[i] for row in matrix] for i in range(3)]
    print(array)
    # With map() function
    array = list(map(ord, 'foo'))
    print(array)
    # With list comprehension
    L = [x for x in range(10) if x % 2 == 0]
    print(L)
    # Prints [0, 2, 4, 6, 8]

    # With filter() function
    array = list(filter((lambda x: x % 2 == 0), range(10)))
    print(array)
    # Prints [0, 2, 4, 6, 8]




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run('array3')
