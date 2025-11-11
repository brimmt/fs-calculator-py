const num1Input = document.getElementById("num1");
const num2Input = document.getElementById("num2");
const operationSelect = document.getElementById("operation");
const resultDisplay = document.getElementById("result");
const calculateBtn = document.getElementById("calculateBtn");


calculateBtn.addEventListener("click", async () => {
    const num1 = parseFloat(num1Input.value); // THis changes the string input or number input into a float
    const num2 = parseFloat(num2Input.value);
    const operation = operationSelect.value; //not sure exactly what this does, does it take the selected choice as a value?



const url = `http://127.0.0.1:8000/calculate?num1=${num1}&num2=${num2}&operation=${encodeURIComponent(operation)}`;  // this actually calls the api in main.py

try {
    const response = await fetch(url);  // this tries to pull from the url in the api call
    const data = await response.json(); // this changes the response to json?

    if (data.result !== undefined) {
        resultDisplay.textContent = `Result: ${data.result}`; // this line is pulling the result and returning is as the data.result so its in json?
    } else {
        resultDisplay.textContent = data.error;
    }
} catch (err) {
    resultDisplay.textContent = "Error connecting to server."  //Why don't i use result instead of resultDisplay?
}

});

