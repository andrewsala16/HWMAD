function calc() {
  var day = new Date(document.getElementById("day").value);
  var dayofweek = Number(day.getDay());
  var daymonth = Number(day.getMonth());
  var daydate = Number(day.getDate());

  if (daydate == 14 && daymonth == 1){
    document.getElementById("result").innerHTML = "Presidents Day No SCHOOL";
  }
  if (daydate == 30 && daymonth == 6){
    document.getElementById("result").innerHTML = "Memorial Day No SCHOOL";
  }
  if (daydate == 17 && daymonth == 0){
    document.getElementById("result").innerHTML = "MLK Day No SCHOOL";
  }
  else{
    if (dayofweek == 6 || dayofweek == 5){
      document.getElementById("result").innerHTML = "The Weekend";
    }

    if (dayofweek == 0 || dayofweek == 4){
      document.getElementById("result").innerHTML = "A Day";
    }

    if (dayofweek == 1 || dayofweek == 3){
      document.getElementById("result").innerHTML = "B Day";
    }

    if (dayofweek == 2){
      document.getElementById("result").innerHTML = "Full Virtual";
    }
  }
}