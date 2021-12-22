def fib(n):
    P = 0
    Q = 1
    if n == 1:
        print(P)
    else:
        print(P)
        print(Q)
        for i in range(2,n):
            R = P + Q
            P = Q
            Q = R
            print(Q)
fib(10)