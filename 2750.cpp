#include <stdio.h>
//선택 정렬로 품. 
int array[1001]; //배열의 인덱스가 0부터 1000까지 가질 수 있도록 데이터의 개수에 +1로 선언해주는 게 좋다. 

int main(void){
	int i, j, num, min, index, temp;
	
	scanf("%d", &num); //데이터의 개수 입력 받음 
	
	for(i=0; i<num; i++){
		scanf("%d", &array[i]); //데이터가 어떤 것인지 입력 받음. 
	}
	for(i=0; i<num; i++){ //정렬 시작 [최소값] 
		min = 1001; // 더 큰 값 넣어줌. 
		
		for(j=i;j<num;j++){
			if(min>array[j]){
				min = array[j];
				index = j;
				}	
			}
			temp = array[i];
			array[i] = array[index];
			array[index] = temp;	
		}
	for(i=0;i<num;i++){
		printf("%d\n", array[i]);
	}
	return 0;
}
