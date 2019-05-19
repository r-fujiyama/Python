def fibonacci(n):
    if n == 0:
        return 0  # F0
    elif n == 1:
        return 1  # F1
    else:
        fibo_minus1 = 1  # Fn-1
        fibo_minus2 = 0  # Fn-2
        for _ in range(2, n):
            fibo = fibo_minus1 + fibo_minus2  # Fn = Fn-1 + Fn-2
            fibo_minus2 = fibo_minus1  # Fn-2の値を更新
            fibo_minus1 = fibo  # Fn-1の値を更新
        return fibo
