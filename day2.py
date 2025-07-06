#factorial of number
"""def factorial(n):
    if n<0:
        print("Negative have not factorial")
    elif(n==0 or n==1):
        print("factoeial:",n)
    else:
        result=1
        for i in range(2,n+1):
            result*=i
        print("factorial of number:",result)
n=int(input("Enter the factorial number:"))
factorial(n)"""
#largest of three number
"""def largest(a,b,c):
    biggest=max(a,b,c)
    print("Largest of three number:",biggest)
largest(6,4,7)"""
#file handling
"""with open("text.txt","w") as f:
    f.write("hello")
with open("text.txt","r") as f:
    content=f.read()
    print(content)"""
#API
import requests
name=input("Enter the name:")
url=f"https://api.agify.io/?name={name}"
response=requests.get(url)
data=response.json()
print("name:",data["name"])
print("Predicted age:",data["age"])