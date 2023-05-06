#개수알고리즘 : 주어진 범위 주어진 조건에 해당하는 자료 개수
#1~1000 까지 정수 중 13의 배수의 개수

#[1] input
count = 0

#[2] process
for i in range(1, 1000): #주어진 범위
	if i % 13 == 0: #주어진 조건
		count += 1
		print(i)

#[3] output
print(f'1부터 1000까지의 정수 중 13의 배수의 개수: {count}')