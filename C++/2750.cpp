#include <stdio.h>
//���� ���ķ� ǰ. 
int array[1001]; //�迭�� �ε����� 0���� 1000���� ���� �� �ֵ��� �������� ������ +1�� �������ִ� �� ����. 

int main(void){
	int i, j, num, min, index, temp;
	
	scanf("%d", &num); //�������� ���� �Է� ���� 
	
	for(i=0; i<num; i++){
		scanf("%d", &array[i]); //�����Ͱ� � ������ �Է� ����. 
	}
	for(i=0; i<num; i++){ //���� ���� [�ּҰ�] 
		min = 1001; // �� ū �� �־���. 
		
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
