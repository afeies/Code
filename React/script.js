// Grab DOM elements
const input = document.getElementById("textInput")
const button = document.getElementById("submitBtn")
const output = document.getElementById("output")

// Add click event
button.addEventListener("click", () => {
    // Read input value
    const text = input.value;

    // Manually update the DOM
    output.textContent = text;
});