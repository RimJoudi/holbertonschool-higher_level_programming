const $ = window.$;
$('#toggle_header').click(function () {
  if ($('HEADER').hasClass('green')) {
    $('HEADER').addClass('red').removeClass('green');
  } else {
    $('HEADER').addClass('green').removeClass('red');
  }
});
