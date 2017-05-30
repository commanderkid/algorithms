##O(f(N)*g(N)) algorithm realisation
a = [9, 8, 7, 3, 5, 7, 1, 2, 3, 4, 5, 6]
b = [11, 22, 44, 55, 44, 33, 4, 26, 24, 52, 55, 6]
i, j = 0, 0
for i in range(len(a)-1):
    for j in range(len(b)-1):
        if (i != j):
            if a[i] == b[j]:
                print("True", i, j)
                print(a[i], b[j])
            #else:
             #   j = j+1
        #else:
         #   i = i+1
###--------------------------------------------------###
a = [9, 8, 7, 3, 5, 7, 1, 2, 3, 4, 5, 6]
b = [11, 22, 44, 55, 44, 33, 4, 26, 24, 52, 55, 6]
i, j = 0, 0
for i in range(len(a)-2):
    j=i+1
    for j in range(len(b)-1):
        if a[i] == a[j]:
            print("True")
        #else:
            
    
