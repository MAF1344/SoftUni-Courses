function formatGrade(grade) {
  if (grade < 3.0) {
    console.log('Fail (2)');
  } else if (grade < 3.5) {
    console.log(`Poor (${grade})`);
  } else if (grade < 4.5) {
    console.log(`Good (${grade})`);
  } else if (grade < 5.5) {
    console.log(`Very Good (${grade})`);
  } else {
    console.log(`Excellent (${grade})`);
  }
}

formatGrade(3.33);
formatGrade(4.50);
formatGrade(2.99);
