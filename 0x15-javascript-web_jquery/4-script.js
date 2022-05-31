$('DIV#toggle_header').on('click', function(event) {
  let obj = $('header')
  if (obj.hasClass('red')) {
    obj.addClass('green');
    obj.removeClass('red');
  } else {
    obj.addClass('red');
    obj.removeClass('green');
  }
});
