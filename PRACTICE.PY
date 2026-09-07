# 1.
# print("hello world")


# 2.3.4.
# a=int(input("enter 1st number:"))
# b=int(input("enter 2nd number:"))
# print(f"the sum of the two numbers is {a+b}")
# a,b=b,a
# print(f"a={a} and b={b}")


# 5.6.
# a=int(input("enter 1st number:"))
# b=int(input("enter 2nd number:"))
# c=int(input("enter 3rd number:"))
# if a>b and a>c:
#     print(f"{a} is the largest number.")
# elif b>c and b>a:
#     print(f"{b} is the largest number.")
# else:
#     print(f"{c} is the largest number.")


# 7.8.
# a=int(input("enter the number:"))
# if a%2==0:
#     print(f"{a} is a even number")
# else:
#     print(f"{a} is a odd number")
# if a<0:
#     print("negative")
# elif a>0:
#     print("positive")
# else:
#     print("neither negative nor positive")

# 9.
# n=int(input("enter the number:"))
# sum=0
# for i in range(n+1):
#     sum+=i
# print(f"the sum of first {n} natural number is {sum}")


# 10.
# n=int(input("enter the number:"))
# i=1
# while i<=10:
#     print(f"{n:2}*{i:2}={n*i:3}")
#     i+=1

# 11.
# n=int(input("enter the number:"))
# a=n
# fact=1
# while n>=1:
#     fact*=n
#     n-=1
# print(f"the factorial of {a} is {fact}")


# 12.
n=int(input("enter the number:"))
if n<=1:
    print("it is not a prime number")
else:
    for i in range(2,int(n*0.5)+1):
        if n%i==0:
            print("it is not a prime number")
            break
        else:
            print("it is a prime number")



# 13.
n=int(input("enter the"))

