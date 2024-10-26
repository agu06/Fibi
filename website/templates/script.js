window.addEventListener('wheel', function(event) {
    document.documentElement.scrollTop += event.deltaY;
    event.preventDefault();
});

function showAlert() {
    alert("You clicked the button!");
}