function signCheck(numOne, numTwo, numThree) {
  let result = numOne * numTwo * numThree;
  if (result > 0) {
    return 'Positive';
  } else if (result < 0) {
    return 'Negative';
  } else {
    return 'Zero';
  }
}

console.log(signCheck(5, 12, -15));
console.log(signCheck(-6, -12, 14));
console.log(signCheck(-1, -2, -3));
console.log(signCheck(-5, 1, 1));
