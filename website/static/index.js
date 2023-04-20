// Get the modal
var modal = document.getElementById("my-Modal");

// Get the button that opens the modal
var asyBtn = document.getElementById("asyBtn");
var wheelBtn = document.getElementById("wheelBtn");
var discBtn = document.getElementById("discBtn");

var lineOptions = document.querySelectorAll(".lineOptions li");
var lineOptionLinks = document.querySelectorAll(".lineOptions a");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

function removeLiItems() {
  var existingLi4 = document.querySelector(".lineOptions li:nth-child(4)");
  if (existingLi4 && (existingLi4.textContent === "461" || existingLi4.textContent === "458")) {
    existingLi4.remove();
  }

  var existingLi3 = document.querySelector(".lineOptions li:nth-child(3)");
  if (existingLi3 && (existingLi3.textContent === "461" || existingLi3.textContent === "458")) {
    existingLi3.remove();
  }

  var existingLi5 = document.querySelector(".lineOptions li:nth-child(5)");
  if (existingLi5 && existingLi5.textContent === "458") {
    existingLi5.remove();
  }
}

// When the user clicks on the button, open the modal
asyBtn.onclick = function() {
  removeLiItems();
  modal.style.display = "block";
  // Reset the options to their original values
  lineOptions[0].innerHTML = "471";
  lineOptions[1].innerHTML = "474";
  lineOptionLinks[0].setAttribute("href", "/471");
  lineOptionLinks[1].setAttribute("href", "/474");
  

}

wheelBtn.onclick = function(){
  modal.style.display = "block";
  removeLiItems();
  // Change the options
  lineOptions[0].innerHTML = "424";
  lineOptions[1].innerHTML = "429";
  lineOptionLinks[0].setAttribute("href", "/424");
  lineOptionLinks[1].setAttribute("href", "/429");

  // Remove options 461 and 458 if present

};

discBtn.onclick = function(){
  modal.style.display = "block";
  lineOptions[0].innerHTML = "456";
  lineOptions[1].innerHTML = "457";
  lineOptionLinks[0].setAttribute("href", "/456");
  lineOptionLinks[1].setAttribute("href", "/457");
  
  // Check if 459 is already added to the list
  var existingLi = document.querySelector(".lineOptions li:nth-child(3)");
  if (!existingLi) {
    // Add the new list items and links
    var li1 = document.createElement("li");
    var a1 = document.createElement("a");
    var text1 = document.createTextNode("458");
    a1.appendChild(text1);
    a1.setAttribute("href", "/458");
    li1.appendChild(a1);
    var ul = document.querySelector(".lineOptions");
    ul.appendChild(li1);
    
    var li2 = document.createElement("li");
    var a2 = document.createElement("a");
    var text2 = document.createTextNode("461");
    a2.appendChild(text2);
    a2.setAttribute("href", "/461");
    li2.appendChild(a2);
    ul.appendChild(li2);
  }
  

}

closeB = document.querySelector('.closeB')
closeB.onclick = function() {
  modal.style.display = "none";
}


const banner = document.getElementById("banner");
const closeBtn = document.getElementById("closeBtn");

closeBtn.addEventListener("click", function() {
  banner.style.display = "none";
});