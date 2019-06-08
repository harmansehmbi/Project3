data = [10, 20, 90, 80, 90]

# lenght = len(data)
# print(length)

print(len(data))
print(max(data))
print(min(data))

print()

# Iterate in List

for i in range(len(data)):
    print(data[i])

print()

# Enhanced For Loop/ For-Each Loop

for elm in data:          # elm word can be anything ,... name doesnt matter
    print(elm)

# works on both homo and hetro


print()

print([x**2 for x in data])