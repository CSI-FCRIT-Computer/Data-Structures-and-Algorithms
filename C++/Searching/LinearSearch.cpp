#include <iostream>

using namespace std;

int main()
{
	int N;
	cout << "\n Array size : ";
	cin >> N;

	int A[N];
	cout << "\n Enter elements : ";

	for(int i = 0; i < N; ++i)
		cin >> A[i];

	int element;
	cout << "\n Enter element to be searched : ";
	cin >> element;

	for(int i = 0; i < N; ++i)
	{
		if(A[i] == element)
		{
			cout << "\n Element " << element << " found at index : " << i << endl;
		}
	}

	return 0;
}