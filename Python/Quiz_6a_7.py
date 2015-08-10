n = 100
numbers = range(2,n)
results = []

while numbers != []:
    results.append(numbers[0])
    for i in numbers:
        if i % results[-1] == 0:
            numbers.remove(i)
        else:
            pass

print len(results)
#print results