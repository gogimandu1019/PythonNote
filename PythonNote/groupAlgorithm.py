#그룹 알고리즘: 특정 키값에 해당하는 그룹화된 합계 리스트 만들기
#[?] 컬렉션형태의 데이터를 특정 키값으로 그룹화

#테스트용 레코드클래스
class Record():
	def __init__(self, name, quantity):
		self.name = name #상품명
		self.quantity = quantity #수량


def main():
	#[1] input
	records = [Record("RADIO",3), Record("TV",1), Record("RADIO",2), Record("DVD",4)]
	groups = [] #출력데이터
	n = len(records)

	#[2] process : group algorithm - sort -> sum -> group
	#[a] sort
	for i in range (n-1):
		for j in range( i+1, n):
			if (records[i].name > records[j].name):
				temp = records[i]
				records[i] = records[j]
				records[j] = temp #swap

	#[b] group
	subtotal = 0 #소계 변수초기화
	for i in range(n):
		subtotal = subtotal + records[i].quantity #같은 상품명의 수량을 누적
		#다음 레코드가 없거나, 현재레코드와 다음레코드가 다르면 저장
		if (((i+1) == n) or (records[i].name != records[i+1].name)) :
			#한 그룹의 키값을 지정하고 소계를 구함
			groups.append(Record(records[i].name, subtotal))
			subtotal = 0 #소계 초기화



	#[3] output
	print("[1] 정렬된 원본데이터 : ")
	for r in records:
		print(f"{r.name.rjust(6)} - {r.quantity}")

	print("[2] 이름으로 그룹화된 데이터 : ")
	for g in groups:
		print(f"{g.name.rjust(6)} - {g.quantity}")

main()