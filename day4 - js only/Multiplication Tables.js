function multiplicationTable(row,col){
  let res = [];
  for (let i=1; i<=row; i++) {
    let tmp = [];  
    for (let j=1; j<=col; j++) {
      tmp.push(j*i);
    }
    res.push(tmp);
  }
  return res;
}
