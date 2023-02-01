#sWAP cASE https://www.hackerrank.com/challenges/swap-case/problem?isFullScreen=true
def swap_case(s):
    return s.swapcase()

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
    
#######################################################

#String Split and join # https://www.hackerrank.com/challenges/python-string-split-and-join/problem?isFullScreen=true
def split_and_join(line):
    return line.replace(" ", "-")

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
    
#######################################################

#What's your name? https://www.hackerrank.com/challenges/whats-your-name/problem?isFullScreen=true
def print_full_name(first, last):
    return print(f"Hello {first} {last}! You just delved into python.")

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)
    
#######################################################    
    
#Find a string https://www.hackerrank.com/challenges/find-a-string/problem?isFullScreen=true    
def count_substring(string, sub_string):
    count = 0
    for i in range(len(string) - len(sub_string)+1):
        if string[i:i+len(sub_string)] == sub_string:
            count += 1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
    
#######################################################

#String Validators https://www.hackerrank.com/challenges/string-validators/problem?isFullScreen=true
if __name__ == '__main__':
    s = input()
    functions = [str.isalnum, str.isalpha, str.isdigit, str.islower, str.isupper]
    
    for func in functions:
        print(any(func(char) for char in s))
          
#######################################################

#Mutations https://www.hackerrank.com/challenges/python-mutations/problem?isFullScreen=true
 def mutate_string(string, position, character):
    l = list(string)
    l[position] = character
    string = ''.join(l)
    return string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
    
#######################################################

#Text Wrap https://www.hackerrank.com/challenges/text-wrap/problem?isFullScreen=true
import textwrap
def wrap(string, max_width):
    return textwrap.fill(string, max_width)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
    
#######################################################

# Designer Door Mat https://www.hackerrank.com/challenges/designer-door-mat/problem?isFullScreen=true
if __name__ == '__main__':

    height,width=list(map(int,input().split()))
    j=1
    for i in range(height):
        if i < height //2:
            print((".|."*j).center(width,"-"))
            j+=2
        elif i == height //2:
            print("WELCOME".center(width,"-"))
        elif i > height //2:
            j-=2
            print((".|."*j).center(width,"-"))
            
#######################################################

#String Formatting https://www.hackerrank.com/challenges/python-string-formatting/problem?isFullScreen=true
def print_formatted(number):
    width = len(str(bin(number))[2:])
    for i in range(1, number+1):
        print("{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(i, width=width))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
    
#######################################################

#Alphabet Rangoli https://www.hackerrank.com/challenges/alphabet-rangoli/problem?isFullScreen=true
import string
def print_rangoli(size):
    alphabet = string.ascii_lowercase
    for i in range(size - 1, -size, -1):
        row = []
        for j in range(abs(i), size):
            if j >= 0:
                row.append(alphabet[j])
        row = '-'.join(row[::-1] + row[1:]).center((size * 4) - 3, '-')
        print(row)

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
    
#######################################################

#Capitalize! https://www.hackerrank.com/challenges/capitalize/problem?isFullScreen=true
def solve(s):
    temp = s.split()
    for word in temp:
        s = s.replace(word, word.capitalize())
    return s

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = solve(s)
    fptr.write(result + '\n')
    fptr.close()

#######################################################

#The Minion Game https://www.hackerrank.com/challenges/the-minion-game/problem?isFullScreen=true
def minion_game(string):
    vowels = "AEIOU"
    kevin_score = 0
    stuart_score = 0
    
    for i in range(len(string)):
        if string[i] in vowels:
            kevin_score += len(string) - i
        else:
            stuart_score += len(string) - i

    if kevin_score > stuart_score:
        print("Kevin", kevin_score)
    elif kevin_score < stuart_score:
        print("Stuart", stuart_score)
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)
    
#######################################################

# Merge the Tools! https://www.hackerrank.com/challenges/merge-the-tools/problem?isFullScreen=true
def merge_the_tools(string, k):
    # your code goes here
    for i in range(0, len(string), k):
        s = string[i:i + k]
        result = ""
        for char in s:
            if char not in result:
                result += char
        print(result)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
    
