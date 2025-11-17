var myName = [];
var myAge = [];
var myBool = [];

var jsname=document.getElementById("namein");
var jsage=document.getElementById("agein")
var jsbool=document.getElementById("boolin")

function getdata(){
    myName.push(jsname.value)
    myAge.push(jsage.value)
    myBool.push(jsbool.value)
}