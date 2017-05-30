#Boolean: ContainsDuplicates(Integer: array[])
# //Cycle for all array, untill last item (with out it)
# For i=0 To <maximum index>-1
#         //Cycle for array elements after item i.
#           For j=i+1 To <maximum index>
#               //Check, dublicates
#               if (array[i]==array[j]) Then Return True
#           Next j
#Next i
#-------------------------------------------------------#

"My Python realisation"

n = [1, 2, 3, 4, 5, 6, 7, 8, 88, 9, 10, 11, 12]
f = [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 88, 123, 66]
a = False
i, j = 0, 0
for i in range((len(n)-1)-1):
    j = i + 1
    for j in range(len(n)):
        if n[i] == f[j]:
            print(True, i, j)
            a = True
if a != True:
    print(False)
"--------------------------"
"Time of this algorithm"
# for i=0:
# n^2-2*n+1 => for i=0 (n-1), for j=0 (n-1)
# n-1 => for i=n-1 (n-1), for j=1 (1)
#=> ((n^2-2*n+1)+(n-1))/2=>(n^2-n)/2, or O(N^2) N->oo
