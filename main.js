$(document).on("ready", () => {
  loadData();
});

$("html").on("click", "button", () => {
  loadData();
});

function loadData() {
  $("#overlay").fadeIn();
  $.ajax({
    url:
      "https://quotesondesign.com/wp-json/posts?filter[orderby]=rand&filter[posts_per_page]=1",
    success: data => {
      const post = data.shift();
      document.title = "Quote | " + post.title;
      $("#quote-title").text(post.title);
      $("#quote-content").html(post.content);
      $("#quote-title-dash").html("&#8212;");
      $("#quote-id").text("#" + post.ID);
      $("#quote-link").attr("href", post.link);
      $("#overlay").fadeOut();
    },
    cache: false
  });
}
