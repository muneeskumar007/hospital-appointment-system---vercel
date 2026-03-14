// Show message after booking appointment
function appointmentBooked() {
    alert("Appointment booked successfully!");
}


// Simple form validation for register page
function validateRegister() {

    let name = document.querySelector("input[name='name']").value;
    let email = document.querySelector("input[name='email']").value;
    let password = document.querySelector("input[name='password']").value;

    if(name === "" || email === "" || password === "") {
        alert("Please fill all fields");
        return false;
    }

    return true;
}


// Simple login validation
function validateLogin() {

    let email = document.querySelector("input[name='email']").value;
    let password = document.querySelector("input[name='password']").value;

    if(email === "" || password === "") {
        alert("Enter email and password");
        return false;
    }

    return true;
}


// // Highlight active navigation link
// document.addEventListener("DOMContentLoaded", function() {

//     let links = document.querySelectorAll("nav a");
//     let current = window.location.pathname;

//     links.forEach(link => {
//         if(link.getAttribute("href") === current){
//             link.style.fontWeight = "bold";
//         }
//     });

//     // Particle animation on auth pages
//     if(document.body.classList.contains('auth-page')){
//         initParticles();
//     }
// });
document.addEventListener("DOMContentLoaded", function(){

if(document.body.classList.contains('auth-page')){
initParticles();
}

});

// // Particle background
// function initParticles(){
//     const canvas = document.getElementById('particle-canvas');
//     if(!canvas) return;

//     const ctx = canvas.getContext('2d');
//     let particles = [];
//     const maxParticles = 70;

//     function resize(){
//         canvas.width = window.innerWidth;
//         canvas.height = window.innerHeight;
//     }

//     function random(min, max){
//         return Math.random() * (max - min) + min;
//     }

//     class Particle {
//         constructor(){
//             this.reset();
//         }

//         reset(){
//             this.x = random(0, canvas.width);
//             this.y = random(0, canvas.height);
//             this.radius = random(1.8, 3.8);
//             this.speed = random(0.2, 0.7);
//             this.angle = random(0, Math.PI * 2);
//             this.alpha = random(0.15, 0.45);
//             this.cos = Math.cos(random(0, Math.PI * 2));
//             this.sin = Math.sin(random(0, Math.PI * 2));
//         }

//         update(){
//             this.x += Math.cos(this.angle) * this.speed;
//             this.y += Math.sin(this.angle) * this.speed;
//             this.angle += 0.002;

//             if(this.x < -50 || this.x > canvas.width + 50 || this.y < -50 || this.y > canvas.height + 50) {
//                 this.reset();
//                 this.y = -20;
//             }
//         }

//         draw(){
//             ctx.beginPath();
//             ctx.fillStyle = `rgba(255,255,255,${this.alpha})`;
//             ctx.arc(this.x, this.y, this.radius, 0, Math.PI * 2);
//             ctx.fill();
//         }
//     }

//     function init(){
//         resize();
//         particles = Array.from({length: maxParticles}, () => new Particle());
//         animate();
//     }

//     function animate(){
//         ctx.clearRect(0, 0, canvas.width, canvas.height);
//         particles.forEach(p => {
//             p.update();
//             p.draw();
//         });
//         requestAnimationFrame(animate);
//     }

//     window.addEventListener('resize', resize);
//     init();
// }


function initParticles(){

const canvas = document.getElementById('particle-canvas');
if(!canvas) return;

const ctx = canvas.getContext('2d');

let particles = [];
const maxParticles = 70;

function resize(){
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;
}

function random(min,max){
return Math.random()*(max-min)+min;
}

class Particle{

constructor(){
this.reset();
}

reset(){

this.x = random(0,canvas.width);
this.y = random(0,canvas.height);

this.radius = random(2,5);

this.speed = random(0.2,0.6);

this.angle = random(0,Math.PI*2);

this.alpha = random(0.3,0.7);

this.type = Math.floor(random(0,3)); // shape type

}

update(){

this.x += Math.cos(this.angle)*this.speed;
this.y += Math.sin(this.angle)*this.speed;

this.angle += 0.002;

if(
this.x < -50 ||
this.x > canvas.width+50 ||
this.y < -50 ||
this.y > canvas.height+50
){
this.reset();
}

}

draw(){

ctx.save();

ctx.globalAlpha = this.alpha;

ctx.shadowColor="rgba(45,108,223,0.6)";
ctx.shadowBlur=10;

if(this.type===0){

/* circle bubble */

ctx.beginPath();
ctx.fillStyle="rgba(45,108,223,0.8)";
ctx.arc(this.x,this.y,this.radius,0,Math.PI*2);
ctx.fill();

}

else if(this.type===1){

/* medical plus */

ctx.fillStyle="rgba(45, 223, 63, 0.5)";

ctx.fillRect(this.x-2,this.y-6,4,12);
ctx.fillRect(this.x-6,this.y-2,12,4);

}

else{

/* floating square */

ctx.fillStyle="rgba(120,160,255,0.6)";
ctx.fillRect(this.x,this.y,this.radius*2,this.radius*2);

}

ctx.restore();

}

}

function init(){

resize();

particles = Array.from({length:maxParticles},()=>new Particle());

animate();

}

function animate(){

ctx.clearRect(0,0,canvas.width,canvas.height);

particles.forEach(p=>{
p.update();
p.draw();
});

requestAnimationFrame(animate);

}

window.addEventListener("resize",resize);

init();

}