
  const tableHeaders = document.querySelectorAll('#data-table th');

  // Add a click event listener to each table header cell
  tableHeaders.forEach(header => {
    header.addEventListener('click', () => {
      // get the h1 element with id "linenumb"
      const linenumb = document.getElementById("linenumb");

      // get the value of the text inside the h1 element
      const linenumbText = linenumb.textContent;

      // get the input element with id "lineNumber"
      const lineNumberInput = document.getElementById("lineNumber");

      // set the value of the input element to the text from the h1 element
      lineNumberInput.value = linenumbText;

      // Show the pop-up/modal
      const modal = document.getElementById('comment-modal');
      modal.style.display = 'block';

      // Set the subject of the form to the text of the clicked header cell
      const subject = header.innerText;
      const subjectField = document.getElementById('subject');
      subjectField.value = subject;

      // Populate the day of the week field with the current weekday
      const daysOfWeek = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];
      const today = new Date();
      const dayOfWeek = daysOfWeek[today.getDay()];
      const dayOfWeekField = document.getElementById('dayOfWeek');
      dayOfWeekField.value = dayOfWeek;

      
    });
  });

// Add a submit event listener to the comment form
const commentForm = document.getElementById('comment-form');
commentForm.addEventListener('submit', event => {
  event.preventDefault();

  // Get the form data
  const dayOfWeek = document.getElementById('dayOfWeek').value;
  const subject = document.getElementById('subject').value;
  const comment = document.getElementById('comment').value;
  const lineNumb = document.getElementById('lineNumber').value;

  const downtimeTypeRadioButtons = document.getElementsByName('downtimeType');
  let downtimeType;

  for (const radioButton of downtimeTypeRadioButtons) {
    if (radioButton.checked) {
      downtimeType = radioButton.value;
      break;
    }
  }

  // Create the data to send to the server
  const data = new URLSearchParams();
  data.append('lineNumber', lineNumb)
  data.append('dayOfWeek', dayOfWeek);
  data.append('subject', subject);
  data.append('comment', comment);
  data.append('downtimeType', downtimeType);  // Add downtime type to form data

  // Send the POST request to the current page
  fetch(window.location.href, {
    method: 'POST',
    body: data
  }).then(response => {
    if (response.ok) {
      // Success!
      console.log('Comment saved!');
    } else {
      // Error!
      console.log('Error saving comment');
    }
  }).catch(error => {
    console.log(error);
  });

  // Hide the pop-up/modal
  const modal = document.getElementById('comment-modal');
  modal.style.display = 'none';

  // Reset the form fields
  commentForm.reset();
});


  // Get the span element with class 'close'
  const span = document.querySelector('.close');
  
  // Add a click event listener to the span element to close the modal
  span.onclick = function() {
    const modal = document.getElementById('comment-modal');
    modal.style.display = "none";  
  }

  
  const expanderButton = document.querySelector('.expander-button');
  const expanderContent = document.querySelector('.expander-content');
  const triangleSymbol = document.querySelector('.expander-button .triangle-symbol');

  expanderButton.addEventListener('click', () => {
    if (expanderContent.style.display === 'none' || expanderContent.style.display === '') {
      expanderContent.style.display = 'block';
      triangleSymbol.innerHTML = '&#9660;';
    } else {
      expanderContent.style.display = 'none';
      triangleSymbol.innerHTML = '&#9654;';
    }
  });

