int var_1 = 0;
float var_6 = 0;
float var_8 = 0;
int fib()
{
  int var_2 = 1;
  int var_3 = 1;
  int var_4 = var_2 + var_3;
  if ((var_1 == 0) | (var_1 == 1))
  {
    return 1;
  }
  if (var_1 >= 20)
  {
    return -1;
  }
  for (int var_5 = 0; var_5 < (var_1 - 2); var_5++)
  {
    var_2 = var_3;
    var_3 = var_4;
    var_4 = var_2 + var_3;
  }

  return var_4;
}

float sqr()
{
  return var_6 * var_6;
}

float ring(float var_7)
{
  for (int var_9 = 0; var_9 < 3; var_9++)
  {
    var_6 = var_8 + var_7;
    var_8 = sqr();
  }

  return var_8;
}

