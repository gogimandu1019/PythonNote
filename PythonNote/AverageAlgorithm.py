#평균알고리즘 : 주어진 범위/주어진 조건에서 해당하는 자료들의 평균
#[?] n명의 점수 중에서 80점 이상 95점 이하인 점수의 평균

#[1] input : n명의 성적
data = [90, 65, 78, 50, 95]
sum = 0
cnt = 0
n = len(data)
avg = 0.0

#[2] process : avg = sum / cnt
for i in range(0, n) :
	if data[i] >= 80 and data[i] <= 95:
		cnt += 1
		sum += data[i]

if sum != 0 and cnt != 0:
	avg = sum / cnt
else :
	print(f'Error!')

#[3] output
print(f'80점 이상 95점 이하인 자료의 평균 : {avg: .2f}')