def run(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    array = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
    print(array[2:-2])
    # Return every 2nd item between position 2 to 7
    print(array[2:7:2])
    print(array[7:2:-2])
    print(array[7:])
    # reverse
    print(array[::-1])
    # /////////////////// Modify //////////////////////
    array = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
    array[1:4] = [1, 2, 3]
    print(array)
    # /////////////////// # Insert at the start //////////////////////
    array = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
    array[:0] = [1, 2, 3]
    print(array)
    # /////////////////// # Insert at the end //////////////////////
    array = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
    array[len(array):] = [1, 2, 3]
    print(array)
    # /////////////////// # Delete Multiple List Items //////////////////////
    array = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
    array[1:5] = []
    del array[1:5]
    print(array)
    #///////////// Clone
    array = ['a', 'b', 'c', 'd', 'e']
    new_list = array[:]
    print(new_list)
    # Prints ['a', 'b', 'c', 'd', 'e']
    print(new_list is array)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run('run')
