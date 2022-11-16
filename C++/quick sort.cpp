#include <stdio.h>

int number = 10;
int data[10] = {1, 10, 5, 8, 7, 6, 4, 3, 2, 9};

void quicksort(int *data, int start, int end){ //�� ������ �����ϴ� �Լ��� ���� �� [����� �Լ�] 
	if(start >= end){ //���Ұ� 1���� ��� 
		return;
	}
	//�ǹ����� ����� 
	int key = start; // Ű�� ù��° ���� 
	int i = start + 1; // ���ʺ��� �ϳ��� ū ���� ã�� �� �ε���
	int j = end; //�������� ���� ���� ã�� ���� �̵� 
	int temp; //�� ���� ���� ��ġ�� �ٲ� �� �ְ� �ӽ� ���� 
	
	while(i <= j){ //������ ������ �ݺ� 
		while(i <= end && data[i] <= data[key]){ //Ű ������ ū ���� ���� ������ ���������� �̵� 
			i++;
		} 
		while(j > start && data[j] >= data[key]){ // Ű ������ ���� ���� ���� ������ �ݺ�
			j--;
		}
		if(i > j){ // ���� ������ ���¸� Ű ���� ��ü 
			temp = data[j];
			data[j] = data[key];
			data[key] = temp;
		} else { // �������� �ʾҴٸ� 
			temp = data[j];
			data[j] = data[i];
			data[i] = temp;
		}
	}
	// �����Ͱ� �������� �ٱ������� ���� ��� 
	quicksort(data, start, j-1); // Ű ���� �������� ���� 
	quicksort(data, j+1, end); // �����ʿ��� ���� �ٽ� �� ���� ����  
}

int main(void){
	quicksort(data, 0, number - 1); //�ε��� 0���� 9���� ���� ���� 
	for(int i = 0; i < number; i++){ //���ĵ� ������ ���  
		printf("%d ", data[i]); 
	}
} 
