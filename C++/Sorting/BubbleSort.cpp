#include<iostream>
using namespace std;

int main()
{
	int arr[5];
	int i, j;
	int temp;
	
	cout << "Enter 5 integer elements" << endl;
	for(i=0; i<5; i++)
	{
		cin >> arr[i];
	}
	
	for(i=0; i<5; i++)
	{
		for(j=0; j<=5-i-1; j++)
		{
			if(arr[j] > arr[j+1])
			{
				temp = arr[j];
				arr[j] = arr[j+1];
				arr[j+1] = temp;	
			}
		}
	}
	
	cout << "Your sorted array is ::" << endl;
	for(i=0; i<5; i++)
	{
		cout << arr[i] << " ";
	}
		
	return 0;
}
