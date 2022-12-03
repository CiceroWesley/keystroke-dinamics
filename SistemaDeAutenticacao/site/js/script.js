var keysPress = []
var keysPressTime = []
var keysRelease = []
var keysReleaseTime = []

const password = "roberto"


function press(event)
{
    let d = new Date()
    let time = d.getTime() / 1000
    let tecla = event.key
    //console.log(time)
    
    keysPress.push(tecla)
    keysPressTime.push(time)

    //console.log(tecla)
}

function release(event)
{
    let d = new Date()
    let time = d.getTime() / 1000
    let tecla = event.key
    //console.log(time)

    keysRelease.push(tecla)
    keysReleaseTime.push(time)

    //console.log(tecla)
}

const enviar = () => {
    let keys = ''

    for(let i = 0; i < keysPress.length; i++){
        keys += keysPress[i]
    }
    let wrong = false

    if(password != keys){
        wrong = true
    }
    //console.log(keys)
    //console.log(password)

    //se a senha está errada, resetar tudo
    if(wrong){
        alert("A senha está errada")
        keysPress = []
        keysRelease = []
        keysPressTime = []
        keysReleaseTime = []
        let textInput = document.getElementById("textInput")
        textInput.value = ""
        return null
    }

    let timeHoldDD = []

    for(let i = 0; i < keysPressTime.length; i++ ){
        //console.log(keysReleaseTime[i])
        //console.log(keysPressTime[i])
        //console.log(keysReleaseTime[i] - keysPressTime[i])
        timeHoldDD.push(keysReleaseTime[i] - keysPressTime[i])
    }
    
    //console.log(timeHoldDD)

    let timeDD = []

    for(let i = 0; i < keysPressTime.length - 1; i++){
        timeDD.push(keysPressTime[i+1] - keysPressTime[i])
    }

    //console.log(timeDD)

    for(let i = 0; i < timeDD.length; i++){
        timeHoldDD.push(timeDD[i])
    }

    let user = document.getElementById("users")
    console.log(user.value)
    timeHoldDD.push(user.value)
    console.log(timeHoldDD)

    //enviar o timeHoldDD para o backend para fazer o testo com o classificador já treinado
    //enviar também o nome do usuário pego do select
    //console.log(JSON.stringify(timeHoldDD))
    let resultado = document.getElementById("result")
fetch("http://127.0.0.1:5000/learn", {
  method: "POST",
  headers: {'Content-Type': 'application/json'}, 
  body: JSON.stringify(timeHoldDD)
}).then(res => {
  res.text()
  .then((result)=>{
    if(result == "True"){
        window.location.href = "./painel.html";
    } else{
        resultado.innerHTML = "Erro na autenticação."
    }
    console.log(result)
  })
}).catch(err => {
    console.log(err)
})
    //após enviar, resetar tudo
    keysPress = []
    keysRelease = []
    keysPressTime = []
    keysReleaseTime = []
    let textInput = document.getElementById("textInput")
    textInput.value = ""
}