function rot13(str) {
  let resultado =[];
  let aux = [...str];

  for (let i=0;i<aux.length;i++){
    if (RegExp(/[\W\s]/).test(aux[i])){
      resultado.push(aux[i])
    }else{

    
    let holder = aux[i].charCodeAt(0)

    if (RegExp(/[0-9\W]/).test(String.fromCharCode(holder-13))){
      resultado.push(String.fromCharCode(holder+13))
    }else{
      resultado.push(String.fromCharCode(holder-13))
    }


    }
  }
  resultado = resultado.join('');

  console.log(resultado)
  return resultado;
}

rot13("SERR PBQR PNZC");
