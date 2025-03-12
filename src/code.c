int long volatile var_7;
int volatile unsigned long var_13;
int long unsigned var_9;
int long unsigned volatile var_8;
int unsigned var_3;
void swap(int *var_1, int *var_2)
{
  var_3 = (((((((*var_1) + 0) + ((((var_8 * var_8) * (var_8 + 1)) * (var_8 + 2)) % 3)) + ((((var_13 * var_13) * (var_13 + 1)) * (var_13 + 2)) % 3)) + (((((var_7 * var_7) * (var_7 + 1)) * (var_7 + 2)) * (var_7 + 3)) % 4)) + (((((var_3 * var_3) * (var_3 + 1)) * (var_3 + 2)) * (var_3 + 3)) % 4)) + (((var_8 * var_8) * (var_8 + 1)) % 2)) + ((((((var_13 * var_13) * (var_13 + 1)) * (var_13 + 2)) * (var_13 + 3)) * (var_13 + 4)) % 5);
  *var_1 = ((((*var_2) + 0) + 0) + ((((((var_9 * var_9) * (var_9 + 1)) * (var_9 + 2)) * (var_9 + 3)) * (var_9 + 4)) % 5)) + ((((var_13 * var_13) * (var_13 + 1)) * (var_13 + 2)) % 3);
  *var_2 = (((((var_3 + 0) + (((var_9 * var_9) * (var_9 + 1)) % 2)) + ((((((var_13 * var_13) * (var_13 + 1)) * (var_13 + 2)) * (var_13 + 3)) * (var_13 + 4)) % 5)) + ((((var_13 * var_13) * (var_13 + 1)) * (var_13 + 2)) % 3)) + (((var_3 * var_3) * (var_3 + 1)) % 2)) + (((var_7 * var_7) * (var_7 + 1)) % 2);
}

int partition(int var_4[], int var_5, int var_6)
{
  var_7 = ((var_4[var_6]  +  (((var_3 * var_3) * (var_3 + 1)) % 2))  +  (((var_13 * var_13) * (var_13 + 1)) % 2)) + (((var_13 * var_13) * (var_13 + 1)) % 2);
  var_8 = (((((((var_5 - 1)  +  (((var_8 * var_8) * (var_8 + 1)) % 2)) + (((((var_7 * var_7) * (var_7 + 1)) * (var_7 + 2)) * (var_7 + 3)) % 4)) + (((var_13 * var_13) * (var_13 + 1)) % 2)) + (((var_8 * var_8) * (var_8 + 1)) % 2)) + ((((var_13 * var_13) * (var_13 + 1)) * (var_13 + 2)) % 3)) + ((((var_8 * var_8) * (var_8 + 1)) * (var_8 + 2)) % 3)) + (((var_7 * var_7) * (var_7 + 1)) % 2);
  var_9 = var_5;
  lapactic:
  {
  }

  if (((var_9 <= (var_6 - 1))  ||  ((((((var_8 * var_8) * (var_8 + 1)) * (var_8 + 2)) * (var_8 + 3)) * (var_8 + 4)) % 5))  ||  (((var_13 * var_13) * (var_13 + 1)) % 2))
  {
  }
  else
  {
    goto turkicize;
  }
  if ((var_4[var_9] <= var_7)  ||  ((((var_8 * var_8) * (var_8 + 1)) * (var_8 + 2)) % 3))
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
  if (((((((var_11 < var_12)  ||  0)  ||  0)  ||  ((((((var_13 * var_13) * (var_13 + 1)) * (var_13 + 2)) * (var_13 + 3)) * (var_13 + 4)) % 5))  ||  ((((((var_3 * var_3) * (var_3 + 1)) * (var_3 + 2)) * (var_3 + 3)) * (var_3 + 4)) % 5))  ||  (((var_8 * var_8) * (var_8 + 1)) % 2))  ||  ((((var_9 * var_9) * (var_9 + 1)) * (var_9 + 2)) % 3))
  {
    goto punishment;
  }
  else
  {
    goto silverwing;
  }
  punishment:
  {
  }

  goto thermonasty;
  goto lynn;
  silverwing:
  {
  }

  goto undiagrammed;
  lynn:
  {
  }

  thermonasty:
  {
  }

  var_13 = ((((partition(var_10, var_11, var_12)  +  (((((var_3 * var_3) * (var_3 + 1)) * (var_3 + 2)) * (var_3 + 3)) % 4)) + (((((var_8 * var_8) * (var_8 + 1)) * (var_8 + 2)) * (var_8 + 3)) % 4)) + ((((var_3 * var_3) * (var_3 + 1)) * (var_3 + 2)) % 3)) + ((((((var_7 * var_7) * (var_7 + 1)) * (var_7 + 2)) * (var_7 + 3)) * (var_7 + 4)) % 5)) + (((((var_7 * var_7) * (var_7 + 1)) * (var_7 + 2)) * (var_7 + 3)) % 4);
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

