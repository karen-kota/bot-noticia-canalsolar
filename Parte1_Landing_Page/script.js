let segundos = 0;
let minutos = 0;

function incrementaSegundos(){
    segundos++;
    if (segundos < 10) {
        segundos = "0" + segundos
    }  else {
        segundos = segundos
    }

    if(segundos==60){
        minutos++;
        if (minutos < 10) {
            minutos = "0" + minutos
        } else {
            minutos = minutos
        }        segundos=0;

        document.getElementById('minuto').innerHTML=minutos
    }
    document.getElementById('segundo').innerHTML=segundos
}

setInterval(function(){ incrementaSegundos() },1000)