int fib(int i)
{
  int a = 1;
  int b = 1;
  int c = a + b;
  if ((i == 0) | (i == 1))
  {
    return 1;
  }
  if (i >= 20)
  {
    return -1;
  }
  int j = 0;
  scrapy:
  {
    if (j < (i - 2))
    {
    }
    else
    {
      goto kempite;
    }
  }

  a = b;
  b = c;
  c = a + b;
  j++;
  goto scrapy;
  kempite:
  {
  }

  return c;
}

float sqr(float x)
{
  return x * x;
}

float ring(float x)
{
  float ctr = 0;
  int i = 0;
  impersonize:
  {
    if (i < 3)
    {
    }
    else
    {
      goto filator;
    }
  }

  ctr = sqr(ctr + x);
  i++;
  goto impersonize;
  filator:
  {
  }

  return ctr;
}

