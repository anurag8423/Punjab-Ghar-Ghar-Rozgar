
let mute=true;
function toggle(){
  if(mute==true){mute=false; alert("sound ON");}
  else if(mute==false){mute=true; alert("sound OFF");}
}
let synth = window.speechSynthesis;




function speak(text) {
    stopSpeaking(); // Stop any ongoing speech
    console.log(text)
    synth = window.speechSynthesis;
    let utterance = new SpeechSynthesisUtterance(text);
    utterance.lang = 'hi-IN';
    if(mute==false){
    synth.speak(utterance);
    }
}

function stopSpeaking() {
    if (synth.speaking) {
        synth.cancel();
    }
}

const loginAudio= document.getElementById("loginAudio");
function playLoginAudio (){
  loginAudio.play();
}
function pauseLoginAudio(){
  console.log("rok")
  loginAudio.pause();

}


const availablejobAudio=document.getElementById("availablejobs")
function playAvailablejobsAudio(){
  console.log("hh")
  availablejobAudio.play();
}
function pauseAvailablejobsAudio(){
  console.log("rok")
  availablejobAudio.pause();

}



const privatejobAudio=document.getElementById("privateJobs")
function playPrivatejobsAudio(){
  console.log("pt")
  privatejobAudio.play();
}
function pausePrivatejobsAudio() {
  privatejobAudio.pause();
}
