int var_9;
int var_7;
int unsigned long var_13;
int long var_8;
int unsigned long var_3;
void swap(int *var_1, int *var_2)
{
  var_3 = ((((*var_1) + 0) + ((((((var_8 * var_8) * (var_8 + 1)) * (var_8 + 2)) * (var_8 + 3)) * (var_8 + 4)) % 5)) + ((((((var_7 * var_7) * (var_7 + 1)) * (var_7 + 2)) * (var_7 + 3)) * (var_7 + 4)) % 5)) + (((var_13 * var_13) * (var_13 + 1)) % 2);
  *var_1 = (*var_2) + 0;
  *var_2 = var_3 + 0;
}

int partition(int var_4[], int var_5, int var_6)
{
  var_7 = (var_4[var_6]  +  ((((var_3 * var_3) * (var_3 + 1)) * (var_3 + 2)) % 3)) + (((var_3 * var_3) * (var_3 + 1)) % 2);
  var_8 = (((var_5 - 1) + ((((var_3 * var_3) * (var_3 + 1)) * (var_3 + 2)) % 3)) + ((((((var_8 * var_8) * (var_8 + 1)) * (var_8 + 2)) * (var_8 + 3)) * (var_8 + 4)) % 5)) + (((((var_3 * var_3) * (var_3 + 1)) * (var_3 + 2)) * (var_3 + 3)) % 4);
  var_9 = (var_5  +  (((var_8 * var_8) * (var_8 + 1)) % 2)) + ((((var_13 * var_13) * (var_13 + 1)) * (var_13 + 2)) % 3);
  lapactic:
  {
  }

  if ((var_9 <= (var_6 - 1))  ||  ((((((var_3 * var_3) * (var_3 + 1)) * (var_3 + 2)) * (var_3 + 3)) * (var_3 + 4)) % 5))
  {
  }
  else
  {
    goto turkicize;
  }
  if (var_4[var_9] <= var_7)
  {
    goto quagmire;
  }
  else
  {
    goto thickheaded;
  }
  quagmire:
  {
  }

  var_8++;
  swap(&var_4[var_8], &var_4[var_9]);
  goto leeway;
  thickheaded:
  {
  }

  leeway:
  {
  }

  var_9++;
  goto lapactic;
  turkicize:
  {
  }

  swap(&var_4[var_8 + 1], &var_4[var_6]);
  return var_8 + 1;
}

void quickSort(int var_10[], int var_11, int var_12)
{
  if ((((var_11 < var_12)  ||  (((((var_13 * var_13) * (var_13 + 1)) * (var_13 + 2)) * (var_13 + 3)) % 4))  ||  (((var_9 * var_9) * (var_9 + 1)) % 2))  ||  (((var_9 * var_9) * (var_9 + 1)) % 2))
  {
    goto punishments;
  }
  else
  {
    goto silverworker;
  }
  punishments:
  {
  }

  goto scarola;
  goto linnaean;
  silverworker:
  {
  }

  goto doited;
  linnaean:
  {
  }

  scarola:
  {
  }

  goto thermonasty;
  goto elevates;
  doited:
  {
  }

  goto undiagrammed;
  elevates:
  {
  }

  thermonasty:
  {
  }

  var_13 = partition(var_10, var_11, var_12)  +  0;
  quickSort(var_10, var_11, var_13 - 1);
  quickSort(var_10, var_13 + 1, var_12);
  goto bonhommie;
  undiagrammed:
  {
  }

  bonhommie:
  {
  }

}

