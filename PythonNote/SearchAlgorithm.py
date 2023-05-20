#검색알고리즘(search algorithm): 주어진 데이터에서 특정 데이터를 찾음
#정렬되어있는 데이터를 이진검색을 사용하여 반띵나눠서 검색
def main():

	#[1]input
	data = [1,3,5,7,9] #오름차순정렬로 가정 - 안되어있는 경우 정렬 필요
	n = len(data)
	search = 3 #검색할 데이터

	flag = False #플래그변수 : 찾으면 true 못찾으면 false
	index = -1 #인덱스변수 초기화

	#[2]process: 이진검색 알고리즘 : FULL-> INDEX SCAN
	low = 0 #min: 낮은 인덱스
	high = n-1 #max: 높은 인덱스

	while low <= high:
		mid = int((low + high) / 2) #중간 인덱스 = 로우 하이 평균, 정수형으로 처리해야
				
		if data[mid] > search: 
			high = mid - 1 #찾을 데이터가 작으면 하이 왼쪽으로 이동
		elif data[mid] < search:
			low = mid + 1 #찾을 데이터가 크면 로우 오른쪽으로 이동
		else:
			flag = True; index=mid; break;

	#[3]output
	if flag:
		print(f"{search}을(를) {index}에서 찾았습니다.")
	else:
		print("찾지 못했습니다")


main()
