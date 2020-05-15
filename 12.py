A = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]
num = -1
sum = 0
while num < 9:
	num += 1
	if A[num] < 50: continue
	sum = sum + A[num]
print(sum)