const resultDisplay = document.getElementById("result");
const historyDisplay = document.getElementById("history");

function append(value) {
  if (resultDisplay.textContent === "0") resultDisplay.textContent = value;
  else resultDisplay.textContent += value;
}

function clearAll() {
  resultDisplay.textContent = "0";
  historyDisplay.textContent = "";
}

function toggleSign() {
  let v = resultDisplay.textContent;
  resultDisplay.textContent = v.startsWith("-") ? v.slice(1) : "-" + v;
}

function calculate() {
  try {
    let expression = resultDisplay.textContent.replace('%','/100');
    let result = eval(expression);

    historyDisplay.textContent = resultDisplay.textContent + " =";
    resultDisplay.textContent = result;

  } catch {
    alert("Invalid calculation!");
    clearAll();
  }
}

function toggleMode() {
  document.getElementById("basicPanel").classList.toggle("hidden");
  document.getElementById("sciPanel").classList.toggle("hidden");
}

function sci(type) {
  let v = parseFloat(resultDisplay.textContent);
  if (isNaN(v)) return alert("Invalid number!");

  let expression = "";
  let result = 0;

  switch(type){
    case "sqrt":
      if(v<0) return alert("Invalid");
      expression = `√(${v})`;
      result = Math.sqrt(v);
      break;

    case "square":
      expression = `(${v})²`;
      result = v * v;
      break;

    case "reciprocal":
      if(v===0) return alert("Divide by zero!");
      expression = `1/(${v})`;
      result = 1 / v;
      break;

    case "sin":
      expression = `sin(${v})`;
      result = Math.sin(v*Math.PI/180);
      break;

    case "cos":
      expression = `cos(${v})`;
      result = Math.cos(v*Math.PI/180);
      break;

    case "tan":
      expression = `tan(${v})`;
      result = Math.tan(v*Math.PI/180);
      break;

    case "log":
      expression = `log(${v})`;
      result = Math.log10(v);
      break;
  }

  historyDisplay.textContent = expression;
  resultDisplay.textContent = parseFloat(result.toFixed(6));
}

