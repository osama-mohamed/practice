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
        url: "/articles/delete/" + id,
        success: function() {
          alert("Deleting Article " + articleTitle);
          window.location.href = "/";
        },
        error: function(err) {
          console.log(err);
        }
      });
    }
  });
  
  $(".delete-account").on("click", function(e) {
    const confirmation = confirm(
      "Are you sure that you want to delete your account and your articles ?"
    );
    if (confirmation) {
      $.ajax({
        type: "POST",
        url: "/users/delete-account",
        success: function() {
          alert("Deleting Account");
          window.location.href = "/";
        },
        error: function(err) {
          console.log(err);
        }
      });
    }
  });
  
  $(".delete-articles").on("click", function(e) {
    const confirmation = confirm(
      "Are you sure that you want to delete your all of your articles ?"
    );
    if (confirmation) {
      $.ajax({
        type: "POST",
        url: "/articles/delete-articles",
        success: function() {
          alert("Deleting Articles");
          window.location.href = "/";
        },
        error: function(err) {
          console.log(err);
        }
      });
    }
  });
});
