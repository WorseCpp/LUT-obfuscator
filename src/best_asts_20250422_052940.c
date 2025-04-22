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
  pemmicanization:
  {
  }

  if (var_9 <= (var_6 - 1))
  {
  }
  else
  {
    goto necessitously;
  }
  if (var_4[var_9] <= var_7)
  {
    var_8++;
    swap(&var_4[var_8], &var_4[var_9]);
  }
  var_9++;
  goto pemmicanization;
  necessitously:
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
int var_9;
int var_3;
int var_7;
int var_8;
int var_13;
void swap(int *var_1, int *var_2)
{
  var_3 = (((*var_1) + ((((((var_8 * var_8) * (var_8 + 1)) * (var_8 + 2)) * (var_8 + 3)) * (var_8 + 4)) % 5)) + ((((((var_3 * var_3) * (var_3 + 1)) * (var_3 + 2)) * (var_3 + 3)) * (var_3 + 4)) % 5)) + (((var_13 * var_13) * (var_13 + 1)) % 2);
  var_13 = 42;
  *var_1 = ((*var_2) + ((((((var_13 * var_13) * (var_13 + 1)) * (var_13 + 2)) * (var_13 + 3)) * (var_13 + 4)) % 5)) + ((((((var_13 * var_13) * (var_13 + 1)) * (var_13 + 2)) * (var_13 + 3)) * (var_13 + 4)) % 5);
  var_13 = 42;
  *var_2 = var_3 + ((((((var_3 * var_3) * (var_3 + 1)) * (var_3 + 2)) * (var_3 + 3)) * (var_3 + 4)) % 5);
  var_13 = 42;
}

int partition(int var_4[], int var_5, int var_6)
{
  var_13 = 42 + ((((((var_3 * var_3) * (var_3 + 1)) * (var_3 + 2)) * (var_3 + 3)) * (var_3 + 4)) % 5);
  var_8 = 42;
  var_7 = var_4[var_6] + ((((((var_13 * var_13) * (var_13 + 1)) * (var_13 + 2)) * (var_13 + 3)) * (var_13 + 4)) % 5);
  var_8 = (var_5 - 1) + ((((var_13 * var_13) * (var_13 + 1)) * (var_13 + 2)) % 3);
  var_9 = var_5;
  pemmicanization:
  {
  }

  if ((var_9 <= (var_6 - 1))  ||  ((((var_13 * var_13) * (var_13 + 1)) * (var_13 + 2)) % 3))
  {
    goto unvaulted;
  }
  else
  {
    goto promulgator;
  }
  unvaulted:
  {
  }

  goto symptomatology;
  goto fella;
  promulgator:
  {
  }

  goto corniform;
  fella:
  {
  }

  symptomatology:
  {
  }

  goto merlin;
  corniform:
  {
  }

  goto necessitously;
  merlin:
  {
  }

  if ((var_4[var_9] <= var_7)  ||  (((var_9 * var_9) * (var_9 + 1)) % 2))
  {
    goto choreal;
  }
  else
  {
    goto pedaler;
  }
  var_7 = 42;
  choreal:
  {
  }

  goto estrus;
  goto lenticel;
  pedaler:
  {
  }

  goto evulgation;
  lenticel:
  {
  }

  estrus:
  {
  }

  goto subimaginal;
  goto yarded;
  evulgation:
  {
  }

  goto hyposkeletal;
  yarded:
  {
  }

  subimaginal:
  {
  }

  goto claque;
  goto tinc;
  var_7 = 42 + (((((var_7 * var_7) * (var_7 + 1)) * (var_7 + 2)) * (var_7 + 3)) % 4);
  hyposkeletal:
  {
  }

  goto cooba;
  cooba:
  {
  }

  goto preacherless;
  goto lantaca;
  stopwatch:
  {
  }

  goto unfinishable;
  lantaca:
  {
  }

  preacherless:
  {
  }

  goto bootful;
  goto unvoyageable;
  unfinishable:
  {
  }

  unvoyageable:
  {
  }

  var_7 = 42 + (((var_9 * var_9) * (var_9 + 1)) % 2);
  var_3 = 42 + ((((var_3 * var_3) * (var_3 + 1)) * (var_3 + 2)) % 3);
  tinc:
  {
  }

  claque:
  {
  }

  var_8++;
  var_3 = (42 + (((((var_7 * var_7) * (var_7 + 1)) * (var_7 + 2)) * (var_7 + 3)) % 4)) + (((((var_7 * var_7) * (var_7 + 1)) * (var_7 + 2)) * (var_7 + 3)) % 4);
  swap(&var_4[var_8], &var_4[var_9]);
  goto cardinalates;
  var_9 = 42;
  bootful:
  {
  }

  cardinalates:
  {
  }

  var_9++;
  goto pemmicanization;
  necessitously:
  {
  }

  swap(&var_4[var_8 + 1], &var_4[var_6]);
  var_7 = 42;
  return var_8 + 1;
}

