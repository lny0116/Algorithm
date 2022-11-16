#include <iostream>
#include <algorithm>

using namespace std;

class student{ //student(자료형) class 객체 - class는 여러개의 변수를 하나로 묶기 위해 사용. 
	public:
		string name;
		int score;
		student(string name, int score){ //생성자 생성, 특정한 객체를 초기화하기 위해서 사용 
			this->name = name;
			this->score = score; //학생의 이름과 점수를 입력 받는 초기화 함수 생성 
		}
		//정렬 기준은 '점수가 작은 순서' 
		bool operator < (student & student){ //연산자 오버로딩 : 왼쪽이 오른쪽보다 작다 
			return this->score < student.score; //정렬 기준은 점수 
		}
};

int main(void){
	student students[]={
		student("나동빈", 90),
		student("이상욱", 93),
		student("박한울", 97),
		student("강종구", 87),
		student("이태일", 92)
	};
	sort(students, students + 5); //위에서 정렬 기준을 정했기 때문에 바로 정렬 수행 
	for(int i =0; i<5; i++){
		cout << students[i].name << ' ';
	}
}
