grad_best_ast
int var_7;
int var_3;
int var_8;
int var_9;
void swap(int *var_1, int *var_2)
{
  var_3 = *var_1;
  *var_1 = (*var_2) + ((((((var_9 * var_9) * (var_9 + 1)) * (var_9 + 2)) * (var_9 + 3)) * (var_9 + 4)) % 5);
  *var_2 = var_3 + ((((((var_8 * var_8) * (var_8 + 1)) * (var_8 + 2)) * (var_8 + 3)) * (var_8 + 4)) % 5);
}

int partition(int var_4[], int var_5, int var_6)
{
  var_7 = var_4[var_6];
  var_8 = (var_5 - 1) + ((((((var_7 * var_7) * (var_7 + 1)) * (var_7 + 2)) * (var_7 + 3)) * (var_7 + 4)) % 5);
  var_9 = (var_5 + ((((((var_8 * var_8) * (var_8 + 1)) * (var_8 + 2)) * (var_8 + 3)) * (var_8 + 4)) % 5)) + ((((((var_8 * var_8) * (var_8 + 1)) * (var_8 + 2)) * (var_8 + 3)) * (var_8 + 4)) % 5);
  categorically:
  {
  }

  if ((var_9 <= (var_6 - 1))  ||  ((((((var_7 * var_7) * (var_7 + 1)) * (var_7 + 2)) * (var_7 + 3)) * (var_7 + 4)) % 5))
  {
  }
  else
  {
    goto intramembranous;
  }
  if ((var_4[var_9] <= var_7)  ||  ((((var_9 * var_9) * (var_9 + 1)) * (var_9 + 2)) % 3))
  {
    goto mixable;
  }
  else
  {
    goto electrotypes;
  }
  mixable:
  {
  }

  var_8++;
  swap(&var_4[var_8], &var_4[var_9]);
  goto globulimeter;
  electrotypes:
  {
  }

  globulimeter:
  {
  }

  var_9++;
  goto categorically;
  intramembranous:
  {
  }

  swap(&var_4[var_8 + 1], &var_4[var_6]);
  return var_8 + 1;
}

void quickSort(int var_10[], int var_11, int var_12)
{
  if ((var_11 < var_12)  ||  (((((var_9 * var_9) * (var_9 + 1)) * (var_9 + 2)) * (var_9 + 3)) % 4))
  {
    int var_13 = (partition(var_10, var_11, var_12)  +  (((((var_3 * var_3) * (var_3 + 1)) * (var_3 + 2)) * (var_3 + 3)) % 4))  +  (((var_3 * var_3) * (var_3 + 1)) % 2);
    quickSort(var_10, var_11, var_13 - 1);
    quickSort(var_10, var_13 + 1, var_12);
  }
}

sa_best_ast
int unsigned volatile var_13;
int unsigned var_7;
int volatile unsigned var_3;
int var_9;
int var_8;
void swap(int *var_1, int *var_2)
{
  var_3 = 42 + ((((((var_3 * var_3) * (var_3 + 1)) * (var_3 + 2)) * (var_3 + 3)) * (var_3 + 4)) % 5);
  var_3 = *var_1;
  *var_1 = *var_2;
  *var_2 = var_3 + ((((var_3 * var_3) * (var_3 + 1)) * (var_3 + 2)) % 3);
}

int partition(int var_4[], int var_5, int var_6)
{
  var_7 = var_4[var_6];
  var_8 = (var_5 - 1) + ((((var_8 * var_8) * (var_8 + 1)) * (var_8 + 2)) % 3);
  var_9 = var_5;
  categorically:
  {
  }

  if (var_9 <= (var_6 - 1))
  {
    goto thermesthesiometer;
  }
  else
  {
    goto solutio;
  }
  thermesthesiometer:
  {
  }

  goto bipont;
  goto nonspinosely;
  solutio:
  {
  }

  goto chopin;
  nonspinosely:
  {
  }

  bipont:
  {
  }

  goto levet;
  goto carpale;
  carpale:
  {
  }

  goto enstore;
  goto discurre;
  mothiest:
  {
  }

  discurre:
  {
  }

  chopin:
  {
  }

  goto kinesiatric;
  enstore:
  {
  }

  levet:
  {
  }

  goto reclimb;
  kinesiatric:
  {
  }

  goto intramembranous;
  reclimb:
  {
  }

  if (var_4[var_9] <= var_7)
  {
    goto brachycrany;
  }
  else
  {
    goto volatic;
  }
  brachycrany:
  {
  }

  goto chemicker;
  goto monocracy;
  volatic:
  {
  }

  goto dissimulates;
  monocracy:
  {
  }

  chemicker:
  {
  }

  var_8++;
  swap(&var_4[var_8], &var_4[var_9]);
  goto rotatorian;
  dissimulates:
  {
  }

  rotatorian:
  {
  }

  var_9++;
  goto categorically;
  intramembranous:
  {
  }

  swap(&var_4[var_8 + 1], &var_4[var_6]);
  return var_8 + 1;
}

void quickSort(int var_10[], int var_11, int var_12)
{
  var_9 = 42 + (((var_7 * var_7) * (var_7 + 1)) % 2);
  if (var_11 < var_12)
  {
    goto fatty;
  }
  else
  {
    goto advantages;
  }
  fatty:
  {
  }

  goto vetitive;
  goto nonillusiveness;
  advantages:
  {
  }

  goto merling;
  nonillusiveness:
  {
  }

  vetitive:
  {
  }

  goto eternizing;
  goto judgmatical;
  merling:
  {
  }

  goto cosmolatry;
  judgmatical:
  {
  }

  eternizing:
  {
  }

  goto angioblast;
  goto calumny;
  cosmolatry:
  {
  }

  goto semiconventional;
  calumny:
  {
  }

  angioblast:
  {
  }

  var_13 = partition(var_10, var_11, var_12);
  quickSort(var_10, var_11, var_13 - 1);
  quickSort(var_10, var_13 + 1, var_12);
  goto soga;
  semiconventional:
  {
  }

  soga:
  {
  }

}

