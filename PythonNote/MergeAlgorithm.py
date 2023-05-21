#[?] 2개의 정수배열 합치기 : 오름차순 정렬 가정
#병합알고리즘 : 오름차순 정렬된 정수 배열 2개를 하나로 병합

#[1] input - 정렬되지 않은 배열인 경우 정렬이 필요함
first = [1,3,5]
second = [2,4]

m = len(first)
n = len(second)

merge = [0]* (m+n) #m+n자리만큼 병합데이터 들어갈 배열을 만듦
i = 0
j = 0
k = 0

#[2] process - merge
while (i < m and j < n): #둘다 배열의 끝에 도달할때까지
	if first[i] < second[j]: #작은값을 저장
		merge[k] = first[i]
		k += 1
		i += 1
	else:
		merge[k] = second[j]
		k += 1
		j += 1


while (i < m): #첫번째 배열 first의 끝에 도달하면
	merge[k] = first[i]
	k += 1
	i += 1

while (j < n): #두번째 배열 second의 끝에 도달하면
	merge[k] = second[j]
	k += 1
	j += 1

#[3] output
for item in merge:
	print(item, end = ",")
print()
