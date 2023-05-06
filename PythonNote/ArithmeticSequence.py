#등차수열(arithmetic) : 연속하는 두 수의 차이가 일정한 수열
#[?] 1부터 20까지 정수 중 홀수의 합을 구하는 프로그램

#[1] input
sum = 0

#[2] process
for i in range(1,20): #주어진 범위
    if i%2 != 0 : #주어진 조건 : 홀수 필터링
        sum = sum + i
        print(sum, end='\n')
#[3] output
print(f'1부터 20까지의 홀수의 합: {sum}')