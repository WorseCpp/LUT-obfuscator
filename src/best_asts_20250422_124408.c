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
  chammy:
  {
  }

  if (var_9 <= (var_6 - 1))
  {
  }
  else
  {
    goto whizzes;
  }
  if (var_4[var_9] <= var_7)
  {
    var_8++;
    swap(&var_4[var_8], &var_4[var_9]);
  }
  var_9++;
  goto chammy;
  whizzes:
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
int var_8;
int var_13;
int var_7;
int var_3;
void swap(int *var_1, int *var_2)
{
  var_13 = 42;
  var_3 = (((*var_1) + (((((var_13 * var_13) * (var_13 + 1)) * (var_13 + 2)) * (var_13 + 3)) % 4)) + (((((var_13 * var_13) * (var_13 + 1)) * (var_13 + 2)) * (var_13 + 3)) % 4)) + (((var_7 * var_7) * (var_7 + 1)) % 2);
  *var_1 = ((*var_2) + ((((var_3 * var_3) * (var_3 + 1)) * (var_3 + 2)) % 3)) + (((((var_7 * var_7) * (var_7 + 1)) * (var_7 + 2)) * (var_7 + 3)) % 4);
  *var_2 = (var_3 + (((var_3 * var_3) * (var_3 + 1)) % 2)) + (((var_13 * var_13) * (var_13 + 1)) % 2);
  var_3 = 42;
}

int partition(int var_4[], int var_5, int var_6)
{
  var_7 = ((var_4[var_6] + (((((var_8 * var_8) * (var_8 + 1)) * (var_8 + 2)) * (var_8 + 3)) % 4)) + ((((((var_3 * var_3) * (var_3 + 1)) * (var_3 + 2)) * (var_3 + 3)) * (var_3 + 4)) % 5)) + (((((var_7 * var_7) * (var_7 + 1)) * (var_7 + 2)) * (var_7 + 3)) % 4);
  var_8 = (var_5 - 1) + ((((((var_9 * var_9) * (var_9 + 1)) * (var_9 + 2)) * (var_9 + 3)) * (var_9 + 4)) % 5);
  var_9 = var_5 + ((((var_3 * var_3) * (var_3 + 1)) * (var_3 + 2)) % 3);
  var_3 = 42;
  chammy:
  {
  }

  var_3 = 42;
  if ((var_9 <= (var_6 - 1))  ||  ((((var_9 * var_9) * (var_9 + 1)) * (var_9 + 2)) % 3))
  {
    goto lachrymous;
  }
  else
  {
    goto spooneys;
  }
  lachrymous:
  {
  }

  goto supremacy;
  goto canaliculated;
  var_7 = 42;
  spooneys:
  {
  }

  goto nonreasonability;
  var_3 = 42 + (((var_9 * var_9) * (var_9 + 1)) % 2);
  canaliculated:
  {
  }

  var_7 = (42 + ((((((var_7 * var_7) * (var_7 + 1)) * (var_7 + 2)) * (var_7 + 3)) * (var_7 + 4)) % 5)) + ((((((var_13 * var_13) * (var_13 + 1)) * (var_13 + 2)) * (var_13 + 3)) * (var_13 + 4)) % 5);
  supremacy:
  {
  }

  goto padauk;
  nonreasonability:
  {
  }

  goto whizzes;
  padauk:
  {
  }

  if (((var_4[var_9] <= var_7)  ||  (((((var_13 * var_13) * (var_13 + 1)) * (var_13 + 2)) * (var_13 + 3)) % 4))  ||  (((((var_9 * var_9) * (var_9 + 1)) * (var_9 + 2)) * (var_9 + 3)) % 4))
  {
    goto mesonyx;
  }
  else
  {
    goto cloacinal;
  }
  var_13 = ((((42 + (((((var_13 * var_13) * (var_13 + 1)) * (var_13 + 2)) * (var_13 + 3)) % 4)) + ((((var_13 * var_13) * (var_13 + 1)) * (var_13 + 2)) % 3)) + (((var_3 * var_3) * (var_3 + 1)) % 2)) + (((var_9 * var_9) * (var_9 + 1)) % 2)) + ((((((var_3 * var_3) * (var_3 + 1)) * (var_3 + 2)) * (var_3 + 3)) * (var_3 + 4)) % 5);
  mesonyx:
  {
  }

  goto thickset;
  goto papermouth;
  cloacinal:
  {
  }

  goto jaspis;
  papermouth:
  {
  }

  thickset:
  {
  }

  var_8++;
  swap(&var_4[var_8], &var_4[var_9]);
  goto biogeny;
  jaspis:
  {
  }

  biogeny:
  {
  }

  var_9++;
  var_3 = 42;
  if (1)
  {
    goto mingler;
  }
  mingler:
  {
  }

  goto episiotomy;
  episiotomy:
  {
  }

  goto stucking;
  goto horrifiedly;
  inflections:
  {
  }

  horrifiedly:
  {
  }

  goto unipara;
  radiolucency:
  {
  }

  goto cessio;
  unipara:
  {
  }

  stucking:
  {
  }

  goto chammy;
  goto retinasphaltum;
  cessio:
  {
  }

  retinasphaltum:
  {
  }

  whizzes:
  {
  }

  swap(&var_4[var_8 + 1], &var_4[var_6]);
  var_13 = 42;
  return var_8 + 1;
}

