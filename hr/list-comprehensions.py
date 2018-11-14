if __name__ == '__main__':
    x = 2
    y = 2
    z = 2
    n = 2
    
    r = list()
    for i in range(0,x+1):
        for j in range(0, y+1):
            for k in range(0, z+1):
                if(i+j+k != n): r.append([i,j,k])
    
    print(r)