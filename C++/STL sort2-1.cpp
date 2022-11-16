#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

bool compare(pair<string, pair<int, int> >a, pair<string, pair<int,int> >b){ //a, b�л��� ������ �� ���ı��� [2���� �л��� �����ִ� �Լ� ����] 
	if(a.second.first == b.second.first){
		return a.second.second > b.second.second; //��������� ���� �л� �켱���� [� �л�] 
	} else{
		return a.second.first > b.second.first; //������ �ٸ��� ������ ���� �л��� �켱 ������ ����. 
	}
}

int main(void){
	vector<pair<string, pair<int, int> > > v; //���ʴ�� �̸�string, ����int, �������int 
	v.push_back(pair<string, pair<int, int> >("������", pair<int, int>(90, 19961222)));
	v.push_back(pair<string, pair<int, int> >("������", pair<int, int>(97, 19930518)));
	v.push_back(pair<string, pair<int, int> >("���ѿ�", pair<int, int>(95, 19930203)));
	v.push_back(pair<string, pair<int, int> >("�̻��", pair<int, int>(90, 19921207)));
	v.push_back(pair<string, pair<int, int> >("������", pair<int, int>(88, 19900302)));
	
	sort(v.begin(), v.end(),compare); //���ı��ؿ� compare ���� 
	for(int i =0; i<v.size(); i++){
		cout<<v[i].first<<' '; // �л� �̸� �������� ���� ��� ��� 
	}
	return 0;
} //�̷������� pair�� �������� ���ļ� ���� �Ǹ�, ���� ������ �� ���� ��쿡�� ȿ�������� ���α׷��� �� �� �ִ�. 