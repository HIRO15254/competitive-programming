N = int(input())
n = N % 10
if n == 2 or n == 4 or n == 5 or n == 7 or n == 9:
    print("hon")
elif n == 3:
    print("bon")
else:
    print("pon")
