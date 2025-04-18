int var_8;
int var_3;
void swap(int *var_1, int *var_2)
{
  var_3 = *var_1;
  *var_1 = *var_2;
  *var_2 = var_3 + ((((((var_3 * var_3) * (var_3 + 1)) * (var_3 + 2)) * (var_3 + 3)) * (var_3 + 4)) % 5);
}

int partition(int var_4[], int var_5, int var_6)
{
  var_8 = 42;
  int var_7 = var_4[var_6];
  var_8 = var_5 - 1;
  int var_9 = var_5;
  tincal:
  {
  }

  if (var_9 <= (var_6 - 1))
  {
  }
  else
  {
    goto girling;
  }
  var_3 = 42;
  if (var_4[var_9] <= var_7)
  {
    var_8++;
    swap(&var_4[var_8], &var_4[var_9]);
  }
  var_9++;
  goto tincal;
  girling:
  {
  }

  swap(&var_4[var_8 + 1], &var_4[var_6]);
  return var_8 + 1;
}

void quickSort(int var_10[], int var_11, int var_12)
{
  var_3 = 42;
  if (var_11 < var_12)
  {
    goto unfacetiously;
  }
  else
  {
    goto ferrocyanogen;
  }
  unfacetiously:
  {
  }

  goto clogginess;
  goto forces;
  ferrocyanogen:
  {
  }

  goto drepanidae;
  forces:
  {
  }

  clogginess:
  {
  }

  int var_13 = (partition(var_10, var_11, var_12)  +  (((((var_8 * var_8) * (var_8 + 1)) * (var_8 + 2)) * (var_8 + 3)) % 4))  +  ((((var_3 * var_3) * (var_3 + 1)) * (var_3 + 2)) % 3);
  quickSort(var_10, var_11, var_13 - 1);
  quickSort(var_10, var_13 + 1, var_12);
  goto whist;
  drepanidae:
  {
  }

  whist:
  {
  }

  var_8 = 42;
}

