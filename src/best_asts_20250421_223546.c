greedy_best_astint var_13;
int var_8;
void swap(int *var_1, int *var_2)
{
  int var_3 = *var_1;
  *var_1 = (*var_2) + ((((((var_8 * var_8) * (var_8 + 1)) * (var_8 + 2)) * (var_8 + 3)) * (var_8 + 4)) % 5);
  *var_2 = var_3;
}

int partition(int var_4[], int var_5, int var_6)
{
  int var_7 = var_4[var_6];
  var_8 = var_5 - 1;
  int var_9 = var_5;
  resumed:
  {
  }

  if (var_9 <= (var_6 - 1))
  {
  }
  else
  {
    goto asyndeton;
  }
  if (var_4[var_9] <= var_7)
  {
    goto refiled;
  }
  else
  {
    goto metencephalons;
  }
  refiled:
  {
  }

  var_8++;
  swap(&var_4[var_8], &var_4[var_9]);
  goto retruding;
  metencephalons:
  {
  }

  retruding:
  {
  }

  var_9++;
  goto resumed;
  asyndeton:
  {
  }

  swap(&var_4[var_8 + 1], &var_4[var_6]);
  return var_8 + 1;
}

void quickSort(int var_10[], int var_11, int var_12)
{
  if (var_11 < var_12)
  {
    goto successfulness;
  }
  else
  {
    goto agisting;
  }
  successfulness:
  {
  }

  var_13 = partition(var_10, var_11, var_12);
  quickSort(var_10, var_11, var_13 - 1);
  quickSort(var_10, var_13 + 1, var_12);
  goto steid;
  agisting:
  {
  }

  steid:
  {
  }

}

grad_best_astvoid swap(int *var_1, int *var_2)
{
  int var_3 = *var_1;
  *var_1 = *var_2;
  *var_2 = var_3;
}

int partition(int var_4[], int var_5, int var_6)
{
  int var_7 = var_4[var_6];
  int var_8 = var_5 - 1;
  int var_9 = var_5;
  resumed:
  {
  }

  if (var_9 <= (var_6 - 1))
  {
  }
  else
  {
    goto asyndeton;
  }
  if (var_4[var_9] <= var_7)
  {
    var_8++;
    swap(&var_4[var_8], &var_4[var_9]);
  }
  var_9++;
  goto resumed;
  asyndeton:
  {
  }

  swap(&var_4[var_8 + 1], &var_4[var_6]);
  return var_8 + 1;
}

void quickSort(int var_10[], int var_11, int var_12)
{
  if (var_11 < var_12)
  {
    int var_13 = partition(var_10, var_11, var_12);
    quickSort(var_10, var_11, var_13 - 1);
    quickSort(var_10, var_13 + 1, var_12);
  }
}

sa_best_astint var_3;
void swap(int *var_1, int *var_2)
{
  var_3 = *var_1;
  *var_1 = *var_2;
  *var_2 = var_3;
}

int partition(int var_4[], int var_5, int var_6)
{
  int var_7 = var_4[var_6];
  int var_8 = var_5 - 1;
  int var_9 = var_5;
  resumed:
  {
  }

  if (var_9 <= (var_6 - 1))
  {
  }
  else
  {
    goto asyndeton;
  }
  if (var_4[var_9] <= var_7)
  {
    var_8++;
    swap(&var_4[var_8], &var_4[var_9]);
  }
  var_9++;
  goto resumed;
  asyndeton:
  {
  }

  swap(&var_4[var_8 + 1], &var_4[var_6]);
  return var_8 + 1;
}

void quickSort(int var_10[], int var_11, int var_12)
{
  if (var_11 < var_12)
  {
    int var_13 = partition(var_10, var_11, var_12);
    quickSort(var_10, var_11, var_13 - 1);
    quickSort(var_10, var_13 + 1, var_12);
  }
}

