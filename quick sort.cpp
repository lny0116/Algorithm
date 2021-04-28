#include <stdio.h>

int number = 10;
int data[10] = {1, 10, 5, 8, 7, 6, 4, 3, 2, 9};

void quicksort(int *data, int start, int end){ //퀵 정렬을 수행하는 함수를 만든 것 [재귀적 함수] 
	if(start >= end){ //원소가 1개인 경우 
		return;
	}
	//피벗값을 잡아줌 
	int key = start; // 키는 첫번째 원소 
	int i = start + 1; // 왼쪽부터 하나씩 큰 값을 찾을 때 인덱스
	int j = end; //왼쪽으로 작은 값을 찾기 위해 이동 
	int temp; //두 가지 값의 위치를 바꿀 수 있게 임시 변수 
	
	while(i <= j){ //엇갈릴 때까지 반복 
		while(i <= end && data[i] <= data[key]){ //키 값보다 큰 값을 만날 때까지 오른쪽으로 이동 
			i++;
		} 
		while(j > start && data[j] >= data[key]){ // 키 값보다 작은 값을 만날 때까지 반복
			j--;
		}
		if(i > j){ // 현재 엇갈린 상태면 키 값과 교체 
			temp = data[j];
			data[j] = data[key];
			data[key] = temp;
		} else { // 엇갈리지 않았다면 
			temp = data[j];
			data[j] = data[i];
			data[i] = temp;
		}
	}
	// 데이터가 엇갈려서 바깥쪽으로 빠진 경우 
	quicksort(data, start, j-1); // 키 값을 기준으로 왼쪽 
	quicksort(data, j+1, end); // 오른쪽에서 각각 다시 퀵 정렬 수행  
}

int main(void){
	quicksort(data, 0, number - 1); //인덱스 0부터 9까지 정렬 수행 
	for(int i = 0; i < number; i++){ //정렬된 데이터 출력  
		printf("%d ", data[i]); 
	}
} 
