const dropBtn = document.querySelector('.dropbtn');
const dropdown = document.querySelector('.dropdown');
const dropdownContent = document.querySelector('.dropdown-content');

dropdown.addEventListener('mouseleave', () => {
  dropBtn.classList.remove('hovered');
  dropBtn.innerHTML = 'Line Navigation'
});

dropdown.addEventListener('mouseover', () => {
  dropBtn.classList.add('hovered');
  dropBtn.innerHTML = 'Line Navigation:'
});