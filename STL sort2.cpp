#include <iostream> //c++ header
#include <vector> //c++�� �̿��� ���� ���α׷����� �� ���� ���� ���̺귯���� ���� ���. 
#include <algorithm>

using namespace std;

int main(void){
	vector<pair<int, string> > v; //pair�� �� ���� ������(1st: int, 2nd: string)�� �ٷ�� ���� ����ϴ� ���̺귯��. 
	v.push_back(pair<int, string>(90, "park")); //push_back = list�� ������ �κп� ������ �ϰڴٴ� �ǹ� 
	v.push_back(pair<int, string>(85, "lee"));
	v.push_back(pair<int, string>(82, "na"));
	v.push_back(pair<int, string>(98, "kang"));
	v.push_back(pair<int, string>(79, "sang"));
	
	sort(v.begin(), v.end()); //�л����� �̸��� ���������� ���� ���� 
	
	for(int i = 0; i<v.size(); i++){ //size�� ���� ���ԵǾ� ���� �ȿ� �� �� ��(5)�� �����Ͱ� �� �ִ��� = �� ������ ũ�⸦ ������. 
		cout << v[i].second << ' '; //second(2nd)�� �θ��� = �̸�(string)�� ���. 
	}
	return 0; 
}
