function telephoneCheck(str) {
    let aux = [...str];
    let counter = 0;
    let checkCC = 0;
  
  
    //garantir que começa com um numero ou ()
    if (aux[0] == '-'){
      return false;
    }
  
    //ver se ter caracteres proibidos
    for (let i=0;i<aux.length;i++){
      if (RegExp(/[!@#$%¨&*?]/).test(aux[i])){
        return false;
      }
      if (RegExp(/[)]/).test(aux[i])){
        if (RegExp(/[(]/).test(aux[i-4]) == false){
          return false;
        }
      }
  
      if (RegExp(/[(]/).test(aux[i])){
        if (RegExp(/[)]/).test(aux[i+4]) == false){
          return false;
        }
      }
  
    }
  
    //ver quantos digitos tem
    for (let i=0;i<aux.length;i++){
      if (RegExp(/[0-9]/).test(aux[i])){
        console.log("numero: "+aux[i] + " counter: "+counter)
        counter = counter+1;
      }
    }
  
    //ver se tem o numero certo de digitos
  
    if (counter < 10 || counter >= 12){
    return false;
  }
  
    // verificar se tem country code e se é 1
    if (counter == 11){
      for (let i=0;i<aux.length;i++){
        if (RegExp(/[0-9]/).test(aux[i])){
          if (aux[i] == 1){
            checkCC = 1;
            break;
          } else{
            return false;
          }
        }
      }
    }
  
    //já retornar true caso seja um sanduiche de numeros
    if (counter == aux.length){
      return true;
    }
  
    if (checkCC == 1){
      if (RegExp(/^1[\s()-]*[0-9]{3}[\s()-]*[0-9]{3}[\s()-][0-9]{4}/).test(str) == false){
        return false;
      }
    }else{
  
      if (RegExp(/[0-9]{3}[\s()-][0-9]{3}[\s()-][0-9]{4}/).test(str) == false){
        return false;
      }
    }
  
    
  
  
  
    return true;
  }
  
  telephoneCheck("555-555-5555");