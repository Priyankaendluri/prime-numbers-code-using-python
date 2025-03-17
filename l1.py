start=int(input("enter start"))
end=int(input("enter stop"))
count=int(input("Enter count:"))
def is_prime(n):
   if n<2:
      return false
   for i in range(2,int(n*0.5)+1):
       if(n%i==0):
          return False
       return True
def print_n_primes(start,end,count):
  primes=[num for num in range(start,end+1)]
  if len(primes)>=count:
      print(count,primes[:count])
  else:
      print(f"only{len(primes)} fewer prime numbers available:")
print_n_primes(start,end,count)

