#include <iostream>
#include <algorithm>

using namespace std;

bool compare(int a,int b){ //boolean = true, false ���� �̿��� ������ ������ �ľ� 
	return a > b; //�������� ���� 
}

int main(void){
	int a[10] = {9, 3, 5, 4, 1, 10, 8, 6, 7, 2};
	sort(a, a+10, compare); //compare�� ���ٸ� ������������ ���ĵǴ� ���� ����, �⺻������ �������� �����̶�� ���� �� �� ����. �������� ��ȯ���� �����ϰ� compare�� ������ ����Ǵ� ���� �� �� ����. 
	for(int i=0;i<10;i++){
		cout << a[i] << ' ';
	}
}
