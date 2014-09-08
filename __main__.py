def sum(n):
    if(n==1):
        return 1;
    else:
        return sum(n-1)+n;
for i in range(1, 100):
    print("Suma pierwszych", i, "liczb wynosi", sum(i), "a");