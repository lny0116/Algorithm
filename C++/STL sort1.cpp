#include <iostream>
#include <algorithm> //stl(standard template library) 라이브러리 = 우리가 사용하게 될 sort함수가 정의되어있음. 

using namespace std; // std 클래스 이름 공간을 사용하겠다. 이렇게 선언하면 일일이 표기 안 해도 됌. 

int main(void){
	int a[10] = {9, 3, 5, 4, 1, 10, 8, 6, 7, 2};
	sort(a, a+10); //배열 변수명,  정렬할 데이터 개수 
	for(int i=0;i<10;i++){
		cout << a[i] << ' ';
	}
}
