$(document).ready(function() {
  $(".delete-article").on("click", function(e) {
    $target = $(e.target);
    // console.log($target[0].dataset.id);
    // console.log($target.attr('data-id'));
    const id = $target.attr("data-id");
    const articleTitle = $target.attr("data-title");
    const confirmation = confirm(
      "Are you sure that you want to delete article: " + articleTitle + " ?"
    );
    if (confirmation) {
      $.ajax({
        type: "DELETE",
        url: "/article/delete/" + id,
        success: function() {
          alert("Deleting Article" + articleTitle);
          window.location.href = "/";
        },
        error: function(err) {
          console.log(err);
        }
      });
    }
  });
});
