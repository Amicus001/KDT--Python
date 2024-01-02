#set 데이터 타입
# 가장 마지막에 추가된 타입
# 목적: 중복 데이터 제거
# 특징: 이미 존재하는 데이터는 저장하지 않음
# 문법: {데이터1, 데이터2, 데이터3, ... 데이터n}

#빈 set 작성:
set_a = set()
print(f'set_a = {type(set_a)}, {len(set_a)}개')

print("-"*60)
#생성자 함수 = 타입 이름과 동일한 함수명;
        #heap 영역에 메모리 공간을 잡아두고 데이터 초기화 기능을 수행한다.

# set 타입의 데이터 생성
a1 = {1,2,1,1,3,2,4,5,5,3,4,2,1}

print(f'a1 = {type(a1)}, {len(a1)}개, {a1}')

#다른 데이터타입에서 중복 데이터 제거 시 형변환을 이용하여 활용한다.

#----------------------------------------------------
#set type의 연산 수행

a1 = {1,2,3,5,6}
b1= {1,2,3,4,5,6,7,8,9,0}

#print(a1+b1)

#원소(요소) 읽기/수정/삭제/추가 -> 인덱스나 키가 없는 자료형이므로 메서드 제공
#추가(1개) : add()
#추가(여러 개): update()

a1.update([11,22,33,44])
print(f'a1 = {type(a1)}, {len(a1)}개, {a1}')

a1.update("Happy Birthday !!")
print(f'a1 = {type(a1)}, {len(a1)}개, {a1}')

a1.add("Happy Birthday! !")

#삭제
a1.remove("p")
print(f'a1 = {type(a1)}, {len(a1)}개, {a1}')


#집합에 관련한 메서드/기호, 연산자

#교집합
#: 여러 집합의 공통으로 존재하는 데이터만 추출하기
#: 기호(연산자) : &
#: 메서드 : intersection()

a1.clear()
a1.update("Happy")
print(f'{a1}')

a2 = a1.intersection({'a','A','b','B'})
print(a2)

#합집합
#여러 집합에서 중복은 하나만 포함한 모든 원소의 집합
#연산자: |, or 연산자
#메서드: union

#차집합
#기호: - 뺄셈 연산자
#메서드: difference()


#정렬
# 원소 값을 서로 비교하여 작은 것부터 큰 데이터 순으로 저장(오름차순 정렬)
#set type에는 정렬 메서드가 없음-> 내장함수 sorted()사용

a = sorted(a1)
print(f'a1 = {type(a)}, {a}')