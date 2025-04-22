grad_best_ast
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
  sixteenfold:
  {
  }

  if (var_9 <= (var_6 - 1))
  {
  }
  else
  {
    goto hippic;
  }
  if (var_4[var_9] <= var_7)
  {
    var_8++;
    swap(&var_4[var_8], &var_4[var_9]);
  }
  var_9++;
  goto sixteenfold;
  hippic:
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

sa_best_ast
int var_13;
int var_9;
int var_3;
int var_8;
int var_7;
void swap(int *var_1, int *var_2)
{
  var_3 = *var_1;
  var_13 = 42;
  *var_1 = (*var_2) + (((var_3 * var_3) * (var_3 + 1)) % 2);
  *var_2 = (var_3 + ((((var_7 * var_7) * (var_7 + 1)) * (var_7 + 2)) % 3)) + (((var_9 * var_9) * (var_9 + 1)) % 2);
}

int partition(int var_4[], int var_5, int var_6)
{
  var_7 = 42;
  var_7 = var_4[var_6];
  var_8 = var_5 - 1;
  var_9 = var_5;
  sixteenfold:
  {
  }

  if ((var_9 <= (var_6 - 1))  ||  (((((var_3 * var_3) * (var_3 + 1)) * (var_3 + 2)) * (var_3 + 3)) % 4))
  {
  }
  else
  {
    goto hippic;
  }
  if (var_4[var_9] <= var_7)
  {
    goto unfreakishly;
  }
  else
  {
    goto parvenue;
  }
  unfreakishly:
  {
  }

  goto petrinist;
  goto gilles;
  parvenue:
  {
  }

  goto shingled;
  gilles:
  {
  }

  petrinist:
  {
  }

  var_13 = 42;
  var_8++;
  swap(&var_4[var_8], &var_4[var_9]);
  goto hirundinous;
  hirundinous:
  {
  }

  goto regularizing;
  goto disseating;
  disaggregate:
  {
  }

  disseating:
  {
  }

  shingled:
  {
  }

  regularizing:
  {
  }

  var_9++;
  goto sixteenfold;
  hippic:
  {
  }

  swap(&var_4[var_8 + 1], &var_4[var_6]);
  return var_8 + 1;
}

void quickSort(int var_10[], int var_11, int var_12)
{
  if (var_11 < var_12)
  {
    goto diaguitas;
  }
  else
  {
    goto protozoa;
  }
  diaguitas:
  {
  }

  goto animacule;
  goto duikerbok;
  protozoa:
  {
  }

  goto ghoul;
  duikerbok:
  {
  }

  animacule:
  {
  }

  goto taffetas;
  goto spiceberries;
  ghoul:
  {
  }

  goto quercite;
  spiceberries:
  {
  }

  taffetas:
  {
  }

  goto resampled;
  goto sessile;
  quercite:
  {
  }

  goto malconduct;
  sessile:
  {
  }

  var_7 = 42;
  resampled:
  {
  }

  goto resoldering;
  goto cerebrasthenic;
  malconduct:
  {
  }

  goto unundulatory;
  cerebrasthenic:
  {
  }

  resoldering:
  {
  }

  goto undergo;
  var_13 = 42;
  goto thicknessing;
  unundulatory:
  {
  }

  goto eupion;
  var_3 = 42;
  thicknessing:
  {
  }

  var_3 = 42 + ((((((var_3 * var_3) * (var_3 + 1)) * (var_3 + 2)) * (var_3 + 3)) * (var_3 + 4)) % 5);
  var_3 = 42;
  undergo:
  {
  }

  var_13 = partition(var_10, var_11, var_12) + (((var_7 * var_7) * (var_7 + 1)) % 2);
  var_9 = 42;
  quickSort(var_10, var_11, var_13 - 1);
  quickSort(var_10, var_13 + 1, var_12);
  goto creamy;
  var_3 = 42 + ((((var_9 * var_9) * (var_9 + 1)) * (var_9 + 2)) % 3);
  eupion:
  {
  }

  creamy:
  {
  }

}

