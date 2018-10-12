window.onload = loadData();
// document.getElementById("new-quote").addEventListener("click", loadData);
document.getElementById("new-quote").onclick = loadData;

function loadData() {
  document.getElementById("overlay").style.display = "block";
  // const myHeaders = new Headers();
  // myHeaders.append('pragma', 'no-cache');
  // myHeaders.append("cache-control", "no-cache");
  fetch(
    "https://quotesondesign.com/wp-json/posts?filter[orderby]=rand&filter[posts_per_page]=1",
    {
      mode: "cors",
      cache: "no-cache"
      // headers: myHeaders
    }
  )
    .then(res => res.json())
    .then(data => {
      const post = data.shift();
      document.title = "Quote | " + post.title;
      document.getElementById("quote-content").innerHTML = post.content;
      document.getElementById("quote-title-dash").innerHTML = "&#8212;";
      document.getElementById("quote-link").href = post.link;
      document.getElementById("quote-title").textContent = post.title;
      document.getElementById("quote-id").textContent = "#" + post.ID;
      document.getElementById("overlay").style.display = "none";
    });
}

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
