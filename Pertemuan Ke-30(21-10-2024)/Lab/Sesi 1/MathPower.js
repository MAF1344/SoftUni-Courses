function pow(num, power) {
  let result = 1;
  for (let i = 0; i < power; i++) {
    result *= num;
  }
  return result;
}

console.log(pow(2, 8));
console.log(pow(3, 4));
