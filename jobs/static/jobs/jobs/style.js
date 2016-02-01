$(window).scroll(function() {

    if ($(this).scrollTop()>20)
     {
        $('.menu').fadeOut();
     }
    else
     {
      $('.menu').fadeIn();
     }
 });