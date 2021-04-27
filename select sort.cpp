#include <stdio.h>

int main(void) {
	int i, j, min, index, temp; //i,j는 배열에 있는 원소를 반복적으로 탐색하기 위해 사용, min은 최소값, index 가장 작은 원소가 존재하는 위치, temp는 특정한 두 수를 바꾸기 위해 사용 
	int	array[10] = {1, 10, 5, 8, 7, 6, 4, 3, 2, 9}; //문제의 배열 
	for(i=0; i<10; i++){
		min = 9999; // 더 큰 숫자를 무작위로 넣은 것. 있는 수를 넣지X 
		for(j=i; j < 10; j++){
			if(min > array[j]){ //최소값을 골라줌 
				min = array[j]; //최소값을 탐색하고 있는 원소로 바꿔줌 
				index = j; // 해당 위치 값을 넣어줌 
			}// 작은 값 선택 완료 
		}
		temp = array[i]; //가장 앞 값을 넣어줌 
		array[i] = array[index]; //가장 앞에 있는 값을 최소값으로 넣어준 뒤 
		array[index] = temp; //최소값 위치에 temp값을 넣어줌 = 세 줄을 합쳐 스와핑이라고 함 
	}
	for(i=0; i<10; i++){ //정렬이 된 원소 출력 
		printf("%d", array[i]);
	}
	return 0;
}
