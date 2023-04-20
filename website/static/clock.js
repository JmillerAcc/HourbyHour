function updateTime() {
  var today = new Date();
  var month = today.getMonth() + 1;
  var date = today.getDate();
  var year = today.getFullYear().toString().slice(-2);
  var hour = today.getHours();
  var meridiem = hour >= 12 ? 'PM' : 'AM'; // determine AM or PM
  hour = hour % 12; // convert to 12 hour format
  hour = hour ? hour : 12; // handle midnight (0)
  var minute = today.getMinutes();
  var second = today.getSeconds();

  // Add leading zeros
  month = month < 10 ? '0' + month : month;
  date = date < 10 ? '0' + date : date;
  hour = hour < 10 ? '0' + hour : hour;
  minute = minute < 10 ? '0' + minute : minute;
  second = second < 10 ? '0' + second : second;

  var dateTime = month + '/' + date + '/' + year + ' ' + hour + ':' + minute + ':' + second + ' ' + meridiem;
  document.getElementById("datetime").innerHTML = dateTime;
  
  // Store the current time in localStorage
  localStorage.setItem("lastTime", dateTime);
}

// Retrieve the last time from localStorage and display it
var lastTime = localStorage.getItem("lastTime");
if (lastTime) {
  document.getElementById("datetime").innerHTML = lastTime;
}

setInterval(updateTime, 1000);








