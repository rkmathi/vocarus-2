// Generated by CoffeeScript 1.3.3

$(function() {
  var StartDate, day_str, diff, index_today;
  StartDate = new Date(2012, 9, 3);
  diff = parseInt((new Date().getTime() / 1000 - StartDate.getTime() / 1000) / (60 * 60 * 24));
  index_today = diff % 3;
  day_str = ['miku', 'gumi', 'luka'];
  $('.miku').append('<div class="' + day_str[index_today] + '_image"><img src="images/' + day_str[index_today] + '.png" alt="ルカ"></div>');
});
