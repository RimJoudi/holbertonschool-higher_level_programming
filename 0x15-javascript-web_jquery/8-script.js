const url = 'https://swapi-api.hbtn.io/api/films/?format=json';
const $ = window.$;

$.get(url, function (movie) {
  for (let i = 0; i < movie.results.length; i++) {
    $('ul#list_movies').append(`<li>${movie.results[i].title}</li>`);
  }
});
