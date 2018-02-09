/**
 * Side Navigation
 */

/* Set the width of the side navigation */
function openNav() {
    document.getElementById("sidenav").style.width = "200px";
}

/* Set the width of the side navigation to 0 */
function closeNav() {
    document.getElementById("sidenav").style.width = "0";
}

/**
 * ToDo Tabs
 */
function openTodo(evt, todoDay) {
    // Declare variables
    var i, todo_links, todo_content;

    // Set display to none for all todo_content
    todo_content = document.getElementsByClassName("todo_content");
    for (i = 0; i < todo_content.length; i++) {
        todo_content[i].style.display = "none";
    }

    // Remove .active_link class from links
    todo_links = document.getElementsByClassName("todolinks");
    for (i = 0; i < todo_links.length; i++) {
        todo_links[i].classList.remove("active_link");
    }

    // Display content of the current day
    document.getElementById(todoDay).style.display = "block";
    evt.currentTarget.classList.add("active_link");
}