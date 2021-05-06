#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

bool compare(pair<string, pair<int, int> >a, pair<string, pair<int,int> >b){ //a, b학생이 존재할 때 정렬기준 [2명의 학생을 비교해주는 함수 정의] 
	if(a.second.first == b.second.first){
		return a.second.second > b.second.second; //생년월일이 느린 학생 우선순위 [어린 학생] 
	} else{
		return a.second.first > b.second.first; //성적이 다르면 성적이 높은 학생이 우선 순위가 높게. 
	}
}

int main(void){
	vector<pair<string, pair<int, int> > > v; //차례대로 이름string, 성적int, 생년월일int 
	v.push_back(pair<string, pair<int, int> >("나동빈", pair<int, int>(90, 19961222)));
	v.push_back(pair<string, pair<int, int> >("이태일", pair<int, int>(97, 19930518)));
	v.push_back(pair<string, pair<int, int> >("박한울", pair<int, int>(95, 19930203)));
	v.push_back(pair<string, pair<int, int> >("이상욱", pair<int, int>(90, 19921207)));
	v.push_back(pair<string, pair<int, int> >("강종구", pair<int, int>(88, 19900302)));
	
	sort(v.begin(), v.end(),compare); //정렬기준에 compare 삽입 
	for(int i =0; i<v.size(); i++){
		cout<<v[i].first<<' '; // 학생 이름 기준으로 정렬 결과 출력 
	}
	return 0;
} //이런식으로 pair를 이중으로 겹쳐서 쓰게 되면, 정렬 기준이 두 개인 경우에도 효과적으로 프로그래밍 할 수 있다. 
