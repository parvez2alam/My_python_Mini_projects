n = int(input("enter any number:"))
if n <= 1:
     print("it is not a prime number.")
else:
     is_prime = True
     for i in range(2, n):
         if n % i == 0:
             is_prime = False
             break
     if is_prime == True:
         print("It is a prime number.")
     else:
         print("it is not a prime number.")