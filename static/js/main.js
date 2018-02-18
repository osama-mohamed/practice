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


    $(window).scroll(function () {
        // sync navbar links with sections
        $('.block').each(function () {
            if($(window).scrollTop() > $(this).offset().top ){
                var blockID = $(this).attr('id');
                $('.navbar a').removeClass('active');
                $('.navbar li a[data-scroll="' + blockID + '"]').addClass('active');
            }
        });

        // scroll to top button
        var scrollToTop = $('.scroll_to_top');
        if($(window).scrollTop() >= 1000 ){
            if(scrollToTop.is(':hidden')){
                scrollToTop.fadeIn(500);
            }
        } else {
            scrollToTop.fadeOut(500);
        }
    });

    // click on scroll to top button to go to top
    $('.scroll_to_top').on('click', function (event) {
        event.preventDefault();
        $('html, body').animate({
            scrollTop: 0
        }, 1000);
    });


    // show popup
    $('.show_popup').click(function () {
        $('.' + $(this).data('popup') ).fadeIn();
    });

    // hide popup
    // hide when click close button only
    $('.close_popup').click(function (e) {
        e.preventDefault();
        // $('.popup').fadeOut();
        $(this).parentsUntil('.popup').parent().fadeOut();
    });
    // hide when click on any place
    $('.popup').click(function () {
        $('.popup').fadeOut();
    });
    // do not hide when clicked on popup body
    $('.popup .inner_popup').click(function (event) {
        event.stopPropagation();
    });
    // hide with esc key in keyboard
    $(document).keydown(function (e) {
        // 27 is the keycode in javascript for esc key
        if(e.keyCode == 27){
            $('.popup').fadeOut();
        }
    });

    // button effects if there are no span
    // $('.buttons_effects button').each(function () {
    //     $(this).prepend('<spana></spana>');
    // });

    // buttons effects from left
    $('.from_left, .border_left').hover(function () {
        $(this).find('span').eq(0).animate({
            width: '100%'
        }, 200);
    }, function () {
        $(this).find('span').eq(0).animate({
            width: 0
        }, 200);
    });

    // buttons effects from top
    $('.from_top, .border_top').hover(function () {
        $(this).find('span').eq(0).animate({
            height: '100%'
        }, 200);
    }, function () {
        $(this).find('span').eq(0).animate({
            height: 0
        }, 200);
    });

    // buttons effects from left borders bottom
    // $('.border_left').hover(function () {
    //     $(this).find('span').eq(0).animate({
    //         width: '100%'
    //     }, 200);
    // }, function () {
    //     $(this).find('span').eq(0).animate({
    //         width: 0
    //     }, 200);
    // });
});