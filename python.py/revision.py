



def generate_evens(limit):
    for i in range(limit):
        if i % 2 == 0:
            yield i
limit = 10
# gen = generate_evens(limit)

# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))

for num in generate_evens(limit):
    print(num)

