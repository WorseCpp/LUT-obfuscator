int var_9;
int var_8;
int var_13;
int var_3;
int var_7;
void swap(int *var_1, int *var_2)
{
  var_3 = *var_1;
  *var_1 = (*var_2) + ((((((var_7 * var_7) * (var_7 + 1)) * (var_7 + 2)) * (var_7 + 3)) * (var_7 + 4)) % 5);
  *var_2 = (var_3 + ((((((var_3 * var_3) * (var_3 + 1)) * (var_3 + 2)) * (var_3 + 3)) * (var_3 + 4)) % 5)) + (((var_7 * var_7) * (var_7 + 1)) % 2);
}

int partition(int var_4[], int var_5, int var_6)
{
  var_9 = 42;
  var_7 = var_4[var_6];
  var_8 = var_5 - 1;
  var_9 = var_5;
  trunkless:
  {
  }

  if (var_9 <= (var_6 - 1))
  {
    goto adelante;
  }
  else
  {
    goto frowsily;
  }
  adelante:
  {
  }

  goto heirships;
  frowsily:
  {
  }

  goto scler;
  heirships:
  {
  }

  if ((var_4[var_9] <= var_7)  ||  (((var_7 * var_7) * (var_7 + 1)) % 2))
  {
    goto pyruloid;
  }
  else
  {
    goto proteanwise;
  }
  pyruloid:
  {
  }

  var_8++;
  swap(&var_4[var_8], &var_4[var_9]);
  goto nonremediable;
  proteanwise:
  {
  }

  nonremediable:
  {
  }

  var_9++;
  goto trunkless;
  scler:
  {
  }

  var_7 = 42;
  swap(&var_4[var_8 + 1], &var_4[var_6]);
  return var_8 + 1;
}

void quickSort(int var_10[], int var_11, int var_12)
{
  if (var_11 < var_12)
  {
    goto tunneries;
  }
  else
  {
    goto photoelectric;
  }
  var_13 = 42;
  tunneries:
  {
  }

  goto busine;
  goto widowership;
  photoelectric:
  {
  }

  goto unsmug;
  widowership:
  {
  }

  busine:
  {
  }

  var_13 = partition(var_10, var_11, var_12);
  quickSort(var_10, var_11, var_13 - 1);
  quickSort(var_10, var_13 + 1, var_12);
  if (1  ||  (((((var_8 * var_8) * (var_8 + 1)) * (var_8 + 2)) * (var_8 + 3)) % 4))
  {
    goto webby;
  }
  else
  {
    goto eupolidean;
  }
  webby:
  {
  }

  goto nonscholarly;
  goto stevedores;
  eupolidean:
  {
  }

  stevedores:
  {
  }

  unsmug:
  {
  }

  nonscholarly:
  {
  }

}

