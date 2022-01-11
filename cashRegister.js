function checkCashRegister(price, cash, cid) {

    let aux = (cash-price)*100;
    let holderArr = [];
   let quantArr = [["PENNY", 1], ["NICKEL", 5], ["DIME", 10], ["QUARTER", 25], ["ONE", 100], ["FIVE", 500], ["TEN", 1000], ["TWENTY", 2000], ["ONE HUNDRED", 10000]];
  let resultado=[]
  let coincounter =[];
  
  
  //prep
  
  for (let i = 0; i < quantArr.length; i++) {
    holderArr[i] = cid[i][1]*100;
  }
  
  for (let i=0;i<quantArr.length;i++){
    coincounter[i] = holderArr[i]/quantArr[i][1]
  }
  
  //aqui gera o troco
  
  for (let i=holderArr.length-1; i>=0;i--){
  
    let contador = 0;
    while (quantArr[i][1] <= aux && coincounter[i] > 0){
      aux = aux-quantArr[i][1];
      coincounter[i]--;
      contador++;
    }
  
    if (contador != 0){
      resultado.push([quantArr[i][0],((contador*quantArr[i][1])/100)])
    }
  }
  
  //aqui checa se falta dar troco ainda
  
  if (aux > 0){
    return {status: "INSUFFICIENT_FUNDS", change: []};
  }
  
  
  
  //aqui checa se acabou o troco do caixa
  
  let checker = false;
  
  for (let i=0;i<coincounter.length;i++){
    if (coincounter[i] != 0){
      checker = true;
    }
  }
  
  if (checker == false){
    console.log({status: "CLOSED", change:cid})
    return {status: "CLOSED", change:cid};
  }
  
  for (let i=0;i<resultado.length;i++){
    console.log(resultado[i])
  }
  
  console.log({status:"OPEN", change: resultado})
  return {status:"OPEN", change: resultado};
  
  
  }
  
  checkCashRegister(19.5, 20, [["PENNY", 1.01], ["NICKEL", 2.05], ["DIME", 3.1], ["QUARTER", 4.25], ["ONE", 90], ["FIVE", 55], ["TEN", 20], ["TWENTY", 60], ["ONE HUNDRED", 100]]);