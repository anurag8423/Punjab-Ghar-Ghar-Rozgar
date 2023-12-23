function addNewAch() {
    let newNode=document.createElement("textarea");
    newNode.classList.add("form-control");
    newNode.classList.add("achFeild");
    newNode.classList.add("mt-2");
    newNode.setAttribute('rows',3);
    newNode.setAttribute('placeholder',"enter your achievents")
    newNode.style.height="10em"
    let achOb = document.getElementById("ach"); 
    let achButtonOb = document.getElementById("achButton");
    achOb.insertBefore(newNode, achButtonOb);

}

function addNewWe() {
    let newNode=document.createElement("textarea");
    newNode.classList.add("form-control");
    newNode.classList.add("weFeild");
    newNode.classList.add("mt-2");
    newNode.setAttribute('rows',3);
    newNode.setAttribute('placeholder',"Other Experience")
    newNode.style.height="10em"
    let weOb= document.getElementById("we");
    let weButtonOb=document.getElementById("weButton");
    weOb.insertBefore(newNode, weButtonOb);
}

function addNewAc() {
    let newNode=document.createElement("textarea");
    newNode.classList.add("form-control");
    newNode.classList.add ("acFeild");
    newNode.classList.add ("mt-2");
    newNode.style.height="10em"
    let acOb=document.getElementById('ac');
    let acButtonOb=document.getElementById("acButton");
    acOb.insertBefore(newNode, acButtonOb)
}

function generateCV(){
  let nameField=document.getElementById("nameField").value;
  let nameT1=document.getElementById("NameT1");
  let nameT2=document.getElementById("NameT2");
  nameT1.innerHTML=nameField;
  nameT2.innerHTML=nameField;
  document.getElementById("contactT").innerHTML=document.getElementById("contact").value;
  document.getElementById("emailT").innerHTML=document.getElementById("email").value;
  document.getElementById("adressT").innerHTML=document.getElementById("adress").value;
  document.getElementById("linkedinT").innerHTML="<p><b>LinkedIn<b></p>"
  document.getElementById("socialT").innerHTML="<p><b>Github<b></p>"
  document.getElementById("linkedinT").href=document.getElementById("linkedin").value;
  document.getElementById("socialT").href=document.getElementById("social").value;

let ach=document.getElementsByClassName("achField")
let str='';
for(let e of ach){
    str=str+ `<li> ${e.value} </li>`;
}

document.getElementById("achT").innerHTML= str;

let wef=document.getElementsByClassName("weField")
let sts='';
for(let e of wef){
    sts=sts+ `<li> ${e.value} </li>`;
}

document.getElementById("weT").innerHTML= sts;

let acd=document.getElementsByClassName("acField")
let stt='';
for(let e of acd){
    stt=stt+ `<li> ${e.value} </li>`;
}

document.getElementById("acT").innerHTML= stt;

let file=document.getElementById('image').files[0];
let read=new FileReader();
read.readAsDataURL(file);
read.onloadend = function(){
    document.getElementById("imageT").src= read.result;
}

document.getElementById('cv-form').style.display='none';
document.getElementById('cv-template').style.display="block";
document.getElementById('printbtn').style.display="block";
}

// Function to download web content as PDF
function downloadAsPDF() {
    // Get the element containing the content you want to convert to PDF
    document.getElementById('printbtn').style.display="none";
    var element = document.getElementById("cv-template");

    // Use html2pdf library to create a PDF
    html2pdf(element);
    setTimeout(function() {
        document.getElementById('printbtn').style.display="block";
      }, 2000);
  }