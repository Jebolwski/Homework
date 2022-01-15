let number = document.querySelector("#number");
let answer = document.querySelector("#answer");
const posnegzer = () => {
    if(number.value=="" || null){
        answer.innerHTML="Bir sayı girin";
    }

    else if(number.value>0){
        answer.innerHTML="Sıfırdan Büyük";
        console.log("Sıfırdan Büyük");
    } 
    else if(number.value<0){
        answer.innerHTML="Sıfırdan Küçük";
        console.log("Sıfırdan Küçük");
    }
    else{
        answer.innerHTML="0";
        console.log("Sıfır");
    }
}