#include <iostream>

using namespace std;

int main()
{
	int N;
	cout << "\n Array size : ";
	cin >> N;

	int A[N];
	cout << "\n Enter elements (ascending order) : ";

	for(int i = 0; i < N; ++i)
		cin >> A[i];

	int element;
	cout << "\n Enter element to be searched : ";
	cin >> element;

	// Binary Search

	int left = 0, right = N, mid;

	while(right > left + 1)
	{
		mid = int((left + right)/2);

		if(element <= A[mid])
			right = mid;
		
		else if(element > A[mid]) 
			left = mid;
	}
	
	if (A[left] == element)
		cout << "\n Element " << element << " found at index : " << left << endl;
	else if (A[right] == element)
		cout << "\n Element " << element << " found at index : " << right << endl;
	else
		cout << "\n Element not found\n";

	return 0;
}