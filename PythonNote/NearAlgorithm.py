#[?] 원본데이터 중 대상 데이터와 가장 가까운 값
import sys
#근삿값 알고리즘 : 가까운 값 = 차이값의 절댓값의 최솟값
def main():
	#[0] initialize
	min = sys.maxsize

	#[1] input
	numbers = [10, 20, 30, 27, 17]
	n = len(numbers)
	target = 25
	near = 0
		
	#[2] process
	for i in range(0, n):
		_abs = abs(numbers[i] - target)	#차이값의 절댓값
		if _abs < min:
			min = _abs #최솟값 알고리즘 활용 : 최솟값변수에 저장
			near = numbers[i] #그 때의 근삿값을 near에 저장

	#[3] output
	print(f'{target} 와/과 가장 가까운 값 : {near} (차이: {min})')

main()