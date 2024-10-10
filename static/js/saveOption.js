const defaultMethod = "average";
const methodSelect = document.querySelector("#method");

methodSelect.addEventListener("change", function() {
    localStorage.setItem("method", methodSelect.value);
});

methodSelect.value = localStorage.getItem("method") || defaultMethod;