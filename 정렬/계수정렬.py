# 계수 정렬
# counting sort
# count 하는 방식으로 하는 정렬 알고리즘

# 1. 가장 작은 데이터부터 가장 큰 데이터까지의 범위가 모두 담길 수 있도록 리스트를 생성
# 2. 각각의 데이터가 몇 번 등장했는지 기록한다. 따라서 인덱스 배열이랑 개수 배열이 따로 있음
# 3. 데이터의 값과 동일한 인덱스의 데이터를 1씩 증가시킨다.

array = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2] # 최소와 최대를 포함하는 배열이 있어야 함

count = [0] * (max(array) + 1)

for i in range(len(array)) :
    count[array[i]] += 1
    
for i in range(len(count)) :
    for j in range(count[i]) :
        print(i, end = ' ')
