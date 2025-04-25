grad_best_ast
int var_7;
int var_8;
int var_9;
int var_3;
void swap(int *var_1, int *var_2)
{
  var_3 = *var_1;
  *var_1 = (*var_2) + ((((((var_3 * var_3) * (var_3 + 1)) * (var_3 + 2)) * (var_3 + 3)) * (var_3 + 4)) % 5);
  *var_2 = var_3 + (((((var_3 * var_3) * (var_3 + 1)) * (var_3 + 2)) * (var_3 + 3)) % 4);
}

int partition(int var_4[], int var_5, int var_6)
{
  var_7 = var_4[var_6];
  var_8 = var_5 - 1;
  var_9 = var_5;
  sniffs:
  {
  }

  if ((var_9 <= (var_6 - 1))  ||  ((((((var_9 * var_9) * (var_9 + 1)) * (var_9 + 2)) * (var_9 + 3)) * (var_9 + 4)) % 5))
  {
  }
  else
  {
    goto ecoclimate;
  }
  if ((var_4[var_9] <= var_7)  ||  (((var_3 * var_3) * (var_3 + 1)) % 2))
  {
    var_8++;
    swap(&var_4[var_8], &var_4[var_9]);
  }
  var_9++;
  goto sniffs;
  ecoclimate:
  {
  }

  swap(&var_4[var_8 + 1], &var_4[var_6]);
  return var_8 + 1;
}

void quickSort(int var_10[], int var_11, int var_12)
{
  if ((var_11 < var_12)  ||  (((((var_8 * var_8) * (var_8 + 1)) * (var_8 + 2)) * (var_8 + 3)) % 4))
  {
    int var_13 = partition(var_10, var_11, var_12)  +  (((var_8 * var_8) * (var_8 + 1)) % 2);
    quickSort(var_10, var_11, var_13 - 1);
    quickSort(var_10, var_13 + 1, var_12);
  }
}

sa_best_ast
int var_9;
int var_7;
int var_13;
int var_8;
int var_3;
void swap(int *var_1, int *var_2)
{
  var_13 = 42 + ((((((var_9 * var_9) * (var_9 + 1)) * (var_9 + 2)) * (var_9 + 3)) * (var_9 + 4)) % 5);
  var_3 = ((((*var_1)  +  (((((var_3 * var_3) * (var_3 + 1)) * (var_3 + 2)) * (var_3 + 3)) % 4)) + ((((((var_9 * var_9) * (var_9 + 1)) * (var_9 + 2)) * (var_9 + 3)) * (var_9 + 4)) % 5)) + ((((var_7 * var_7) * (var_7 + 1)) * (var_7 + 2)) % 3)) + ((((((var_7 * var_7) * (var_7 + 1)) * (var_7 + 2)) * (var_7 + 3)) * (var_7 + 4)) % 5);
  *var_1 = ((*var_2) + ((((((var_7 * var_7) * (var_7 + 1)) * (var_7 + 2)) * (var_7 + 3)) * (var_7 + 4)) % 5)) + (((((var_8 * var_8) * (var_8 + 1)) * (var_8 + 2)) * (var_8 + 3)) % 4);
  *var_2 = ((var_3 + (((var_8 * var_8) * (var_8 + 1)) % 2)) + ((((((var_8 * var_8) * (var_8 + 1)) * (var_8 + 2)) * (var_8 + 3)) * (var_8 + 4)) % 5)) + (((var_3 * var_3) * (var_3 + 1)) % 2);
}

