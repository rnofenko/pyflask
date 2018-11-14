if __name__ == '__main__':
    string = "abracadabra"
    character = 'w'
    position = 5
    res = string[:position] + character + string[position+1:]
    print(res)
    
    string = "ABCDCDC"
    sub_string = "CDC"
    count = 0
    for i in range(0, len(string)):
        if string.find(sub_string, i) == i:
            count+=1
    print(count)
