n = int(input())

for i in range(0,n*2+1):
    for j in range(0,n*2+1):
        if i == j or i+j == n*2:
            print(" * ", end="")
        else:
            print(" . ", end="")
    print("\t")        


    