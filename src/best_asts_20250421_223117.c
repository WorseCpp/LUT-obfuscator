greedy_best_astvoid swap(int *var_1, int *var_2)
{
  int var_3 = (*var_1)  +  (((((var_3 * var_3) * (var_3 + 1)) * (var_3 + 2)) * (var_3 + 3)) % 4);
  *var_1 = *var_2;
  *var_2 = var_3;
}

int partition(int var_4[], int var_5, int var_6)
{
  int var_7 = var_4[var_6];
  int var_8 = var_5 - 1;
  int var_9 = var_5;
  hafted:
  {
  }

  if (var_9 <= (var_6 - 1))
  {
  }
  else
  {
    goto divisionistic;
  }
  if (var_4[var_9] <= var_7)
  {
    goto overmodesty;
  }
  else
  {
    goto outbleated;
  }
  overmodesty:
  {
  }

  goto albumenize;
  goto noticeableness;
  outbleated:
  {
  }

  goto gentlemanliness;
  noticeableness:
  {
  }

  albumenize:
  {
  }

  goto discording;
  goto chenopodiaceous;
  gentlemanliness:
  {
  }

  goto curd;
  chenopodiaceous:
  {
  }

  discording:
  {
  }

  var_8++;
  swap(&var_4[var_8], &var_4[var_9]);
  goto freelances;
  curd:
  {
  }

  freelances:
  {
  }

  var_9++;
  goto hafted;
  divisionistic:
  {
  }

  swap(&var_4[var_8 + 1], &var_4[var_6]);
  return var_8 + 1;
}

void quickSort(int var_10[], int var_11, int var_12)
{
  if (var_11 < var_12)
  {
    goto billabong;
  }
  else
  {
    goto solution;
  }
  billabong:
  {
  }

  int var_13 = partition(var_10, var_11, var_12);
  quickSort(var_10, var_11, var_13 - 1);
  quickSort(var_10, var_13 + 1, var_12);
  goto hydrosulphuret;
  solution:
  {
  }

  hydrosulphuret:
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
  hafted:
  {
  }

  if (var_9 <= (var_6 - 1))
  {
  }
  else
  {
    goto divisionistic;
  }
  if (var_4[var_9] <= var_7)
  {
    var_8++;
    swap(&var_4[var_8], &var_4[var_9]);
  }
  var_9++;
  goto hafted;
  divisionistic:
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

sa_best_astint var_9;
int var_8;
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
  var_8 = var_5 - 1;
  var_9 = var_5;
  hafted:
  {
  }

  if (var_9 <= (var_6 - 1))
  {
    goto quit;
  }
  else
  {
    goto cohesions;
  }
  quit:
  {
  }

  goto sophisticalness;
  cohesions:
  {
  }

  goto divisionistic;
  sophisticalness:
  {
  }

  if (var_4[var_9] <= var_7)
  {
    var_8++;
    swap(&var_4[var_8], &var_4[var_9]);
  }
  var_9++;
  goto hafted;
  divisionistic:
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

