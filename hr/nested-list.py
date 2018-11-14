if __name__ == '__main__':
    students = list()
    # for _ in range(int(input())):
    #     name = input()
    #     score = float(input())
    #     students.append([name, score])

    students.append(['Prashant', 32])
    students.append(['Pallavi', 36])
    students.append(['Dheeraj', 39])
    students.append(['Shivam', 40])
    
    print('\ninitial')
    for x in students:
        print(f'{x[0]} {x[1]}')

    minItem = min(x[1] for x in students)
    print(f'\nmin {minItem}')

    students = list(filter(lambda x: x[1] > minItem, students))
    print('\nwithout min')
    for x in students:
        print(f'{x[0]} {x[1]}')

    minItem = min(x[1] for x in students)
    print(f'\nmin {minItem}')

    students = list(filter(lambda x: x[1] == minItem, students))
    print('\nrunner-ups')
    for x in students:
        print(f'{x[0]} {x[1]}')

    students.sort(key=lambda x: x[0], reverse=False)

    print('final')
    for x in students:
        print(x[0])