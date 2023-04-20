

function openNav() {
  document.getElementById("mySidenav").style.width = "250px";
  document.getElementById("main").classList.add("pushed");
}

function closeNav() {
  document.getElementById("mySidenav").style.width = "0";
  document.getElementById("main").classList.remove("pushed");
}



// Call the openNav function when the page loads
window.onload = function() {
  openNav();
}

const resetLink = document.getElementById('resetLink')
resetLink.addEventListener('click', function(event) {
  event.preventDefault();
  const formContainer = document.querySelector('#formContainer');
  formContainer.style.justifyContent = 'center';
  const existingForm = formContainer.querySelector('form');
  if (existingForm) {
    formContainer.removeChild(existingForm);
  }
  if (!formContainer.querySelector('form')) {
    const formElement = document.createElement('form');

    formElement.method = 'post';
    const currentUrl = window.location.href;
    formElement.action = currentUrl;
    formElement.name ="reset_form";

    // Create hidden input field for reset_form
    const resetFormInput = document.createElement('input');
    resetFormInput.type = 'hidden';
    resetFormInput.name = 'reset_form';
    resetFormInput.value = 'true';
    formElement.appendChild(resetFormInput);

    // Create container for form elements
    const formContent = document.createElement('div');

    const formLabel = document.createElement('h1');
    formLabel.innerHTML = "Reset Your Password Here!";
    formContent.appendChild(formLabel);

    // Create container div for input fields
    const inputContainer = document.createElement('div');
    inputContainer.style.display = 'flex';
    inputContainer.style.flexDirection = 'column';
    inputContainer.style.gap = '10px';


    const passwordInput = document.createElement('input');
    passwordInput.type = 'password';
    passwordInput.name = 'password';
    passwordInput.placeholder = 'Enter current password';
    inputContainer.appendChild(passwordInput);

    
    const passwordInput1 = document.createElement('input');
    passwordInput1.type = 'password';
    passwordInput1.name = 'new_password';
    passwordInput1.placeholder = 'Enter New Password';
    inputContainer.appendChild(passwordInput1);

    const passwordInput2 = document.createElement('input');
    passwordInput2.type = 'password';
    passwordInput2.name = 'confirm_new_password';
    passwordInput2.placeholder = 'Confirm new passowrd';
    inputContainer.appendChild(passwordInput2);

    // Create container div for submit button
    const submitContainer = document.createElement('div');
    submitContainer.style.display = 'flex';
    submitContainer.style.justifyContent = 'flex-end';
    submitContainer.style.marginTop = '2px';

    const submitButton = document.createElement('button');
    submitButton.type = 'submit';
    submitButton.innerText = 'Reset';
    submitButton.style.width = '80px';
    submitButton.style.borderRadius = '5px';
    submitButton.style.backgroundColor = 'red';
    submitButton.style.fontWeight = 'bolder';
    submitButton.style.color = 'white';
    submitButton.style.cursor= 'pointer';
    submitContainer.appendChild(submitButton);

    // Add containers to form
    formContent.appendChild(inputContainer);
    formContent.appendChild(submitContainer);
    formElement.appendChild(formContent);
    formContainer.appendChild(formElement);
  
  }
});

