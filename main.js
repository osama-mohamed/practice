let clearSet = setInterval(function(){

  let datenews = new Date("oct 1, 2018 23:59:59").getTime(),
    nowDate = new Date().getTime(),
    resualt = datenews - nowDate;
    
  let days = Math.floor(resualt / (1000 * 60 * 60 * 24)),
    hours = Math.floor(resualt % (1000 * 60 * 60 * 24) / (1000 * 60 * 60)),
    minutes = Math.floor(resualt % (1000 * 60 * 60) / (1000 * 60)),
    seconds = Math.floor(resualt % (1000 * 60) / 1000);
  
  let countDown = document.querySelector(".countDown").innerHTML =
    days + " Days - "+ hours + " Hours - " + minutes + " Minutes - " + seconds + " Seconds"
  
  if(resualt < 0){
      clearInterval(clearSet);
      countDown.innerHTML = "End"
  }
  
}, 1000)