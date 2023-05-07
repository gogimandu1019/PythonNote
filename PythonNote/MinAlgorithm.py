import sys	

#주어진 데이터 중 가장 작은 짝수 구하기
def main():
	#[0] initialize
	min = sys.maxsize;	#숫자형식 데이터 중 가장 작은값으로 초기화

	#[1] input
	numbers = [2, 5, 3, 7, 1]; #min = -7
	n = len(numbers)

	#[2] process	
	for i in range(0, n): #주어진 범위
		if numbers[i] < min: #더 작은 데이터가 있다면
			if numbers[i] % 2 == 0 :	#그리고 그 수가 짝수이면
				min = numbers[i] #min에 그 데이터를 할당
	
	#[3] output
	print(f'최솟값: {min}')

main()