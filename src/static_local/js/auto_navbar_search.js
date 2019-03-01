$(document).ready(function() {
  let typingTimer;
  const doneInterval = 500;
  const searchInput = $("#navbar-search-form input[type=text]");
  let searchQuery;
  searchInput.keyup(function() {
    searchQuery = $(this).val();
    clearTimeout(typingTimer);
    typingTimer = setTimeout(doneSearchTyping, doneInterval);
  });
  searchInput.keydown(function() {
    clearTimeout(typingTimer);
  });
  function doneSearchTyping() {
    if (searchQuery) {
      const url = `/tweet/search/?q=${searchQuery}`;
      document.location.href = url;
    }
  }
});
