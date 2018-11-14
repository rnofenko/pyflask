if __name__ == '__main__':
    n = 3
    
    commands = []
    #commands = ['insert 0 5','insert 1 10','insert 0 6','print','remove 6','append 9','append 1','sort','print','pop','reverse','print']

    for i in range(n):
        commands.append(input())
    
    list = []
    for commandText in commands:
        parts = commandText.split(' ')
        command = parts[0]
        if command == 'insert':
            list.insert(int(parts[1]), int(parts[2]))
        elif command == 'print':
            print(list)
        elif command == 'remove':
            list.remove(int(parts[1]))
        elif command == 'append':
            list.append(int(parts[1]))
        elif command == 'sort':
            list.sort()
        elif command == 'reverse':
            list.reverse()
        elif command == 'pop':
            list.pop()
        else:
            print('Unhandled command ' + command)