#include <stdio.h>

int main(void){
	int i, j, temp; //i, j는 반복을 위해, temp는 서로 다른 위치에 존재하는 두 개의 원소를 바꾸기 위해 사용 
	int array [10] = {1, 10, 5, 8, 7, 6, 4, 3, 2, 9};
	for(i=0; i<10; i++){
		for(j=0;j<9-i;j++){ //버블 정렬은 뒤에서부터 집합의 크기를 하나씩 감소시키는 특징이 있기 때문에 -i를 해줌 
			if(array[j]>array[j+1]){ //옆에 있는 것과 비교해주는 식 
			temp = array[j];
			array[j] = array[j+1];
			array[j+1] = temp;
			}
		}
	}
	for(i=0;i<10;i++){
	printf("%d ", array[i]);
	}
	return 0;
}
