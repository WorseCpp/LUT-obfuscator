#include "stdio.h"


void quickSort(int arr[], int low, int high);

#define len 15

int main()
{
    int m_arr[len];

    for (int i = 0; i < 10; i++)
    {

        for(int j = 0; j < len; j++)
        {
            m_arr[j] = rand();
        }

        quickSort(m_arr, 0, len-1);

        for(int j = 0; j < len-1; j++)
        {
            if (m_arr[j] > m_arr[j+1])
            {
                return 0;
            } 
        }

    }

    return 1;
}