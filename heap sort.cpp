#include <stdio.h>

int n = 9;
int heap[9] = {7, 6, 5, 8, 3, 5, 9, 1, 6};

int main(void){
	//���� ��ü Ʈ�� ������ �ִ� �� ������ �ٲ�. 
	for(int i=1; i<n; i++){
		int c=i;
		do{
			int root = (c -1)/2; //Ư���� ������ �θ� ����Ű�� �� 
			if(heap[root] < heap[c]){ //�θ��� ������ �ڽ��� ���� �� ũ�� ��ġ �ٲٴ� �ڵ� 
				int temp = heap[root];
				heap[root] = heap[c];
				heap[c] = temp;
			}
			c = root; //�ڽ��� �θ�� �̵� 
		} while (c != 0);
	}
	//ũ�⸦ �ٿ����� �ݺ������� ���� ���� 
	for(int i = n-1; i>=0;i--){
		int temp = heap[0];
		heap[0] = heap[i]; //���� ū ���� 0���� �ε����� �� �ڷ� ������ = �������� ���� 
		heap[i] = temp;
		int root = 0;
		int c = 1;
		do{
			c = 2*root+1;
			// �ڽ� �߿� �� ū ���� ã��
			if(heap[c] < heap[c+1] && c < i-1){ // i-1���� Ŭ �� ���� ���� ���� 
				c++;
			} 
			//��Ʈ���� �ڽ��� �� ũ�ٸ� ��ȯ
			if(heap[root] < heap[c] && c < i){ //root�� ��ġ�� c�� ��ġ�� �ٲ��� 
				int temp = heap[root];
				heap[root] = heap[c];
				heap[c] = temp;
			} 
			root = c; //��������� �� ������ ������� 
		}while (c<i);
	}
	for(int i = 0; i<n;i++){
		printf("%d ",heap[i]); //��� ��� 
	}
}