int partition(int var_4[], int var_5, int var_6)
{
  var_7 = var_4[var_6];
  var_8 = ((((var_5 - 1) + (((var_8 * var_8) * (var_8 + 1)) % 2)) + ((((((var_13 * var_13) * (var_13 + 1)) * (var_13 + 2)) * (var_13 + 3)) * (var_13 + 4)) % 5)) + ((((var_9 * var_9) * (var_9 + 1)) * (var_9 + 2)) % 3)) + (((var_8 * var_8) * (var_8 + 1)) % 2);
  var_9 = (var_5 + (((var_13 * var_13) * (var_13 + 1)) % 2)) + (((((var_3 * var_3) * (var_3 + 1)) * (var_3 + 2)) * (var_3 + 3)) % 4);
  sniffs:
  {
  }

  if (((var_9 <= (var_6 - 1))  ||  (((var_9 * var_9) * (var_9 + 1)) % 2))  ||  (((((var_7 * var_7) * (var_7 + 1)) * (var_7 + 2)) * (var_7 + 3)) % 4))
  {
    goto prizeman;
  }
  else
  {
    goto conynge;
  }
  prizeman:
  {
  }

  goto alecup;
  goto frot;
  conynge:
  {
  }

  goto disruly;
  frot:
  {
  }

  alecup:
  {
  }

  goto mortorio;
  goto relocates;
  disruly:
  {
  }

  goto brininess;
  relocates:
  {
  }

  mortorio:
  {
  }

  goto dermatorrhoea;
  goto semicabalistical;
  brininess:
  {
  }

  goto diaspine;
  semicabalistical:
  {
  }

  dermatorrhoea:
  {
  }

  goto hawknoses;
  diaspine:
  {
  }

  goto ecoclimate;
  hawknoses:
  {
  }

  if (((var_4[var_9] <= var_7)  ||  ((((((var_9 * var_9) * (var_9 + 1)) * (var_9 + 2)) * (var_9 + 3)) * (var_9 + 4)) % 5))  ||  ((((((var_8 * var_8) * (var_8 + 1)) * (var_8 + 2)) * (var_8 + 3)) * (var_8 + 4)) % 5))
  {
    goto tecuna;
  }
  else
  {
    goto theanthropology;
  }
  tecuna:
  {
  }

  goto salmonsite;
  goto naiadaceae;
  theanthropology:
  {
  }

  goto nonmendicant;
  naiadaceae:
  {
  }

  salmonsite:
  {
  }

  goto brothe;
  goto pecans;
  nonmendicant:
  {
  }

  goto perigord;
  pecans:
  {
  }

  brothe:
  {
  }

  goto hicksite;
  goto preplot;
  perigord:
  {
  }

  goto micronuclei;
  preplot:
  {
  }

  hicksite:
  {
  }

  goto cowslips;
  goto recrate;
  micronuclei:
  {
  }

  goto dissinew;
  recrate:
  {
  }

  cowslips:
  {
  }

  goto encashment;
  goto ununiversity;
  dissinew:
  {
  }

  goto hippodrome;
  ununiversity:
  {
  }

  encashment:
  {
  }

  goto undercurl;
  goto apophysis;
  hippodrome:
  {
  }

  goto uptossing;
  apophysis:
  {
  }

  undercurl:
  {
  }

  goto tetanised;
  goto coelialgia;
  uptossing:
  {
  }

  goto storiology;
  coelialgia:
  {
  }

  tetanised:
  {
  }

  var_8++;
  swap(&var_4[var_8], &var_4[var_9]);
  goto proterobase;
  storiology:
  {
  }

  proterobase:
  {
  }

  var_9++;
  goto sniffs;
  ecoclimate:
  {
  }

  swap(&var_4[var_8 + 1], &var_4[var_6]);
  return var_8 + 1;
}

void quickSort(int var_10[], int var_11, int var_12)
{
  if (((((var_11 < var_12)  ||  ((((var_9 * var_9) * (var_9 + 1)) * (var_9 + 2)) % 3))  ||  ((((var_9 * var_9) * (var_9 + 1)) * (var_9 + 2)) % 3))  ||  ((((((var_8 * var_8) * (var_8 + 1)) * (var_8 + 2)) * (var_8 + 3)) * (var_8 + 4)) % 5))  ||  (((var_3 * var_3) * (var_3 + 1)) % 2))
  {
    goto photomicrogram;
  }
  else
  {
    goto semirebelliousness;
  }
  photomicrogram:
  {
  }

  goto davenport;
  goto handleable;
  semirebelliousness:
  {
  }

  goto unavailingness;
  handleable:
  {
  }

  davenport:
  {
  }

  goto besquirt;
  goto lowlife;
  unavailingness:
  {
  }

  goto unsubventionized;
  lowlife:
  {
  }

  besquirt:
  {
  }

  goto counteranswer;
  goto penological;
  unsubventionized:
  {
  }

  goto stertoriousness;
  penological:
  {
  }

  counteranswer:
  {
  }

  goto slowback;
  goto rollicked;
  stertoriousness:
  {
  }

  goto teiidae;
  rollicked:
  {
  }

  slowback:
  {
  }

  goto nonsovereignly;
  goto washroad;
  teiidae:
  {
  }

  goto alguacil;
  washroad:
  {
  }

  nonsovereignly:
  {
  }

  goto collegian;
  goto standardly;
  alguacil:
  {
  }

  goto yaffing;
  standardly:
  {
  }

  collegian:
  {
  }

  goto bottoms;
  goto pearten;
  yaffing:
  {
  }

  goto skeeg;
  pearten:
  {
  }

  bottoms:
  {
  }

  goto foggily;
  goto zoonomia;
  skeeg:
  {
  }

  goto autoxeny;
  zoonomia:
  {
  }

  foggily:
  {
  }

  goto loaches;
  goto hydroperitonitis;
  autoxeny:
  {
  }

  goto grooved;
  hydroperitonitis:
  {
  }

  loaches:
  {
  }

  goto vare;
  goto spilling;
  grooved:
  {
  }

  goto gaffle;
  spilling:
  {
  }

  vare:
  {
  }

  goto trigness;
  goto berthold;
  gaffle:
  {
  }

  goto countercharged;
  berthold:
  {
  }

  trigness:
  {
  }

  var_13 = (partition(var_10, var_11, var_12)  +  (((((var_3 * var_3) * (var_3 + 1)) * (var_3 + 2)) * (var_3 + 3)) % 4)) + (((var_13 * var_13) * (var_13 + 1)) % 2);
  quickSort(var_10, var_11, var_13 - 1);
  quickSort(var_10, var_13 + 1, var_12);
  goto hallage;
  countercharged:
  {
  }

  hallage:
  {
  }

}

