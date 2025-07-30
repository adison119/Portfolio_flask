// header contect spell
const message = "Hey, I'm Adison Weluwanarak";
const textElement = document.getElementById("text")
let charIndex = 0;
const typingSpeed = 100;

// function spell text
function typeWriter() {
    if (charIndex < message.length ) {
        textElement.innerHTML =message.substring(0,charIndex+1) + '<span class="cursor"></span>';
        charIndex++;
        setTimeout(typeWriter,typingSpeed);
    }
    else {
        textElement.innerHTML = message + '<span class="cursor"></span>';
    }
}
// start when load web
window.addEventListener('load', () =>{
    setTimeout(typeWriter,500)
})