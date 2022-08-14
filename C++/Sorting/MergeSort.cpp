#include <iostream>
using namespace std;

void merge(int arr[], int l, int m, int r)
{
	int i = l;	//starting index for left sub array
	int j = m+1; 	// mid element index
	int k = l;    //last element index
	int temp[5];
	
	while(i<=m && j<=r)
	{
		if(arr[i] <= arr[j])
		{
			temp[k] = arr[i];
			i++;
			k++;
		}
		else
		{
			temp[k] = arr[j];
			j++;
			k++;
		}
	}
	while(i<=m)
	{
		temp[k] = arr[i];
		i++;
		k++;
	}
	while(j<=r)
	{
		temp[k] = arr[j];
		j++;
		k++;
	}
	for(int p=l; p<=r; p++) 	
	{
		arr[p] = temp[p];
	}
	
}

void mergeSort(int arr[], int l, int r)
{
	if(l<r)
	{
		int m = (l+r)/2;
		mergeSort(arr,0,m);
		mergeSort(arr,m+1,r);
		merge(arr,l,m,r);
	}
}


int main()
{
	int myarr[5];
	cout << "Enter 5 integers \n"; 
	for(int i=0; i<5; i++)
	{
		cin >> myarr[i];
	}
	
	cout << "Before Sorting \n"; 
	for(int i=0; i<5; i++)
	{
		cout << myarr[i] << " ";
	}
	
	mergeSort(myarr,0,4);  // func calling
	
	cout << "\n After Sorting \n"; 
	for(int i=0; i<5; i++)
	{
		cout << myarr[i] << " ";
	}
	
	
	return 0;
}