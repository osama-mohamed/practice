const auth = 'apikey=dc8c056';
$(document).ready(() => {
  $("#searchForm").on("submit", e => {
    e.preventDefault();
    const searchText = $('#searchText').val();
    getMovies(searchText);
  });
});

function getMovies(searchText) {
  axios.get(`https://www.omdbapi.com/?${auth}&s=${searchText}`)
  .then((response) => {
    if(response.data.Error) {
      let output = '';
      output += `
          <div class="col-md-3">
            <div class="well text-center">
              <h5>${response.data.Error}</h5>
            </div>
          </div>
        `;
        $('#movies').html(output);
    } else {
      const movies = response.data.Search;
      let output = '';
      $.each(movies, (index, movie) => {
        output += `
          <div class="col-md-3">
            <div class="well text-center">
            <img src="${movie.Poster}">
              <h5>${movie.Title}</h5>
              <a onclick="movieSelected('${movie.imdbID}')" href="#" class="btn btn-primary">Movie Detail</a>
            </div>
          </div>
        `;
      });
      $('#movies').html(output);
    }
  })
  .catch(error => {
    console.log(error);
  });
}

function movieSelected(id) {
  sessionStorage.setItem('movieId', id);
  window.location = "movie.html";
  return false;
}

function getMovie() {
  let movieId = sessionStorage.getItem('movieId');
  axios.get(`https://www.omdbapi.com/?${auth}&i=${movieId}&plot=full`)
  .then((response) => {
    const movie = response.data;
    let output = `
      <div class="row">
        <div class="col-md-4">
          <img src="${movie.Poster}" class="thumbnail">
        </div>

        <div class="col-md-8">
          <h2>${movie.Type}: ${movie.Title}</h2>
          <ul class="list-group">
            <li class="list-group-item"><strong>Genre:</strong> ${movie.Genre}</li>
            <li class="list-group-item"><strong>Country:</strong> ${movie.Country}, <strong>Language:</strong> ${movie.Language}, <strong>Runtime:</strong> ${movie.Runtime}</li>
            <li class="list-group-item"><strong>Released:</strong> ${movie.Released}</li>
            <li class="list-group-item"><strong>Awards:</strong> ${movie.Awards}</li>
            <li class="list-group-item"><strong>Rated:</strong> ${movie.Rated}</li>
            <li class="list-group-item"><strong>IMDB Rated:</strong> ${movie.imdbRating}</li>
            <li class="list-group-item"><strong>IMDB Votes:</strong> ${movie.imdbVotes}</li>
            <li class="list-group-item"><strong>Director:</strong> ${movie.Director}</li>
            <li class="list-group-item"><strong>Writer:</strong> ${movie.Writer}</li>
            <li class="list-group-item"><strong>Actors:</strong> ${movie.Actors}</li>
          </ul>
        </div>
      </div>

      <div class="row">
        <div class="well">
          <h3>Plot</h3>
          ${movie.Plot}
          <hr>
          <a href="https://imdb.com/title/${movie.imdbID}" target="_blank" class="btn btn-primary">View IMDB</a>
          <a href="index.html" class="btn btn-default">Go Back To Search</a>
        </div>
      </div>
      `;
    $('#movie').html(output);
  })
  .catch(error => {
    console.log(error);
  });
}



