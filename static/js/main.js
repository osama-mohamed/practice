$(function () {
    $('.navbar li a').on('click', function (e) {
        e.preventDefault();
        $('html, body').animate({
            scrollTop: $('#' + $(this).data('scroll')).offset().top
        }, 1000);
        window.console.log('#' + $(this).data('scroll'));
    });
});