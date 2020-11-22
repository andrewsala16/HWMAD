function round(value, decimals) {
  return Number(Math.round(value + 'e' + decimals) + 'e-' + decimals);
}

function bmi() {
  var feet = Number(document.getElementById("feet").value) * 12;
  var inch = Number(document.getElementById("inch").value);
  var weight = Number(document.getElementById("weight").value);
  var res = (703 * weight) / (((feet) + inch) ** 2);

  if (isNaN(res)) {
    document.getElementById("result").innerHTML = "No input found"
  }

  if (res < 18.5) {
    document.getElementById("result").style.color = "orange"
    document.getElementById("result").innerHTML = "BMI: " + round(res, 1) + " - You are underweight"
  }

  if (res > 18.5 && res <= 24.9) {
    document.getElementById("result").style.color = "green"
    document.getElementById("result").innerHTML = "BMI: " + round(res, 1) + " - You are normal"
  }

  if (res > 25) {
    document.getElementById("result").style.color = "orange"
    document.getElementById("result").innerHTML = "BMI: " + round(res, 1) + " - You are overweight"
  }

}