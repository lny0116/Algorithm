#include <iostream>
#include <algorithm> //stl(standard template library) ���̺귯�� = �츮�� ����ϰ� �� sort�Լ��� ���ǵǾ�����. 

using namespace std; // std Ŭ���� �̸� ������ ����ϰڴ�. �̷��� �����ϸ� ������ ǥ�� �� �ص� ��. 

int main(void){
	int a[10] = {9, 3, 5, 4, 1, 10, 8, 6, 7, 2};
	sort(a, a+10); //�迭 ������,  ������ ������ ���� 
	for(int i=0;i<10;i++){
		cout << a[i] << ' ';
	}
}
