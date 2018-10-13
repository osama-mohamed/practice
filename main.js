window.onload = loadData();
// document.getElementById("new-quote").addEventListener("click", loadData);
document.getElementById("new-quote").onclick = loadData;

function fadeOut(el) {
  el.style.opacity = 1;

  (function fade() {
    if ((el.style.opacity -= 0.1) <= 0) {
      el.style.display = "none";
    } else {
      requestAnimationFrame(fade);
    }
  })();
}

function fadeIn(el, display) {
  el.style.opacity = 0;
  el.style.display = display || "block";

  (function fade() {
    var val = parseFloat(el.style.opacity);
    if (!((val += 0.1) > 1)) {
      el.style.opacity = val;
      requestAnimationFrame(fade);
    }
  })();
}

// function loadData() {
//   fadeIn(document.getElementById("overlay"));
//   // document.getElementById("overlay").style.display = "block";
//   // const myHeaders = new Headers();
//   // myHeaders.append('pragma', 'no-cache');
//   // myHeaders.append("cache-control", "no-cache");
//   fetch(
//     "https://quotesondesign.com/wp-json/posts?filter[orderby]=rand&filter[posts_per_page]=1",
//     {
//       mode: "cors",
//       cache: "no-cache"
//       // headers: myHeaders
//     }
//   )
//     .then(res => res.json())
//     .then(data => {
//       const post = data.shift();
//       document.title = "Quote | " + post.title;
//       document.getElementById("quote-content").innerHTML = post.content;
//       document.getElementById("quote-title-dash").innerHTML = "&#8212;";
//       document.getElementById("quote-link").href = post.link;
//       document.getElementById("quote-title").textContent = post.title;
//       document.getElementById("quote-id").textContent = "#" + post.ID;
//       // document.getElementById("overlay").style.display = "none";
//       fadeOut(document.getElementById("overlay"));
//     });
// }

// function loadData() {
//   document.getElementById("overlay").style.display = "block";
//   const xhttp = new XMLHttpRequest();
//   xhttp.onreadystatechange = function() {
//     if (this.readyState == 4 && this.status == 200) {
//       const post = JSON.parse(this.responseText).shift();
//       document.title = "Quote | " + post.title;
//       document.getElementById("quote-content").innerHTML = post.content;
//       document.getElementById("quote-title-dash").innerHTML = "&#8212;";
//       document.getElementById("quote-link").href = post.link;
//       document.getElementById("quote-title").textContent = post.title;
//       document.getElementById("quote-id").textContent = "#" + post.ID;
//       document.getElementById("overlay").style.display = "none";
//     }
//   };
//   xhttp.open(
//     "GET",
//     "https://quotesondesign.com/wp-json/posts?filter[orderby]=rand&filter[posts_per_page]=1",
//     true
//   );
//   xhttp.send();
// }

function loadData() {
  document.getElementById("overlay").style.display = "block";
  axios({
    method: "get",
    url:
      "https://quotesondesign.com/wp-json/posts?filter[orderby]=rand&filter[posts_per_page]=1",
    headers: { "cache-control": "no-cache" }
  })
    .then(response => {
      const post = response.data.shift();
      document.title = "Quote | " + post.title;
      document.getElementById("quote-content").innerHTML = post.content;
      document.getElementById("quote-title-dash").innerHTML = "&#8212;";
      document.getElementById("quote-link").href = post.link;
      document.getElementById("quote-title").textContent = post.title;
      document.getElementById("quote-id").textContent = "#" + post.ID;
      fadeOut(document.getElementById("overlay"));
    })
    .catch(error => {
      console.log(error);
    })
    .then(() => {});
}
