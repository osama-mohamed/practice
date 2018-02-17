$(function () {
    // calculate body padding top depend on navbar height
    $('body').css('paddingTop', $('.navbar').innerHeight());

    // smooth scroll to element
    $('.navbar li a').on('click', function (e) {
        e.preventDefault();
        $('html, body').animate({
            scrollTop: $('#' + $(this).data('scroll')).offset().top + 1
        }, 1000);
        // window.console.log('#' + $(this).data('scroll'));
    });

    // add active class to navbar link and remove from siblings
    $('.navbar li a').click(function () {
        // $('.navbar a').removeClass('active');
        // $(this).addClass('active');
        $(this).addClass('active').parent().siblings().find('a').removeClass('active');
    });

    // sync navbar links with sections
    $(window).scroll(function () {
        $('.block').each(function () {
            if($(window).scrollTop() > $(this).offset().top ){
                var blockID = $(this).attr('id');
                $('.navbar a').removeClass('active');
                $('.navbar li a[data-scroll="' + blockID + '"]').addClass('active');
            }
        });
    });
});