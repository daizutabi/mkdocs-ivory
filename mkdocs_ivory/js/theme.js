function ready() {
  $('.nav .section').each(function() {
    $(this).click(function(e) {
      $(this).toggleClass("hide");
      $(this).parent().children(".subnav").toggleClass("hide");
    });
  });

  $('.hamburger').click(function(e) {
    $('html').toggleClass("show");
    $('aside').toggleClass("show");
    $('.home-top .site-name').toggleClass("hide");
  });
}

$(ready);
