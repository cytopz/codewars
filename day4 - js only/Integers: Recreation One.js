function listSquared(m, n) {
  const listOfDivisors = n => {
    let arr = [];
    for (let i=1; i<=n; i++) {
      if (n % i === 0) arr.push(i*i);
    }
    return arr;
  }
  const sum = num => {
    return listOfDivisors(num).reduce((a, b) => a+b) 
  }
  const isSquared = num => {
    return Math.sqrt(sum(num)) % 1 === 0
  }
  res = [];
  for (let i=m; i<=n; i++) {
    if (isSquared(i)) res.push([i, sum(i)]);
  }
  return res;
}
