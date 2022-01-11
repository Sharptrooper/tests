// 1000 = m, 500 = d, 100 = c, 50 = l, x =10, v =5, i =1

function convertToRoman(num) {

    let romanArr=[];
  
    if (num>=1000){
      let aux = num.toString().split('');
      for (let i=0;i<aux[0];i++){
        romanArr.push("M")
      }
      num = num % 1000;
    }
  
  
    if (num >100){
      let aux = num.toString().split('')
      if (aux[0] < 5 && aux[0] != 4){
        for (let i=0;i<aux[0];i++){
          romanArr.push("C");
        }
      }
      else if(aux[0] >= 5 && aux[0] < 10 && aux[0] != 9){
        romanArr.push("D");
        for(let i=5;i<aux[0];i++){
          romanArr.push("C")
        }
      }else if(aux[0] == 4){
        romanArr.push("CD")
      }else if(aux[0]==9){
        romanArr.push("CM")
      }else{
        console.log('wtf man')
      }
      num = num % 100;
    }
  
  
    if (num >10){
      console.log("num dezena: "+num)
      let aux = num.toString().split('')
      if (aux[0] < 5 && aux[0] != 4){
        for (let i=0;i<aux[0];i++){
          romanArr.push("X");
        }
      }
      else if(aux[0] >= 5 && aux[0] < 10 && aux[0] != 9){
        romanArr.push("L");
        for(let i=5;i<aux[0];i++){
          romanArr.push("X")
        }
      }else if(aux[0] == 4){
        romanArr.push("XL")
      }else if(aux[0]==9){
        romanArr.push("XC")
      }else{
        console.log('wtf man')
      }
      num = num % 10;
    }
  
  
      if (num >=1){
        console.log("num unidade: "+num)
      let aux = num.toString().split('')
      if (aux < 5 && aux != 4){
        for (let i=0;i<aux;i++){
          romanArr.push("I");
        }
      }
      else if(aux >= 5 && aux < 10 && aux != 9){
        romanArr.push("V");
        for(let i=5;i<aux;i++){
          romanArr.push("I")
        }
      }else if(aux == 4){
        romanArr.push("IV")
      }else if(aux==9){
        romanArr.push("IX")
      }else{
        console.log('wtf man')
      }
      num = num % 1;
    }
  romanArr = romanArr.join('')
  
  console.log(romanArr)
   
  
   return romanArr;
  }
  
  convertToRoman(36);