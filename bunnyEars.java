// We have a number of bunnies and each bunny has two big floppy ears.
// We want to compute the total number of ears across all the bunnies recursively (without loops or multiplication).

public int bunnyEars(int bunnies) {
  int ears;
  if (bunnies == 0){
    return 0;
  }
  else if (bunnies == 1){
    return 2;
  }
  else if (bunnies == 2){
    return 4;
  }
  else{
    ears = 2 + bunnyEars(bunnies-1);
    return ears;
  }
}
