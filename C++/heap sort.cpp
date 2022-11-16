#include <stdio.h>

int n = 9;
int heap[9] = {7, 6, 5, 8, 3, 5, 9, 1, 6};

int main(void){
	//먼저 전체 트리 구조를 최대 힙 구조로 바꿈. 
	for(int i=1; i<n; i++){
		int c=i;
		do{
			int root = (c -1)/2; //특정한 원소의 부모를 가리키게 됨 
			if(heap[root] < heap[c]){ //부모의 값보다 자식의 값이 더 크면 위치 바꾸는 코드 
				int temp = heap[root];
				heap[root] = heap[c];
				heap[c] = temp;
			}
			c = root; //자식의 부모로 이동 
		} while (c != 0);
	}
	//크기를 줄여가며 반복적으로 힙을 구성 
	for(int i = n-1; i>=0;i--){
		int temp = heap[0];
		heap[0] = heap[i]; //가장 큰 값인 0번쨰 인덱스를 맨 뒤로 보내줌 = 오름차순 정렬 
		heap[i] = temp;
		int root = 0;
		int c = 1;
		do{
			c = 2*root+1;
			// 자식 중에 더 큰 값을 찾기
			if(heap[c] < heap[c+1] && c < i-1){ // i-1보다 클 수 없게 범위 지정 
				c++;
			} 
			//루트보다 자식이 더 크다면 교환
			if(heap[root] < heap[c] && c < i){ //root의 위치와 c의 위치를 바꿔줌 
				int temp = heap[root];
				heap[root] = heap[c];
				heap[c] = temp;
			} 
			root = c; //재귀적으로 힙 구조를 만들어줌 
		}while (c<i);
	}
	for(int i = 0; i<n;i++){
		printf("%d ",heap[i]); //결과 출력 
	}
}
