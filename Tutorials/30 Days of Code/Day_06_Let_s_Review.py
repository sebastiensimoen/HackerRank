if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        s = input()
        print(s[::2] + ' ' + s[1::2]) 
