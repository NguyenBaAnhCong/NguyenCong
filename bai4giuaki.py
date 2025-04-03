def fibonacci(n):
    if n == 0:
        return [0]
    elif n == 1:
        return [0, 1]

    fib = [0] * (n + 1)  # Tạo mảng lưu Fibonacci
    fib[1] = 1  

    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]  

    return fib  # Trả về toàn bộ mảng Fibonacci

n = int(input("Nhập số n: "))
if n < 0:
    print("Vui lòng nhập số nguyên không âm.")
else:
    fib_array = fibonacci(n)  
    print(f"Dãy Fibonacci từ 0 đến {n}: {fib_array}")  
    print(f"Số Fibonacci thứ {n} là: {fib_array[n]}")  
