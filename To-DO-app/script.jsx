function getTasks() {
    const tasks = localStorage.getItem('tasks');
    return tasks ? JSON.parse(tasks) : [];
}

function saveTasks(tasks) {
    localStorage.setItem('tasks', JSON.stringify(tasks));
}

function renderTasks() {
    const taskList = document.getElementById('taskList');
    taskList.innerHTML = '';
    const tasks = getTasks();
    tasks.forEach((task, index) => {
        const li = document.createElement('li');
        li.textContent = task;
        
        const delBtn = document.createElement('button');
        delBtn.textContent = 'Delete';
        delBtn.className = 'delete-btn';
        delBtn.onclick = () => deleteTask(index);

        li.appendChild(delBtn);
        taskList.appendChild(li);
    });
}

function addTask() {
    const input = document.getElementById('taskInput');
    const task = input.value.trim();
    if (task) {
        const tasks = getTasks();
        tasks.push(task);
        saveTasks(tasks);
        input.value = '';
        renderTasks();
    } else {
        alert('Please enter a task.');
    }
}

function deleteTask(index) {
    const tasks = getTasks();
    tasks.splice(index, 1);
    saveTasks(tasks);
    renderTasks();
}

// Show tasks when page loads
window.onload = renderTasks;