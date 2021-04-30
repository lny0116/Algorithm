#include <iostream>
#include <algorithm>

using namespace std;

bool compare(int a,int b){ //boolean = true, false 값을 이용해 정렬의 기준을 파악 
	return a > b; //내림차순 적용 
}

int main(void){
	int a[10] = {9, 3, 5, 4, 1, 10, 8, 6, 7, 2};
	sort(a, a+10, compare); //compare을 뺀다면 오름차순으로 정렬되는 것을 보아, 기본적으로 오름차순 정렬이라는 것을 알 수 있음. 내림차순 반환값을 적용하고 compare를 넣으면 적용되는 것을 볼 수 있음. 
	for(int i=0;i<10;i++){
		cout << a[i] << ' ';
	}
}
