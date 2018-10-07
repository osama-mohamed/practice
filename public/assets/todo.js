$(document).ready(() => {
  $("form").on("submit", () => {
    let item = $("form input");
    let todo = { item: item.val() };
    $.ajax({
      type: "POST",
      url: "/",
      data: todo,
      success: data => {
        $("ul").append(
          '<li data-value="' +
            data.item +
            '" data-done="false">' +
            ($("ul li").length + 1) +
            " - " +
            data.item +
            '<button class="deleteItem">X</button></li><br>'
        );
        item.val("").blur();
      }
    });
    return false;
  });

  $("html").on("click", ".deleteItem", function(event) {
    event.stopPropagation();
    let item = $(this)
      .parent()
      .attr("data-value")
      .replace(/ /g, "-");
    $.ajax({
      type: "DELETE",
      url: "/" + item,
      success: data => {
        const item = $(this).parent()
        item.next('br').remove();
        item.fadeOut().remove();
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
