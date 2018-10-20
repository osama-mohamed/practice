const timeUntil = "oct 1, 2019 23:59:59";

let clearSet = setInterval(() => {
  let datenews = new Date(timeUntil).getTime(),
    nowDate = new Date().getTime(),
    result = datenews - nowDate;

  let days = Math.floor(result / (1000 * 60 * 60 * 24)),
    hours = Math.floor((result % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60)),
    minutes = Math.floor((result % (1000 * 60 * 60)) / (1000 * 60)),
    seconds = Math.floor((result % (1000 * 60)) / 1000);

  const countDown = document.querySelector(".countDown");
  countDown.innerHTML = days + " Days - " + hours + " Hours - " + minutes + " Minutes - " + seconds + " Seconds";
    
    if (result <= 0) {
      clearInterval(clearSet);
      countDown.innerHTML = "End";
    }
}, 1000);

document.getElementById("time-until").innerHTML += timeUntil;
