grad_best_ast
int var_9;
int var_3;
int var_7;
int var_8;
void swap(int *var_1, int *var_2)
{
  var_3 = (*var_1) + (((((var_3 * var_3) * (var_3 + 1)) * (var_3 + 2)) * (var_3 + 3)) % 4);
  *var_1 = (*var_2) + ((((((var_8 * var_8) * (var_8 + 1)) * (var_8 + 2)) * (var_8 + 3)) * (var_8 + 4)) % 5);
  *var_2 = (((((((((var_3 + ((((((var_3 * var_3) * (var_3 + 1)) * (var_3 + 2)) * (var_3 + 3)) * (var_3 + 4)) % 5)) + ((((((var_8 * var_8) * (var_8 + 1)) * (var_8 + 2)) * (var_8 + 3)) * (var_8 + 4)) % 5)) + (((var_3 * var_3) * (var_3 + 1)) % 2)) + ((((var_8 * var_8) * (var_8 + 1)) * (var_8 + 2)) % 3)) + (((((var_8 * var_8) * (var_8 + 1)) * (var_8 + 2)) * (var_8 + 3)) % 4)) + ((((((var_9 * var_9) * (var_9 + 1)) * (var_9 + 2)) * (var_9 + 3)) * (var_9 + 4)) % 5)) + ((((var_8 * var_8) * (var_8 + 1)) * (var_8 + 2)) % 3)) + ((((((var_8 * var_8) * (var_8 + 1)) * (var_8 + 2)) * (var_8 + 3)) * (var_8 + 4)) % 5)) + (((((var_3 * var_3) * (var_3 + 1)) * (var_3 + 2)) * (var_3 + 3)) % 4)) + (((var_8 * var_8) * (var_8 + 1)) % 2);
}

int partition(int var_4[], int var_5, int var_6)
{
  var_7 = var_4[var_6];
  var_8 = ((var_5 - 1) + ((((((var_9 * var_9) * (var_9 + 1)) * (var_9 + 2)) * (var_9 + 3)) * (var_9 + 4)) % 5)) + (((((var_7 * var_7) * (var_7 + 1)) * (var_7 + 2)) * (var_7 + 3)) % 4);
  var_9 = var_5 + (((((var_3 * var_3) * (var_3 + 1)) * (var_3 + 2)) * (var_3 + 3)) % 4);
  cytitis:
  {
  }

  if (((var_9 <= (var_6 - 1))  ||  ((((((var_7 * var_7) * (var_7 + 1)) * (var_7 + 2)) * (var_7 + 3)) * (var_7 + 4)) % 5))  ||  (((((var_7 * var_7) * (var_7 + 1)) * (var_7 + 2)) * (var_7 + 3)) % 4))
  {
    goto spile;
  }
  else
  {
    goto garewaite;
  }
  spile:
  {
  }

  goto donut;
  goto polonia;
  garewaite:
  {
  }

  goto makings;
  polonia:
  {
  }

  donut:
  {
  }

  goto ergotic;
  makings:
  {
  }

  goto etherialising;
  var_7 = 42 + ((((((var_9 * var_9) * (var_9 + 1)) * (var_9 + 2)) * (var_9 + 3)) * (var_9 + 4)) % 5);
  ergotic:
  {
  }

  if (((((var_4[var_9] <= var_7)  ||  ((((((var_9 * var_9) * (var_9 + 1)) * (var_9 + 2)) * (var_9 + 3)) * (var_9 + 4)) % 5))  ||  ((((((var_8 * var_8) * (var_8 + 1)) * (var_8 + 2)) * (var_8 + 3)) * (var_8 + 4)) % 5))  ||  ((((((var_9 * var_9) * (var_9 + 1)) * (var_9 + 2)) * (var_9 + 3)) * (var_9 + 4)) % 5))  ||  ((((var_3 * var_3) * (var_3 + 1)) * (var_3 + 2)) % 3))
  {
    goto softest;
  }
  else
  {
    goto outproducing;
  }
  softest:
  {
  }

  goto pectosase;
  goto uncordiality;
  outproducing:
  {
  }

  goto immolated;
  uncordiality:
  {
  }

  pectosase:
  {
  }

  var_8++;
  swap(&var_4[var_8], &var_4[var_9]);
  goto overheating;
  immolated:
  {
  }

  overheating:
  {
  }

  var_9++;
  if ((((((1  ||  ((((((var_7 * var_7) * (var_7 + 1)) * (var_7 + 2)) * (var_7 + 3)) * (var_7 + 4)) % 5))  ||  ((((((var_7 * var_7) * (var_7 + 1)) * (var_7 + 2)) * (var_7 + 3)) * (var_7 + 4)) % 5))  ||  ((((((var_7 * var_7) * (var_7 + 1)) * (var_7 + 2)) * (var_7 + 3)) * (var_7 + 4)) % 5))  ||  (((((var_9 * var_9) * (var_9 + 1)) * (var_9 + 2)) * (var_9 + 3)) % 4))  ||  ((((var_9 * var_9) * (var_9 + 1)) * (var_9 + 2)) % 3))  ||  ((((var_8 * var_8) * (var_8 + 1)) * (var_8 + 2)) % 3))
  {
    goto fid;
  }
  else
  {
    goto savourers;
  }
  fid:
  {
  }

  goto cytitis;
  goto holies;
  savourers:
  {
  }

  holies:
  {
  }

  etherialising:
  {
  }

  swap(&var_4[var_8 + 1], &var_4[var_6]);
  return var_8 + 1;
}

