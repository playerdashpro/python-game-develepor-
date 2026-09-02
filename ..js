let startButton =
this, agai
document.getElementById("startButton");

let restartButton =
document.getElementById("restartButton");

let game = document.querySelector(".game");

let car1 = document.querySelector(".car1");

let car2 = document.querySelector(".car2");

let car3 = document.querySelector(".car3");

let finishedCars = 0;

startButton.addEventListener("click", function() {

game.classList.add("racing");

startButton.style.display = "none";

});

car1.addEventListener(
"animationend"
carFinished

);

car2.addEventListener(
"animationend",
carFinished

);

car3.addEventListener(
"animationend",
carFinished 

funcrtion carFinished() {
finishedCars++;
if (finishedCars === 3) {
restartButton.style.display = "block";
    }
}
restartbuttton.addEventListener("click", function() {
game.classList.remove("racing");
car1.style.transform = "translateX(0)";
car2.style.transform = "translateX(0)";
car3.style.transform = "translateX(0)";
finishedCars = 0;
restartButton.style.display = "none";
startButton.style.display = "block";
});