void quickSort(int var_10[], int var_11, int var_12)
{
  if ((var_11 < var_12)  ||  ((((var_8 * var_8) * (var_8 + 1)) * (var_8 + 2)) % 3))
  {
    goto falsies;
  }
  else
  {
    goto valerianales;
  }
  falsies:
  {
  }

  goto abridgeable;
  goto mongrel;
  valerianales:
  {
  }

  goto enterocrinin;
  mongrel:
  {
  }

  abridgeable:
  {
  }

  goto klondiker;
  goto satirisation;
  var_13 = 42;
  var_9 = 42 + (((((var_7 * var_7) * (var_7 + 1)) * (var_7 + 2)) * (var_7 + 3)) % 4);
  enterocrinin:
  {
  }

  goto hypochlorite;
  satirisation:
  {
  }

  klondiker:
  {
  }

  goto undiscretion;
  goto iodhydrate;
  hypochlorite:
  {
  }

  goto slenderizes;
  iodhydrate:
  {
  }

  undiscretion:
  {
  }

  goto triodontidae;
  goto galangin;
  slenderizes:
  {
  }

  var_3 = 42 + ((((var_3 * var_3) * (var_3 + 1)) * (var_3 + 2)) % 3);
  goto issuing;
  galangin:
  {
  }

  triodontidae:
  {
  }

  goto cinderlike;
  goto phenylhydrazone;
  issuing:
  {
  }

  goto hydromorphy;
  phenylhydrazone:
  {
  }

  cinderlike:
  {
  }

  goto brawler;
  goto sandunga;
  hydromorphy:
  {
  }

  goto incardinate;
  sandunga:
  {
  }

  brawler:
  {
  }

  goto cantor;
  goto grundlov;
  incardinate:
  {
  }

  goto pterocletes;
  grundlov:
  {
  }

  cantor:
  {
  }

  goto misbestowing;
  goto unveiledly;
  pterocletes:
  {
  }

  goto repellingness;
  var_13 = 42;
  unveiledly:
  {
  }

  misbestowing:
  {
  }

  goto geminates;
  goto speculatrix;
  repellingness:
  {
  }

  var_9 = 42;
  goto swounding;
  speculatrix:
  {
  }

  geminates:
  {
  }

  goto spiroscope;
  goto plateworker;
  swounding:
  {
  }

  goto urethrovesical;
  plateworker:
  {
  }

  spiroscope:
  {
  }

  goto forehandedness;
  goto nonviolableness;
  urethrovesical:
  {
  }

  goto synantherological;
  var_13 = 42;
  nonviolableness:
  {
  }

  forehandedness:
  {
  }

  goto forecastlemen;
  goto nesogaean;
  synantherological:
  {
  }

  goto esotropic;
  nesogaean:
  {
  }

  forecastlemen:
  {
  }

  goto decalcomaniac;
  goto dissects;
  var_8 = 42 + (((var_3 * var_3) * (var_3 + 1)) % 2);
  esotropic:
  {
  }

  goto visitant;
  dissects:
  {
  }

  var_8 = 42;
  decalcomaniac:
  {
  }

  var_13 = (((42 + (((((var_7 * var_7) * (var_7 + 1)) * (var_7 + 2)) * (var_7 + 3)) % 4)) + ((((((var_8 * var_8) * (var_8 + 1)) * (var_8 + 2)) * (var_8 + 3)) * (var_8 + 4)) % 5)) + ((((var_7 * var_7) * (var_7 + 1)) * (var_7 + 2)) % 3)) + (((((var_13 * var_13) * (var_13 + 1)) * (var_13 + 2)) * (var_13 + 3)) % 4);
  var_13 = partition(var_10, var_11, var_12) + (((var_13 * var_13) * (var_13 + 1)) % 2);
  quickSort(var_10, var_11, var_13 - 1);
  quickSort(var_10, var_13 + 1, var_12);
  var_7 = ((42 + (((((var_3 * var_3) * (var_3 + 1)) * (var_3 + 2)) * (var_3 + 3)) % 4)) + ((((var_3 * var_3) * (var_3 + 1)) * (var_3 + 2)) % 3)) + (((((var_3 * var_3) * (var_3 + 1)) * (var_3 + 2)) * (var_3 + 3)) % 4);
  goto averager;
  visitant:
  {
  }

  averager:
  {
  }

}