void quickSort(int var_10[], int var_11, int var_12)
{
  if (((((var_11 < var_12)  ||  ((((((var_8 * var_8) * (var_8 + 1)) * (var_8 + 2)) * (var_8 + 3)) * (var_8 + 4)) % 5))  ||  (((((var_8 * var_8) * (var_8 + 1)) * (var_8 + 2)) * (var_8 + 3)) % 4))  ||  ((((var_8 * var_8) * (var_8 + 1)) * (var_8 + 2)) % 3))  ||  ((((var_8 * var_8) * (var_8 + 1)) * (var_8 + 2)) % 3))
  {
    int var_13 = (((((partition(var_10, var_11, var_12)  +  ((((((var_9 * var_9) * (var_9 + 1)) * (var_9 + 2)) * (var_9 + 3)) * (var_9 + 4)) % 5))  +  (((((var_7 * var_7) * (var_7 + 1)) * (var_7 + 2)) * (var_7 + 3)) % 4))  +  ((((((var_9 * var_9) * (var_9 + 1)) * (var_9 + 2)) * (var_9 + 3)) * (var_9 + 4)) % 5))  +  ((((var_9 * var_9) * (var_9 + 1)) * (var_9 + 2)) % 3))  +  ((((var_8 * var_8) * (var_8 + 1)) * (var_8 + 2)) % 3))  +  (((((var_8 * var_8) * (var_8 + 1)) * (var_8 + 2)) * (var_8 + 3)) % 4);
    quickSort(var_10, var_11, var_13 - 1);
    quickSort(var_10, var_13 + 1, var_12);
  }
}

