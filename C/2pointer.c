#include <stdio.h>

void MaxAndMin(int *arr, int size, int ** maxPtr, int ** minPtr) {
	int * max, *min;
	int i;

	max = min = &arr[0]; //max와 min값은 arr의 주소를 가리키고 배열은 결국 첫번째 인덱스를 가리키는데 첫번째 인덱스가 1임 == *max랑 *min이 1임 그니까
	for (i = 0; i < size; i++) { //size만큼 돌아 == 4*5 / 4 == 5만큼 돈다
		if (*max < arr[i]) { //처음 기준으로 1<(0번째 인덱스=)1이니까 안돌고, 다음에 i=1일때 인덱스 = 2니까 1<2라 *max값이 2로 바뀜
			max = &arr[i];
		}
		else if (*min > arr[i]) { //여기는 결론적으로 안 돌아. 걍 min은 1인채로 쭉... 높은게 없으니까
			min = &arr[i];
		}
	}

	*maxPtr = max; //5
	*minPtr = min; //1
}

void main()
{
	int * maxPtr; //포인터 변수 선언해주고
	int * minPtr;
	int arr[5]; //arr에 5개 값을 넣어 1,2,3,4,5를 넣어봐
	int i;

	for (i = 0; i < 5; i++) { //i는 0-4까지 5번 돌아
		printf("정수를 입력해주세요 >>> ");
		scanf("%d", &arr[i]); //arr의 주소에 담아
	}

	MaxAndMin(arr, sizeof(arr)/sizeof(int), &maxPtr, &minPtr); //함수 호출
	printf("최대 값 : %d\n최소 값 : %d\n", *maxPtr, *minPtr);
}
