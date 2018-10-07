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
        fetchData();
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
        const item = $(this).parent();
        item.next("br").remove();
        item.fadeOut().remove();
        fetchData();
      }
    });
  });

  $("html").on("click", "li", function() {
    let item = $(this)
      .attr("data-value")
      .replace(/ /g, "-");
    $.ajax({
      type: "POST",
      url: "/done/" + item,
      success: data => {
        if (data.done === true) {
          $(this).attr("data-done", false);
        } else {
          $(this).attr("data-done", true);
        }
        fetchData();
      }
    });
  });
});

function fetchData() {
  $.ajax({
    type: "GET",
    url: "/all",
    success: data => {
      $("ul").empty();
      let doneTodos = 0;
      for (let i = 0; i < data.length; i++) {
        if (data[i].done === true) {
          doneTodos += 1;
          $("ul").append(
            '<li data-value="' +
              data[i].item +
              '" data-done="true">' +
              ($("ul li").length + 1) +
              " - " +
              data[i].item +
              '<button class="deleteItem">X</button></li><br>'
          );
        } else {
          $("ul").append(
            '<li data-value="' +
              data[i].item +
              '" data-done="false">' +
              ($("ul li").length + 1) +
              " - " +
              data[i].item +
              '<button class="deleteItem">X</button></li><br>'
          );
        }
      }
      $("form span").text(`done : ${doneTodos} - ${data.length}`);
    }
  });
}