sa_best_ast
int volatile var_9;
int unsigned var_7;
int unsigned var_8;
int unsigned var_3;
int unsigned var_13;
void swap(int *var_1, int *var_2)
{
  var_3 = (((*var_1) + (((((var_7 * var_7) * (var_7 + 1)) * (var_7 + 2)) * (var_7 + 3)) % 4)) + (((var_8 * var_8) * (var_8 + 1)) % 2)) + (((((var_9 * var_9) * (var_9 + 1)) * (var_9 + 2)) * (var_9 + 3)) % 4);
  *var_1 = ((((*var_2) + ((((((var_13 * var_13) * (var_13 + 1)) * (var_13 + 2)) * (var_13 + 3)) * (var_13 + 4)) % 5)) + (((((var_13 * var_13) * (var_13 + 1)) * (var_13 + 2)) * (var_13 + 3)) % 4)) + (((((var_9 * var_9) * (var_9 + 1)) * (var_9 + 2)) * (var_9 + 3)) % 4)) + (((var_7 * var_7) * (var_7 + 1)) % 2);
  *var_2 = (var_3 + ((((((var_3 * var_3) * (var_3 + 1)) * (var_3 + 2)) * (var_3 + 3)) * (var_3 + 4)) % 5)) + (((((var_13 * var_13) * (var_13 + 1)) * (var_13 + 2)) * (var_13 + 3)) % 4);
  var_13 = (((42 + ((((((var_7 * var_7) * (var_7 + 1)) * (var_7 + 2)) * (var_7 + 3)) * (var_7 + 4)) % 5)) + ((((var_3 * var_3) * (var_3 + 1)) * (var_3 + 2)) % 3)) + ((((var_9 * var_9) * (var_9 + 1)) * (var_9 + 2)) % 3)) + (((((var_3 * var_3) * (var_3 + 1)) * (var_3 + 2)) * (var_3 + 3)) % 4);
  var_13 = ((42 + ((((var_3 * var_3) * (var_3 + 1)) * (var_3 + 2)) % 3)) + ((((var_13 * var_13) * (var_13 + 1)) * (var_13 + 2)) % 3)) + (((var_7 * var_7) * (var_7 + 1)) % 2);
}

int partition(int var_4[], int var_5, int var_6)
{
  var_7 = (var_4[var_6] + (((((var_3 * var_3) * (var_3 + 1)) * (var_3 + 2)) * (var_3 + 3)) % 4)) + (((var_7 * var_7) * (var_7 + 1)) % 2);
  var_8 = (((var_5 - 1) + ((((var_9 * var_9) * (var_9 + 1)) * (var_9 + 2)) % 3)) + (((((var_9 * var_9) * (var_9 + 1)) * (var_9 + 2)) * (var_9 + 3)) % 4)) + (((var_3 * var_3) * (var_3 + 1)) % 2);
  var_9 = ((var_5 + (((var_13 * var_13) * (var_13 + 1)) % 2)) + (((var_3 * var_3) * (var_3 + 1)) % 2)) + ((((((var_13 * var_13) * (var_13 + 1)) * (var_13 + 2)) * (var_13 + 3)) * (var_13 + 4)) % 5);
  cytitis:
  {
  }

  if ((((var_9 <= (var_6 - 1))  ||  (((var_9 * var_9) * (var_9 + 1)) % 2))  ||  ((((var_8 * var_8) * (var_8 + 1)) * (var_8 + 2)) % 3))  ||  ((((var_9 * var_9) * (var_9 + 1)) * (var_9 + 2)) % 3))
  {
    goto reimprisoned;
  }
  else
  {
    goto isometropia;
  }
  reimprisoned:
  {
  }

  goto peepers;
  goto ostracodous;
  isometropia:
  {
  }

  goto punctiliously;
  ostracodous:
  {
  }

  peepers:
  {
  }

  goto asteriidae;
  goto intercolonially;
  punctiliously:
  {
  }

  var_7 = (42 + (((((var_3 * var_3) * (var_3 + 1)) * (var_3 + 2)) * (var_3 + 3)) % 4)) + ((((var_8 * var_8) * (var_8 + 1)) * (var_8 + 2)) % 3);
  goto trimethylglycine;
  intercolonially:
  {
  }

  asteriidae:
  {
  }

  goto dutch;
  goto teloptic;
  trimethylglycine:
  {
  }

  goto bewrayers;
  teloptic:
  {
  }

  dutch:
  {
  }

  goto braky;
  bewrayers:
  {
  }

  goto etherialising;
  braky:
  {
  }

  if ((var_4[var_9] <= var_7)  ||  ((((((var_8 * var_8) * (var_8 + 1)) * (var_8 + 2)) * (var_8 + 3)) * (var_8 + 4)) % 5))
  {
    goto sectarian;
  }
  else
  {
    goto amurca;
  }
  sectarian:
  {
  }

  goto outvalue;
  goto premorbidly;
  amurca:
  {
  }

  goto agacerie;
  premorbidly:
  {
  }

  var_7 = (42 + ((((var_3 * var_3) * (var_3 + 1)) * (var_3 + 2)) % 3)) + (((((var_8 * var_8) * (var_8 + 1)) * (var_8 + 2)) * (var_8 + 3)) % 4);
  outvalue:
  {
  }

  goto theopathy;
  goto warlordism;
  agacerie:
  {
  }

  goto stour;
  warlordism:
  {
  }

  theopathy:
  {
  }

  var_8++;
  swap(&var_4[var_8], &var_4[var_9]);
  goto lapidified;
  stour:
  {
  }

  lapidified:
  {
  }

  var_9++;
  goto cytitis;
  etherialising:
  {
  }

  swap(&var_4[var_8 + 1], &var_4[var_6]);
  return var_8 + 1;
}

