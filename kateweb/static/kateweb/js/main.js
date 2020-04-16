$(window).on('load', function () {
    var $preloader = $('#page-preloader'),
        $spinner   = $preloader.find('.spinner');
    $spinner.fadeOut();
    $preloader.delay(350).fadeOut('slow');
});

$(document).ready(function () {

    $(".sidenav").sidenav();

    $('.slider').slider();
});

// Initializes PhotoSwipe.
var pswpInit = function (startsAtIndex) {

    if (!startsAtIndex) {
        startsAtIndex = 0;
    }

    var pswpElement = document.querySelectorAll('.pswp')[0];

    // commented the array bellow since the images array will be loaded from the server
    // in variable called djangoAlbumImages.

    // build items array
    //var items = [
    //    {
    //        src: 'https://placekitten.com/600/400',
    //        w: 600,
    //        h: 400
    //    },
    //    {
    //        src: 'https://placekitten.com/1200/900',
    //        w: 1200,
    //        h: 900
    //    }
    //];

    // find is images are loaded from the server.
    if (window.djangoAlbumImages && window.djangoAlbumImages.length > 0) {
        // define options (if needed)
        var options = {
            // optionName: 'option value'
            // for example:
            index: startsAtIndex // start at first slide
        };

        // Initializes and opens PhotoSwipe
        var gallery = new PhotoSwipe(pswpElement, PhotoSwipeUI_Default, window.djangoAlbumImages, options);
        gallery.init();
    }
}


// if ($(document.getElementById('home-html'))) {
  $(document).on("scroll", function(){

    if($(document).width() < 320)
      return false;
    if ($(document).scrollTop() > 30){
      $('#header_home').addClass('width_full');
      $("#container_home").removeClass('align-items-end');
      $('#container_home').addClass('align-items-start');
      $('#navbar').css('margin-bottom', '0px');
    }
    else {
      $('#header_home').removeClass('width_full');
      $('#container_home').removeClass('align-items-start');
      $("#container_home").addClass('align-items-end');
      $('#navbar').css('margin-bottom', '20px');
    }
  });



// // optional
// $('#blogCarousel').carousel({
// 			interval: 5000
// });
