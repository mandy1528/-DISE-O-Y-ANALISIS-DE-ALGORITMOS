def marge (A,B,n,m):
#input: arr A, arr B
#output: arreglo ordenado

i=0 #A
j=0 #B
k=0 #C
C = [0]*(n+m-1)
while k<=n+m-1:
    if i<n and j<m:
        if A[i]<B[j]:
            C[k]=A[i]
            i+=1
        else:
            C[k]=B[j]
            j+=1
    elif i<n:
        C[k]=A[i]
        i+=1
    else:
        C[k]=B[j]
        j+=1
    k+=1
    return C
