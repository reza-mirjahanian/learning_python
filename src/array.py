def run(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    array = list(name)
    array.append('t')
    array.insert(2, 'x')
    array += ['2']
    array.extend(['e3'])
    print(array)
    list2 = ['red']
    list2 = list2 * 3
    print(list2)
    if 'yellow' not in list2:
        print('yes')
    colors = ['red', 'green', 'blue']
    for item in colors:
        print(item)
    for i in range(len(colors)):
        colors[i] = colors[i] * 2
    print(colors)
    list3 = [0 for x in range(len(colors))]
    print(list3)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run('run')
