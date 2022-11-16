#include <stdio.h>

int main(void){
	int i, j, temp; //반복을 위한 i, j. 두 개의 원소값을 서로 바꾸기 위한 일시적인 변수 temp 
	int array[10] = {1, 10, 5, 8, 7, 6, 4, 3, 2, 9};
	for(i = 0; i < 9; i++){
		j = i; //현재 정렬할 원소를 선택해 적절한 위치에 삽입할 수 있게 해줌 
		while(array[j] > array[j + 1]){ //j는 1씩 빼면서 오른쪽 값과 비교해 왼쪽값이 더 크다면 위치를 바꿈 
			temp = array[j];
			array[j]=array[j+1];
			array[j+1]=temp;
			j--;
		}
	}
	for(i=0; i<10; i++){
		printf("%d ", array[i]);
	}
	return 0;
}
