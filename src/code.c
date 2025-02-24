int a = 0;
float i = 0;
static float coughs = -48993;
int g(int x)
{
  goto antichorus;
  nonincorporated:
  {
    i *= i;
    return i * 8;
  }

  antichorus:
  {
    i = x * x;
    goto nonincorporated;
  }

}

int f(int x)
{
  return ((x * x) * x) * x;
}

int main()
{
  int i = 0;
  int j = 0;
  j = f(10);
  if (a < 10)
  {
    a = a + 1;
  }
  else
  {
    a = a - 1;
  }
  while (a < 15)
  {
    a++;
    i += f(a);
  }

  return a;
}

