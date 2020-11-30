function calc() {

  var day = new Date(document.getElementById("day").value);
  var firstDay =  new Date("09/10/2020");
  var numberoDays = parseInt((day.getTime()-firstDay.getTime())/86400000);

  var mlk = new Date("1/18/2021");
  var president = new Date("2/15/2021");
  var memorial = new Date("5/31/2021");
  var lastDay = new Date("6/22/2021");

  var datemonth = Number(day.getMonth())+", "+ Number(day.getDate());
  var holidays = ["1, 14", "4, 30", "0, 17", "5, 21"]


  
  if (mlk.getTime()>day.getTime()){
    if ((numberoDays%2) == 0){
      document.getElementById("result").innerHTML = "A Day";
    }
    else{
      document.getElementById("result").innerHTML = "B Day";
    }
  }
  if (president.getTime()>day.getTime() && mlk.getTime()<day.getTime()){
    if ((numberoDays%2) == 1){
      document.getElementById("result").innerHTML = "A Day";
    }
    else{
      document.getElementById("result").innerHTML = "B Day";
    }
  }
  if (president.getTime()<day.getTime() && memorial.getTime()>day.getTime()){
    if ((numberoDays%2) == 0){
      document.getElementById("result").innerHTML = "A Day";
    }
    else{
      document.getElementById("result").innerHTML = "B Day";
    }
  }
  if(memorial.getTime()<day.getTime()){
    if ((numberoDays%2) == 0){
      document.getElementById("result").innerHTML = "A Day";
    }
    else{
      document.getElementById("result").innerHTML = "B Day";
    }
  }


  if(lastDay.getTime()<day.getTime()){
    document.getElementById("result").innerHTML = "Summer Vacay";
  }
  if(datemonth == holidays[0]){
    document.getElementById("result").innerHTML = "Presidents Day No SCHOOL";
  }
  if(datemonth == holidays[1]){
    document.getElementById("result").innerHTML = "Memorial Day No SCHOOL";
  }
  if(datemonth == holidays[2]){
    document.getElementById("result").innerHTML = "MLK Day No SCHOOL";
  }
  if(datemonth == holidays[3]){
    document.getElementById("result").innerHTML = "Last Day of School";
  }

}