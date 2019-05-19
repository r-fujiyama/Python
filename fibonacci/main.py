import time
from fibonacci import fibonacci

print("フィボナッチ数列を生成します。")
val = int(input("値を入力してください:"))
start = time.time()
fibo = fibonacci(val)
process_time = time.time() - start
print(fibo)
print("要した時間:", process_time)
