prime=[]
for num in range(2, 50):
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           prime.append(num)
print("prime numbers:" ,prime)    