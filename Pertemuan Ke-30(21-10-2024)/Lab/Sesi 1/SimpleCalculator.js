function solve(a, b, operator) {
  switch (operator) {
    case 'multiply':
      multiply(a, b);
      break;
    case 'divide':
      divide(a, b);
      break;
    case 'add':
      add(a, b);
      break;
    case 'subtract':
      substract(a, b);
      break;
  }
  function multiply(a, b) {
    console.log(a * b);
  }

  function divide(a, b) {
    console.log(a / b);
  }

  function add(a, b) {
    console.log(a + b);
  }

  function substract(a, b) {
    console.log(a - b);
  }
}

solve(5, 5, 'multiply');
solve(40, 8, 'divide');
solve(12, 19, 'add');
solve(50, 13, 'subtract');