void quickSort(int var_10[], int var_11, int var_12)
{
  if ((var_11 < var_12)  ||  ((((var_9 * var_9) * (var_9 + 1)) * (var_9 + 2)) % 3))
  {
    goto rivet;
  }
  else
  {
    goto turrilite;
  }
  rivet:
  {
  }

  goto upvalley;
  goto pelargikon;
  turrilite:
  {
  }

  var_9 = ((42 + (((var_3 * var_3) * (var_3 + 1)) % 2)) + (((((var_9 * var_9) * (var_9 + 1)) * (var_9 + 2)) * (var_9 + 3)) % 4)) + ((((var_9 * var_9) * (var_9 + 1)) * (var_9 + 2)) % 3);
  goto maladjustment;
  pelargikon:
  {
  }

  var_7 = 42 + (((((var_7 * var_7) * (var_7 + 1)) * (var_7 + 2)) * (var_7 + 3)) % 4);
  upvalley:
  {
  }

  var_7 = (42 + (((((var_9 * var_9) * (var_9 + 1)) * (var_9 + 2)) * (var_9 + 3)) % 4)) + (((((var_8 * var_8) * (var_8 + 1)) * (var_8 + 2)) * (var_8 + 3)) % 4);
  goto quadridentate;
  quadridentate:
  {
  }

  goto araneidan;
  var_13 = 42 + (((((var_7 * var_7) * (var_7 + 1)) * (var_7 + 2)) * (var_7 + 3)) % 4);
  goto snipefish;
  blurringly:
  {
  }

  snipefish:
  {
  }

  var_3 = 42 + (((((var_7 * var_7) * (var_7 + 1)) * (var_7 + 2)) * (var_7 + 3)) % 4);
  goto nonpermeable;
  maladjustment:
  {
  }

  goto promptress;
  promptress:
  {
  }

  goto cemetery;
  goto unboiled;
  pharisaean:
  {
  }

  var_7 = ((42 + (((((var_9 * var_9) * (var_9 + 1)) * (var_9 + 2)) * (var_9 + 3)) % 4)) + (((var_7 * var_7) * (var_7 + 1)) % 2)) + (((((var_7 * var_7) * (var_7 + 1)) * (var_7 + 2)) * (var_7 + 3)) % 4);
  unboiled:
  {
  }

  nonpermeable:
  {
  }

  araneidan:
  {
  }

  var_13 = partition(var_10, var_11, var_12) + (((((var_9 * var_9) * (var_9 + 1)) * (var_9 + 2)) * (var_9 + 3)) % 4);
  quickSort(var_10, var_11, var_13 - 1);
  quickSort(var_10, var_13 + 1, var_12);
  goto fluors;
  cemetery:
  {
  }

  fluors:
  {
  }

}

