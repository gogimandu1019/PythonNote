#[?] 주어진 (지정범위) 데이터의 순위(등수) 구하는 로직

#순위알고리즘 : 점수데이터에 대한 순위 구하기
def main():
	
	#[1] input
	scores = [90, 87, 100, 95, 80] #등수 : 3 4 1 2 5
	n = len(scores)
	rankings = [1] * n #모두 1로 초기화
	print(scores)
	print(rankings)
	
	#[2] process
	for i in range(n):
		rankings[i] = 1 #매 회전마다 순위배열 1등으로 초기화
		for j in range(n):
			if scores[i] < scores[j]: #현재와 나머지 비교
			    rankings[i] += 1 #나보다 큰 점수가 나오면 순위를 1 증가
	
	#[3] output
	for i in range(n):
		print(f"{scores[i]:3}점: {rankings[i]}등")

main()