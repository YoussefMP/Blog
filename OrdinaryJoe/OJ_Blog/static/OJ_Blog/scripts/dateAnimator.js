$(function() {
  var intervalID = setInterval(function(){
    document.getElementById('requestText').innerHTML += '.'
  }, 500)
  var animationTime = 5000;
  setTimeout(main(), 250);
  function main(){
    $('#hh1').animate({scrollTop:$("#hh1-main").offset().top}, animationTime, 'swing', function() {
  });
    setTimeout(function(){
      $('#hh2').animate({scrollTop:$("#hh2-main").offset().top}, animationTime, 'swing', function() {
  });
    }, 100);
    setTimeout(function(){
      $('#symbol').animate({scrollTop:$("#symbol-main").offset().top}, animationTime, 'swing', function() {
  });
    }, 200);
    setTimeout(function(){
      $('#mm1').animate({scrollTop:$("#mm1-main").offset().top}, animationTime, 'swing', function() {
  });
    }, 300);
    setTimeout(function(){
      $('#mm2').animate({scrollTop:$("#mm2-main").offset().top}, animationTime, 'swing', function() {
  });
    }, 400);
  }
});
