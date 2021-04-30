#include <iostream>
#include <algorithm>

using namespace std;

class student{ //student(�ڷ���) class ��ü - class�� �������� ������ �ϳ��� ���� ���� ���. 
	public:
		string name;
		int score;
		student(string name, int score){ //������ ����, Ư���� ��ü�� �ʱ�ȭ�ϱ� ���ؼ� ��� 
			this->name = name;
			this->score = score; //�л��� �̸��� ������ �Է� �޴� �ʱ�ȭ �Լ� ���� 
		}
		//���� ������ '������ ���� ����' 
		bool operator < (student & student){ //������ �����ε� : ������ �����ʺ��� �۴� 
			return this->score < student.score; //���� ������ ���� 
		}
};

int main(void){
	student students[]={
		student("������", 90),
		student("�̻��", 93),
		student("���ѿ�", 97),
		student("������", 87),
		student("������", 92)
	};
	sort(students, students + 5); //������ ���� ������ ���߱� ������ �ٷ� ���� ���� 
	for(int i =0; i<5; i++){
		cout << students[i].name << ' ';
	}
}
