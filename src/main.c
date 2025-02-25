#include "stdio.h"


int fib(int i);
float sqr(float x);
float ring(float x);

int dat[10] = {1, 1, 2, 3, 5, 8, 13, 21, 34, 55};

float m_sqr(float x)
{
    return x*x;    
}

float m_ring(float x)
{
    float ctr = 0;
    for (int i = 0; i < 3; i++)
    {
        ctr = m_sqr(ctr + x);
    }
    return ctr;
}

int main()
{
    for (int i =0; i < 10; i++)
    {
        printf("%i ", fib(i));
        if (fib(i) != dat[i] | m_sqr(i) != sqr(i) | m_ring(i) != ring(i))
        {
            return 0;
        }
    }
    return 1;
}