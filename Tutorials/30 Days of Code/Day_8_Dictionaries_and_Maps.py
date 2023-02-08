if __name__ == '__main__':
    n = int(input().strip())
    phone_book = {}
    for i in range(n):
        name, phone = input().strip().split(' ')
        phone_book[name] = phone
    while True:
        try:
            name = input().strip()
            if name in phone_book:
                print(f"{name}={phone_book[name]}")
            else:
                print("Not found")
        except EOFError:
            break
