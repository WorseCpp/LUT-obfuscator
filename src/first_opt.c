int var_8;
int long var_13;
int var_9;
int volatile unsigned long var_7;
int var_3;
void swap(int *var_1, int *var_2)
{
  var_3 = (*var_1)  +  (((var_3 * var_3) * (var_3 + 1)) % 2);
  *var_1 = ((*var_2) + ((((((var_7 * var_7) * (var_7 + 1)) * (var_7 + 2)) * (var_7 + 3)) * (var_7 + 4)) % 5)) + ((((((var_7 * var_7) * (var_7 + 1)) * (var_7 + 2)) * (var_7 + 3)) * (var_7 + 4)) % 5);
  *var_2 = (var_3 + (((var_3 * var_3) * (var_3 + 1)) % 2)) + ((((var_13 * var_13) * (var_13 + 1)) * (var_13 + 2)) % 3);
}

int partition(int var_4[], int var_5, int var_6)
{
  var_7 = (var_4[var_6] + ((((var_7 * var_7) * (var_7 + 1)) * (var_7 + 2)) % 3)) + ((((var_7 * var_7) * (var_7 + 1)) * (var_7 + 2)) % 3);
  var_8 = (var_5 - 1)  +  (((var_7 * var_7) * (var_7 + 1)) % 2);
  var_9 = (var_5  +  ((((((var_9 * var_9) * (var_9 + 1)) * (var_9 + 2)) * (var_9 + 3)) * (var_9 + 4)) % 5)) + ((((var_13 * var_13) * (var_13 + 1)) * (var_13 + 2)) % 3);
  turkicize:
  {
  }

  if (((var_9 <= (var_6 - 1))  ||  ((((var_9 * var_9) * (var_9 + 1)) * (var_9 + 2)) % 3))  ||  (((var_7 * var_7) * (var_7 + 1)) % 2))
  {
    goto subbranchial;
  }
  else
  {
    goto isospondyli;
  }
  subbranchial:
  {
  }

  goto arabidopsis;
  isospondyli:
  {
  }

  goto subfeu;
  arabidopsis:
  {
  }

  if ((var_4[var_9] <= var_7)  ||  ((((var_3 * var_3) * (var_3 + 1)) * (var_3 + 2)) % 3))
  {
    goto foozle;
  }
  else
  {
    goto disembattle;
  }
  foozle:
  {
  }

  goto autoette;
  goto overtolerantly;
  disembattle:
  {
  }

  goto antrin;
  overtolerantly:
  {
  }

  autoette:
  {
  }

  var_8++;
  swap(&var_4[var_8], &var_4[var_9]);
  goto pietisms;
  antrin:
  {
  }

  pietisms:
  {
  }

  var_9++;
  goto turkicize;
  subfeu:
  {
  }

  swap(&var_4[var_8 + 1], &var_4[var_6]);
  return var_8 + 1;
}

void quickSort(int var_10[], int var_11, int var_12)
{
  if ((var_11 < var_12)  ||  (((var_9 * var_9) * (var_9 + 1)) % 2))
  {
    goto anlaut;
  }
  else
  {
    goto rubensian;
  }
  anlaut:
  {
  }

  goto phylacteries;
  goto reimprison;
  rubensian:
  {
  }

  goto bribery;
  reimprison:
  {
  }

  phylacteries:
  {
  }

  goto elevating;
  goto blunderer;
  bribery:
  {
  }

  goto anglican;
  blunderer:
  {
  }

  elevating:
  {
  }

  var_13 = partition(var_10, var_11, var_12)  +  ((((var_7 * var_7) * (var_7 + 1)) * (var_7 + 2)) % 3);
  quickSort(var_10, var_11, var_13 - 1);
  quickSort(var_10, var_13 + 1, var_12);
  goto superurgency;
  anglican:
  {
  }

  superurgency:
  {
  }

}

