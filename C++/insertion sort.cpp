#include <stdio.h>

int main(void){
	int i, j, temp; //�ݺ��� ���� i, j. �� ���� ���Ұ��� ���� �ٲٱ� ���� �Ͻ����� ���� temp 
	int array[10] = {1, 10, 5, 8, 7, 6, 4, 3, 2, 9};
	for(i = 0; i < 9; i++){
		j = i; //���� ������ ���Ҹ� ������ ������ ��ġ�� ������ �� �ְ� ���� 
		while(array[j] > array[j + 1]){ //j�� 1�� ���鼭 ������ ���� ���� ���ʰ��� �� ũ�ٸ� ��ġ�� �ٲ� 
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
