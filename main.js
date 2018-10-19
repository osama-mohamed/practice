document.getElementById("myForm").addEventListener("submit", saveBookmark);
document.getElementById("deleteAll").addEventListener("click", deleteAll);

function saveBookmark(e) {
  e.preventDefault();
  const siteName = document.getElementById("siteName").value;
  const siteUrl = document.getElementById("siteUrl").value;
  if (!validateForm(siteName, siteUrl)) {
    return false;
  }
  const bookmark = {
    name: siteName,
    url: siteUrl,
    click: 0
  };
  if (localStorage.getItem("bookmarks") == null) {
    let bookmarks = [];
    bookmarks.push(bookmark);
    localStorage.setItem("bookmarks", JSON.stringify(bookmarks));
  } else {
    let bookmarks = JSON.parse(localStorage.getItem("bookmarks"));
    bookmarks.push(bookmark);
    localStorage.setItem("bookmarks", JSON.stringify(bookmarks));
  }
  document.getElementById("myForm").reset();
  getBookmarks();
}

function getBookmarks() {
  let bookmarks = JSON.parse(localStorage.getItem("bookmarks"));
  let bookmarksHTML = document.getElementById("bookmarks");
  bookmarksHTML.innerHTML = "";
  if(bookmarks) {
    bookmarks.forEach(bookmark => {
      bookmarksHTML.innerHTML += `<div class="well">
                                    <h3>
                                      ${bookmark.name}
                                      - ${bookmark.click} clicks
                                      <a class="btn btn-default" href="${bookmark.url}" target="_blank" onclick="numberOfClicks('${bookmark.url},${bookmark.name}')">View</a>
                                      <a class="btn btn-danger" href="#" onclick="deleteBookmark('${bookmark.url},${bookmark.name}')">Delete</a>
                                    </h3>
                                  </div>`;
    });
  }
}

function deleteBookmark(url) {
  let bookmarks = JSON.parse(localStorage.getItem("bookmarks"));
  bookmarks.forEach((bookmark, index) => {
    if (bookmark.url == url.split(',')[0] && bookmark.name == url.split(',')[1]) {
      bookmarks.splice(index, 1);
    }
  });
  localStorage.setItem("bookmarks", JSON.stringify(bookmarks));
  getBookmarks();
}

function validateForm(siteName, siteUrl) {
  if (!siteName || !siteUrl) {
    alert("Please fill in the form correctly!");
    return false;
  }
  const regex = new RegExp(/[-a-zA-Z0-9@:%_\+.~#?&//=]{2,256}\.[a-z]{2,4}\b(\/[-a-zA-Z0-9@:%_\+.~#?&//=]*)?/gi);
  if (siteUrl.match(regex)) {
    return true;
  } else {
    alert("Pleas use a valid URL!");
    return false;
  }
}

function deleteAll() {
  localStorage.removeItem("bookmarks");
  getBookmarks();
}

function numberOfClicks(url){
  let bookmarks = JSON.parse(localStorage.getItem("bookmarks"));
  bookmarks.forEach((bookmark, index) => {
    if (bookmark.url == url.split(',')[0] && bookmark.name == url.split(',')[1]) {
      bookmark.click += 1;
    }
  });
  localStorage.setItem("bookmarks", JSON.stringify(bookmarks));
  getBookmarks();
}