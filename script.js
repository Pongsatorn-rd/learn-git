const form = document.getElementById('task-form');
const input = document.getElementById('task-input');
const taskList = document.getElementById('task-list');

form.addEventListener('submit', function (e) {
  e.preventDefault();
  const task = input.value.trim();
  if (task) {
    addTask(task);
    input.value = '';
  }
});

function addTask(taskText) {
  const li = document.createElement('li');
  li.innerHTML = `
    <span>${taskText}</span>
    <button onclick="removeTask(this)">Delete</button>
  `;
  taskList.appendChild(li);
}

function removeTask(button) {
  button.parentElement.remove();
}
