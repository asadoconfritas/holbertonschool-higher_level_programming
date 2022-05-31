const url = 'https://swapi-api.hbtn.io/api/films/?format=json';
$.get(url, function(data) {
  for (let i = 0; data.results[i]; i++) {
    $('UL#list_movies').append('<div>' + data.results[i].title + '</div>');
  }
});
