import itertools

numbers = [2.50,4.99,5.60,2.00,1.50,1.00,0.50]
desiredSum = 3.00
combs = []

#permuting
depth = 2
while depth <= len(numbers):
   combs.append((itertools.combinations(numbers,depth)))
   depth += 1

#adding
outcomes = []
for combinations in combs:
    l = list(combinations)
    for comb in l:
        total = sum(comb)
        outcomes.append((comb,total))

#reporting
correct = []
for item in outcomes:
    if item[1] == desiredSum:
        correct.append(item)

if len(correct) > 0:
    print("Potential combinations are:")
    for combo in correct:
        print(combo[0])
else:
    print("There are no combinations that result in "+str(desiredSum))