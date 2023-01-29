# List Comprehensions https://www.hackerrank.com/challenges/list-comprehensions/problem?isFullScreen=true
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    print([[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i + j + k != n])
    
#######################################################

#Find the Runner-Up Score! https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?isFullScreen=true
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    
    maximum = max(arr)
    arr = [num for num in arr if num != maximum]
    
    runner_up = max(arr)
    print(runner_up)
    
#######################################################

#Nested Lists https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true
if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
        
    second_lowest_grade = sorted(set(score for name, score in students))[1]
    students = sorted([name for name, score in students if score == second_lowest_grade])
    print(*students, sep='\n')
    
#######################################################

#Finding the percentage https://www.hackerrank.com/challenges/finding-the-percentage/problem?isFullScreen=true
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
            
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        average = sum(scores) / len(line)
        
        student_marks[name] = "%.2f" % average
        
    query_name = input()
    for name in student_marks.keys():
            if name == query_name:
                print(student_marks[name])
                break

#######################################################

#Lists https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=true
if __name__ == '__main__':
    N = int(input())
    liste = []

    for i in range(N):
        key, *value = input().split()
        if key == 'insert':
            liste.insert(int(value[0]), int(value[1]))
        elif key == 'print':
            print(liste)
        elif key == 'remove':
            liste.remove(int(value[0]))
        elif key == 'append':
            liste.append(int(value[0]))
        elif key == 'sort':
            liste.sort()
        elif key == 'pop':
            liste.pop()
        elif key == 'reverse':
            liste.reverse()

#######################################################

#Tuples https://www.hackerrank.com/challenges/python-tuples/problem?isFullScreen=true
if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    my_tuple = tuple(integer_list)
    print(hash(my_tuple))
