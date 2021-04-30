#include <iostream> //c++ header
#include <vector> //c++을 이용해 각종 프로그래밍을 할 때는 벡터 라이브러리를 많이 사용. 
#include <algorithm>

using namespace std;

int main(void){
	vector<pair<int, string> > v; //pair는 한 쌍의 데이터(1st: int, 2nd: string)를 다루기 위해 사용하는 라이브러리. 
	v.push_back(pair<int, string>(90, "park")); //push_back = list의 마지막 부분에 삽입을 하겠다는 의미 
	v.push_back(pair<int, string>(85, "lee"));
	v.push_back(pair<int, string>(82, "na"));
	v.push_back(pair<int, string>(98, "kang"));
	v.push_back(pair<int, string>(79, "sang"));
	
	sort(v.begin(), v.end()); //학생들의 이름이 성적순으로 정렬 수행 
	
	for(int i = 0; i<v.size(); i++){ //size는 현재 삽입되어 벡터 안에 총 몇 개(5)의 데이터가 들어가 있는지 = 즉 벡터의 크기를 가져옴. 
		cout << v[i].second << ' '; //second(2nd)를 부르면 = 이름(string)을 출력. 
	}
	return 0; 
}
