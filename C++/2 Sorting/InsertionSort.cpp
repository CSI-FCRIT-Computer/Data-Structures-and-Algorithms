#include<iostream>
using namespace std;

void insertionSort(int arr[])
{
	int key=0;
	int j=0;
	
	for(int i=0; i<5; i++)
	{
		key = arr[i];
		j = i-1;
		
		while(j >= 0 && arr[j] > key)
		{
			arr[j+1] = arr[j];
			j = j-1;
		}
		arr[j+1] = key;
	}
}

int main()
{
	int myarr[5];
	cout << "Enter 5 integer elements" << endl;	
	
	for(int i=0; i<5; i++)
	{
		cin >> myarr[i];
	}
	
	cout << "Before Sorting" << endl;
	for(int i=0; i<5; i++)
	{
		cout << myarr[i] << " ";
	}
	
	insertionSort(myarr);
	cout <<endl<< "After Sorting" << endl;
	for(int i=0; i<5; i++)
	{
		cout << myarr[i] << " ";
	}
	
	return 0;
}