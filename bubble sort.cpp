#include <stdio.h>

int main(void){
	int i, j, temp; //i, j�� �ݺ��� ����, temp�� ���� �ٸ� ��ġ�� �����ϴ� �� ���� ���Ҹ� �ٲٱ� ���� ��� 
	int array [10] = {1, 10, 5, 8, 7, 6, 4, 3, 2, 9};
	for(i=0; i<10; i++){
		for(j=0;j<9-i;j++){ //���� ������ �ڿ������� ������ ũ�⸦ �ϳ��� ���ҽ�Ű�� Ư¡�� �ֱ� ������ -i�� ���� 
			if(array[j]>array[j+1]){ //���� �ִ� �Ͱ� �����ִ� �� 
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
