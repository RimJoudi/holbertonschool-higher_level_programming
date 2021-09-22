const url = 'https://fourtonfish.com/hellosalut/?lang=fr';
const $ = window.$;
$.getJSON(url, function (data) {
  $('DIV#hello').text(data.hello);
});
