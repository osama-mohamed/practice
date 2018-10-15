$(document).ready(function() {
  $('.delete-recipe').on('click', function() {
    const id = $(this).data('id');
    const url = '/delete/' + id;
    if(confirm('Delete recipe ?')) {
      $.ajax({
        url: url,
        type: 'DELETE',
        success: function(result) {
          console.log(result);
          window.location.href = '/';
        },
        error: function(err) {
          console.log(err);
        }
      });
    }
  });

  $('.edit-recipe').on('click', function() {
    $('#edit-form-id').val( $(this).data('id') );
    $('#edit-form-name').val( $(this).data('name') );
    $('#edit-form-ingredients').val( $(this).data('ingredients') );
    $('#edit-form-directions').val( $(this).data('directions') );
  });
});