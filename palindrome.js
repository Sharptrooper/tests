function palindrome(str) {
    let aux = [...str];
    //let aux = "1 eye for of 1 eye."
    let holderArr=[];
    for (let i=0;i<aux.length;i++){
      if (RegExp(/[a-zA-Z0-9]/).test(aux[i])){
        console.log('ping: '+aux[i])
        holderArr.push(aux[i].toUpperCase())
      }
    }
    console.log('holderArr: '+holderArr)
    let mirrorArr=[];
  
    for (let i=holderArr.length-1;i>=0;i--){
      console.log("i: "+i+" e valor: "+holderArr[i])
      mirrorArr.push(holderArr[i])
    }
    mirrorArr = mirrorArr.join('');
    holderArr = holderArr.join('');
  
    if (mirrorArr === holderArr){
      return true;
    }else{
      return false;
    }
  
  }
  
  
  
  palindrome("eye");