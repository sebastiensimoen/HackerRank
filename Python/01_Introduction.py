#Say "Hello, World!" With Python https://www.hackerrank.com/challenges/py-hello-world/problem?isFullScreen=true
if __name__ == '__main__':
    print("Hello, World!")

#######################################################

#Python If-Else https://www.hackerrank.com/challenges/py-if-else/problem?isFullScreen=true
if __name__ == '__main__':
  n = int(input().strip())
  if n % 2 == 1:
      print("Weird")
  elif n % 2 == 0 and n >= 2 and n <= 5:
      print("Not Weird")
  elif n % 2 == 0 and n >= 6 and n <= 20:
      print("Weird")
  elif n % 2 == 0 and n > 20:
      print("Not Weird")
      
#######################################################

#Arithmetic Operators https://www.hackerrank.com/challenges/python-arithmetic-operators/problem?isFullScreen=true
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(f"{a+b}\n{a-b}\n{a*b}")
    
#######################################################

#Python: Division https://www.hackerrank.com/challenges/python-division/problem?isFullScreen=true
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(f"{a//b}\n{a/b}")
    
#######################################################

#Loops https://www.hackerrank.com/challenges/python-loops/problem?isFullScreen=true
if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        print(i*i)
        
#######################################################

#Write a function https://www.hackerrank.com/challenges/write-a-function/problem?isFullScreen=true
def is_leap(year):
    leap = False
    if year % 4 == 0:
        if year % 100 != 0 or year % 400 == 0:
            leap = True
    return leap
year = int(input())
print(is_leap(year))

#######################################################

#Print Function https://www.hackerrank.com/challenges/python-print/problem?isFullScreen=true
if __name__ == '__main__':
    n = int(input())
    for i in range(1, n+1, 1):
        print(i, end='')
