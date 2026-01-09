# Task 1

# Write your own generator function my_enumerate that works like the built-in function enumerate.

lessons = ["Why Python Programming", "Data Types and Operators", "Control Flow", "Functions", "Scripting"]

def my_enumerate(arr, step=1):
    i = 0 
    while i < len(arr):
        yield i, arr[i]
        i += step

print("Task 1")
for i, lesson in my_enumerate(lessons, 1):
    print("Lesson {}: {}".format(i, lesson))


# Task 2 - chunker

def chunker(arr, chunkSize):
    i = 0
    while i < len(arr):
        nextChunk = []
        j = 0
        while j < chunkSize:
            if i+j < len(arr):
                nextChunk.append(arr[i+j])
                j += 1
            else:
                break

        yield nextChunk
        i += chunkSize
    

print("\n\nTask 2")
for chunk in chunker(range(25), 4):
    print(list(chunk))