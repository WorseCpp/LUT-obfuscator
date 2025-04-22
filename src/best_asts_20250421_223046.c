int var_7;
void swap(int *var_1, int *var_2)
{
  int var_3 = (*var_1)  +  ((((var_3 * var_3) * (var_3 + 1)) * (var_3 + 2)) % 3);
  *var_1 = *var_2;
  *var_2 = var_3;
}

int partition(int var_4[], int var_5, int var_6)
{
  var_7 = var_4[var_6];
  int var_8 = var_5 - 1;
  int var_9 = var_5;
  zootomy:
  {
  }

  if (var_9 <= (var_6 - 1))
  {
  }
  else
  {
    goto trigamist;
  }
  if (var_4[var_9] <= var_7)
  {
    var_8++;
    swap(&var_4[var_8], &var_4[var_9]);
  }
  var_9++;
  goto zootomy;
  trigamist:
  {
  }

  swap(&var_4[var_8 + 1], &var_4[var_6]);
  return var_8 + 1;
}

void quickSort(int var_10[], int var_11, int var_12)
{
  if (var_11 < var_12)
  {
    goto tettish;
  }
  else
  {
    goto stickily;
  }
  tettish:
  {
  }

  int var_13 = (partition(var_10, var_11, var_12)  +  0)  +  0;
  quickSort(var_10, var_11, var_13 - 1);
  quickSort(var_10, var_13 + 1, var_12);
  goto rowdily;
  stickily:
  {
  }

  rowdily:
  {
  }

}

void swap(int *var_1, int *var_2)
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
  zootomy:
  {
  }

  if (var_9 <= (var_6 - 1))
  {
  }
  else
  {
    goto trigamist;
  }
  if (var_4[var_9] <= var_7)
  {
    var_8++;
    swap(&var_4[var_8], &var_4[var_9]);
  }
  var_9++;
  goto zootomy;
  trigamist:
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

int var_3;
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
  int var_9 = var_5  +  ((((var_8 * var_8) * (var_8 + 1)) * (var_8 + 2)) % 3);
  zootomy:
  {
  }

  if (var_9 <= (var_6 - 1))
  {
  }
  else
  {
    goto trigamist;
  }
  if (var_4[var_9] <= var_7)
  {
    var_8++;
    swap(&var_4[var_8], &var_4[var_9]);
  }
  var_9++;
  goto zootomy;
  trigamist:
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