const contactAdminLink = document.querySelector('#contactAdminLink');
contactAdminLink.addEventListener('click', function(event) {
  event.preventDefault();
  const formContainer = document.querySelector('#formContainer');
  const existingForm = formContainer.querySelector('form');
  if (existingForm) {
    formContainer.removeChild(existingForm);
  }
  const formElement = document.createElement('form');
  formElement.method = 'post';
  const currentUrl = window.location.href;
  formElement.action = currentUrl;
  formElement.name = 'contact_admin'

  const contactFormInput = document.createElement('input');
  contactFormInput.type = 'hidden';
  contactFormInput.name = 'contact_admin';
  contactFormInput.value = 'true';
  formElement.appendChild(contactFormInput);

  // Create container for form elements
  const formContent = document.createElement('div');

  const formLabel = document.createElement('h1')
  formLabel.innerHTML = "Contact Admin Here!"
  formContent.appendChild(formLabel);

  // Create container div for input fields
  const inputContainer = document.createElement('div');
  inputContainer.style.display = 'flex';
  inputContainer.style.flexDirection = 'column';
  inputContainer.style.gap = '10px';
  const fullName = document.getElementById('fullName');
  const nameInput = document.createElement('input');
  nameInput.type = 'text';
  nameInput.name = 'name';
  nameInput.value= fullName.textContent;
  nameInput.readOnly= true
  inputContainer.appendChild(nameInput);

  const emailInput = document.createElement('input');
  emailInput.type = 'email';
  emailInput.name = 'email';
  emailInput.placeholder = 'Enter your email';
  inputContainer.appendChild(emailInput);

  const messageInput = document.createElement('textarea');
  messageInput.name = 'message';
  messageInput.placeholder = 'Enter your message';
  inputContainer.appendChild(messageInput);

  // Create container div for submit button
  const submitContainer = document.createElement('div');
  submitContainer.style.display = 'flex';
  submitContainer.style.justifyContent = 'flex-end';
  submitContainer.style.marginTop = '2px';

  const submitButton = document.createElement('button');
  submitButton.type = 'submit';
  submitButton.innerText = 'Submit';
  submitButton.style.width = '80px';
  submitButton.style.borderRadius = '5px';
  submitButton.style.backgroundColor = 'red';
  submitButton.style.fontWeight = 'bolder';
  submitButton.style.color = 'white';
  submitButton.style.cursor= 'pointer';
  submitContainer.appendChild(submitButton);

  // Add containers to form
  formContent.appendChild(inputContainer);
  formContent.appendChild(submitContainer);
  formElement.appendChild(formContent);
  formContainer.appendChild(formElement);
});


const yourComments = document.querySelector('#yourComments');
const lastComment = document.querySelector('#lastComment');
lastComment.style.display='none';
lastComment.style.backgroundColor="black";
lastComment.style.color = 'white';
lastComment.style.borderRadius = "10px";
lastComment.style.justifyContent ='center';
lastComment.style.height = '200px';
lastComment.style.padding = '40px';
lastComment.style.marginTop = '80px';
lastComment.style.width ='400px';


const links = document.querySelectorAll('a:not(#yourComments):not(.closebtn)');

links.forEach(link => {
  link.addEventListener('click', function(event) {
    // get the comments container and the last comment element
    const commentsContainer = document.querySelector('#main');
    const lastComment = document.querySelector('#lastComment');


    // remove the last comment if it exists
    if (lastComment) {
      lastComment.style.display='none';
      
    }

    // Hide lastComment when any other link is clicked

    
  });
});


yourComments.addEventListener('click', function(event){
  event.preventDefault();
  const formContainer = document.querySelector('#formContainer');
  const existingForm = formContainer.querySelector('form');
  if (existingForm) {
    formContainer.removeChild(existingForm);
  }
  lastComment.style.display='block';
  lastComment.style.flexDirection='column';
});

// Wait for the DOM to be ready
document.addEventListener("DOMContentLoaded", function() {
  // Get the contactAdminLink element
  const contactAdminLink = document.getElementById('contactAdminLink');
  
  // Check if the user is an admin
  if (user.is_admin) {
    // If the user is an admin, hide the contactAdminLink
    contactAdminLink.style.display = 'none';
  }
});



const badge = document.querySelector('.badge');
const notification = document.querySelector('.notification')
const newComments = Number(badge.textContent);

if (newComments > 0) {
  badge.style.display = 'flex';
  notification.style.display= 'flex';
} else {
  badge.style.display = 'none';
  notification.style.display= 'none';
}


async function updateCommentCount(resetLastVisit = false) {
  const response = await fetch(`/get_new_comment_count?reset_last_visit=${resetLastVisit}`);
  const data = await response.json();
  const newComments = data.new_comment_count;

  badge.textContent = newComments;
  if (newComments > 0) {
    badge.style.display = "flex";
    notification.style.display = "flex";
  } else {
    badge.style.display = "none";
    notification.style.display = "none";
  }
}

// Add an event listener to the notification icon
notification.addEventListener("click", () => {
  updateCommentCount(true);
});

if (typeof user !== 'undefined') {
  const userObj = JSON.parse(document.body.dataset.user);
  console.log(userObj);
  // rest of your code that uses the user object
}