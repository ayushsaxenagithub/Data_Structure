#We clone this on GitHub to check if the repository is working properly
n= int (input("Enter the number : "))
def sum(num):
    s=0
    for i in range(1,num+1):
        s=s+( i*i*i) 
    return s

print("The sum of the numbers is :",sum(n))

