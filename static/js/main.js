$(function () {
    // calculate body padding top depend on navbar height
    $('body').css('paddingTop', $('.navbar').innerHeight() + 20 );

    // smooth scroll to element
    $('.navbar li a').on('click', function (e) {
        e.preventDefault();
        $('html, body').animate({
            scrollTop: $('#' + $(this).data('scroll')).offset().top
        }, 1000);
        // window.console.log('#' + $(this).data('scroll'));
    });
});