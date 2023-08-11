def fat(x):
    print("x = ", x)
    if x == 1:  # condição de saída
        print("Condição de saída (x = 1)")
        return 1
    else:
        fatorial = x * fat(x - 1)
        print(fatorial)
        return fatorial


print("3! = ", fat(3))
# print("\n###########################\n")
# print("5! = ", fat(5))
# print("\n###########################\n")
# print("10! = ", fat(10))
    