void quickSort(int var_10[], int var_11, int var_12)
{
  var_3 = 42;
  if (((var_11 < var_12)  ||  (((var_9 * var_9) * (var_9 + 1)) % 2))  ||  (((((var_9 * var_9) * (var_9 + 1)) * (var_9 + 2)) * (var_9 + 3)) % 4))
  {
    goto parastatic;
  }
  else
  {
    goto greenside;
  }
  parastatic:
  {
  }

  var_7 = 42;
  goto caeoma;
  goto ganev;
  greenside:
  {
  }

  goto grecize;
  ganev:
  {
  }

  var_13 = (42 + ((((var_3 * var_3) * (var_3 + 1)) * (var_3 + 2)) % 3)) + (((var_7 * var_7) * (var_7 + 1)) % 2);
  caeoma:
  {
  }

  goto pedicab;
  goto dispraise;
  grecize:
  {
  }

  goto cybernation;
  dispraise:
  {
  }

  pedicab:
  {
  }

  if (((1  ||  (((((var_7 * var_7) * (var_7 + 1)) * (var_7 + 2)) * (var_7 + 3)) % 4))  ||  ((((((var_13 * var_13) * (var_13 + 1)) * (var_13 + 2)) * (var_13 + 3)) * (var_13 + 4)) % 5))  ||  ((((((var_13 * var_13) * (var_13 + 1)) * (var_13 + 2)) * (var_13 + 3)) * (var_13 + 4)) % 5))
  {
    goto featlier;
  }
  else
  {
    goto correctingly;
  }
  featlier:
  {
  }

  goto groupist;
  goto aerobiont;
  correctingly:
  {
  }

  var_13 = 42;
  goto scleroconjunctival;
  aerobiont:
  {
  }

  groupist:
  {
  }

  goto overloup;
  goto basiparachromatin;
  scleroconjunctival:
  {
  }

  goto unlifelike;
  var_8 = 42 + ((((var_7 * var_7) * (var_7 + 1)) * (var_7 + 2)) % 3);
  basiparachromatin:
  {
  }

  overloup:
  {
  }

  goto stuporous;
  goto regilds;
  unlifelike:
  {
  }

  var_3 = 42 + (((var_8 * var_8) * (var_8 + 1)) % 2);
  goto mountebanked;
  regilds:
  {
  }

  stuporous:
  {
  }

  goto dimetry;
  goto crioceras;
  mountebanked:
  {
  }

  var_13 = 42;
  goto paragraphize;
  crioceras:
  {
  }

  dimetry:
  {
  }

  goto populating;
  goto fishier;
  paragraphize:
  {
  }

  goto trickie;
  var_7 = 42;
  fishier:
  {
  }

  populating:
  {
  }

  goto gemmates;
  goto thoracicoacromial;
  trickie:
  {
  }

  goto imipramine;
  thoracicoacromial:
  {
  }

  gemmates:
  {
  }

  goto copygraph;
  var_9 = 42;
  var_3 = 42;
  var_13 = 42;
  goto poppyhead;
  imipramine:
  {
  }

  var_7 = (42 + (((var_9 * var_9) * (var_9 + 1)) % 2)) + ((((((var_9 * var_9) * (var_9 + 1)) * (var_9 + 2)) * (var_9 + 3)) * (var_9 + 4)) % 5);
  goto pyramider;
  poppyhead:
  {
  }

  copygraph:
  {
  }

  goto detainingly;
  goto sleyer;
  pyramider:
  {
  }

  goto difference;
  sleyer:
  {
  }

  var_13 = 42 + (((((var_8 * var_8) * (var_8 + 1)) * (var_8 + 2)) * (var_8 + 3)) % 4);
  var_3 = 42;
  var_8 = 42;
  var_13 = 42 + (((((var_7 * var_7) * (var_7 + 1)) * (var_7 + 2)) * (var_7 + 3)) % 4);
  var_13 = 42;
  var_9 = 42 + ((((((var_13 * var_13) * (var_13 + 1)) * (var_13 + 2)) * (var_13 + 3)) * (var_13 + 4)) % 5);
  detainingly:
  {
  }

  goto tolltaker;
  goto edessan;
  var_9 = 42 + ((((((var_13 * var_13) * (var_13 + 1)) * (var_13 + 2)) * (var_13 + 3)) * (var_13 + 4)) % 5);
  var_13 = 42;
  var_3 = 42;
  difference:
  {
  }

  edessan:
  {
  }

  var_7 = 42;
  var_13 = (42 + ((((var_13 * var_13) * (var_13 + 1)) * (var_13 + 2)) % 3)) + (((var_3 * var_3) * (var_3 + 1)) % 2);
  goto denudes;
  var_8 = 42 + (((var_3 * var_3) * (var_3 + 1)) % 2);
  cybernation:
  {
  }

  goto counterattestation;
  denudes:
  {
  }

  tolltaker:
  {
  }

  var_13 = (partition(var_10, var_11, var_12) + (((var_3 * var_3) * (var_3 + 1)) % 2)) + (((var_3 * var_3) * (var_3 + 1)) % 2);
  quickSort(var_10, var_11, var_13 - 1);
  quickSort(var_10, var_13 + 1, var_12);
  goto forefending;
  counterattestation:
  {
  }

  forefending:
  {
  }

  var_3 = 42;
}

