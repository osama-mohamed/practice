$(document).ready(() => {
  $("form").on("submit", () => {
    let item = $("form input");
    let todo = { item: item.val() };
    $.ajax({
      type: "POST",
      url: "/",
      data: todo,
      success: data => {
        location.reload();
      }
    });
    return false;
  });

  $(".deleteItem").on("click", function(event) {
    event.stopPropagation();
    let item = $(this)
      .parent()
      .attr("data-value")
      .replace(/ /g, "-");
    $.ajax({
      type: "DELETE",
      url: "/" + item,
      success: data => {
        location.reload();
      }
    });
  });

  $("li").on("click", function() {
    let item = $(this)
      .attr("data-value")
      .replace(/ /g, "-");
    $.ajax({
      type: "POST",
      url: "/done/" + item,
      success: data => {
        location.reload();
      }
    });
  });
});
