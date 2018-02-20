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
    
    // bounce button
    $('.bounce').on('click', function () {
        $(this).animate({
            marginTop: '-=20px'
        }, 500).animate({
            marginTop: '+=20px'
        }, 500);
    });


    // animated progress bar
    $('.animated_progress_bar span').each(function () {
        $(this).animate({
            width: $(this).attr('data-progress') + '%'
        }, 1000, function () {
            $(this).text($(this).attr('data-progress') + '%');
        });
    });

    // fixed menu
    $('.fixed_menu').css('left', - $('.fixed_menu').innerWidth());
    $('body').on('click', '.fixed_menu .fa-cog', function () {
        // console.log($(this).parent().width());
        $(this).parent('.fixed_menu').toggleClass('is_visible');
        if($(this).parent('.fixed_menu').hasClass('is_visible')){
            $(this).parent('.fixed_menu').animate({
                left: 0
            }, 500);
            // if i want to push the body
            $('body').animate({
                paddingLeft: $('.fixed_menu').innerWidth()
            }, 500);
        } else {
            $(this).parent('.fixed_menu').animate({
                left: - $('.fixed_menu').innerWidth()
            }, 500);
            // if i want to push the body
            $('body').animate({
                paddingLeft: 0
            }, 500);
        }
    });

    // change colors
    $('.change_colors li').on('click', function(){
        $('body').attr('data_default_color', $(this).data('color'));
    });

    // thumbnails gallery
    var NumberOfThumbnails = $('.thumbnails').children().length,
        MarginBetweenThumbnails = '.5',
        TotalMarginBetweenThumbnails = (NumberOfThumbnails - 1) * MarginBetweenThumbnails,
        ThumbnailWidth = (100 - TotalMarginBetweenThumbnails) / NumberOfThumbnails;

    $('.thumbnails img').css({
        'width': ThumbnailWidth + '%',
        'margin-right': MarginBetweenThumbnails + '%'
    });
    $('.thumbnails img:last-child').css({
        'margin-right': 0
    });
    $('.gallery .thumbnails img').on('click', function () {
        $(this).addClass('selected').siblings().removeClass('selected');
        $('.master-img img').hide().attr('src', $(this).attr('src')).fadeIn(500);
        // console.log($(this).attr('src'));
        // console.log($(this).parent('.thumbnails').prev('.master-img').find('img').attr('src'));
    });
    $('.master-img .fa-chevron-left').on('click', function () {
        if($('.thumbnails .selected').is(':first-child')){
            $('.thumbnails img:last').click();
            // $('.thumbnails img').eq(-1).click();
            // $('.thumbnails img').eq(4).click();
        } else {
            $('.thumbnails .selected').prev().click();
        }
    });
    $('.master-img .fa-chevron-right').on('click', function () {
        if($('.thumbnails .selected').is(':last-child')){
            $('.thumbnails img').eq(0).click();
        } else {
            $('.thumbnails .selected').next().click();
        }
    });

    // toggle product description
    $('.products .product i, .items .item i').on('click', function () {
        $(this).toggleClass('fa-plus fa-minus').next('.description').slideToggle();
    });

    // toggle grid/list view items
    $('.view_options i').on('click', function () {
        $(this).addClass('active').siblings().removeClass('active');
        $('.items').removeClass('list_view grid_view').addClass( $(this).data('class') );
        console.log($(this).data('class'));
    });

    // error message
    $('.error_message').each(function () {
        $(this).animate({
            right: 0
        }, 1000, function () {
            $(this).delay(3000).fadeOut();
        });
    });

    // our form

    // hide placeholder on focus and restore on blur
    var placeAttr = '';
    $('[placeholder]').focus(function () {
        placeAttr = $(this).attr('placeholder');
        $(this).attr('placeholder', '');
    }).blur(function () {
        if ($('.auto_direction').val().charCodeAt(0) < 200 ){ // which means that the language is English
            $('.auto_direction').css('direction', 'ltr');
        } else {
            $('.auto_direction').css('direction', 'rtl');
            $('.auto_direction').attr('placeholder', 'نتلاتلاتل');
        }
        $(this).attr('placeholder', placeAttr);
    });

    // show message when field is empty
    $('[required]').on('blur', function () {
        if($(this).val() == ''){
            $(this).next('.the_message').fadeIn().delay(2000).fadeOut();
        }
    });

    // add asterisk to all required fields
    $('<span class="asterisk">*</span>').insertBefore(':input[required]');
    // customize the asterisk
    $('.asterisk').parent('div').css('position', 'relative');
    $('.asterisk').each(function () {
        $(this).css({
            'position': 'absolute',
            'top': 13,
            'left': $(this).parent('div').find('input[required]').innerWidth() - 20,
            'color': '#d63031',
            'font-weight': 'bold'
        });
    });

    // customize file input field
    $('.our_form input[type="file"]').wrap('<div class="custom_file"></div>');
    $('.our_form input[type="file"]').change(function () {
        $(this).prev('span').text( $(this).val().slice(12) );
    });
    $('.custom_file').prepend('<span>Upload Your File</span>');
    $('.custom_file').append('<i class="fa fa-upload fa-lg skin_color"></i>');
    $('.our_form .custom_file').css({
        'height': $('.our_form input[type="text"]').innerHeight()
        // 'height': $('.our_form').find('input[type="text"]').innerHeight()
    });

    // detect unicode for keyboard keys
    $('.detect_unicode').on('keyup', function (event) {
        var keyboardKey = event.keyCode || event.which;
        $('.unicode').html('The Unicode for the key you pressed is : ' + keyboardKey);
    });

    // change input direction depend on language
    $('.auto_direction').on('keyup', function () {
        if ($(this).val().charCodeAt(0) < 200 ){ // which means that the language is English
            $(this).css('direction', 'ltr');
        } else {
            $(this).css('direction', 'rtl');
        }
    });

    // convert input value to tag
    $('.add_tag').on('keyup', function (event) {
        var keyboardKey = event.keyCode || event.which;
        if(keyboardKey === 188){ // when comma pressed
            var inputValue = $(this).val().slice(0, -1);
            $('.tags').append('<span class="tag_span"><i class="fa fa-times"></i>' + inputValue + '</span>');
            $(this).val('');
        }
    });

    // remove tag on click
    $('.tags').on('click', '.tag_span i', function () {
        $(this).parent('.tag_span').fadeOut(800);
    });
    
    // trimmed text
    // $('.trimmed_text p').each(function () {
    //     if($(this).text().length > 100 ) {
    //         var trimmedText = $(this).text().substr(0, 100);
    //         $(this).text(trimmedText + ' ...');
    //     }
    // });
    function trimText(selector, maxLength) {
        $(selector).each(function () {
            if($(this).text().length > maxLength ) {
                var trimmedText = $(this).text().substr(0, maxLength);
                $(this).text(trimmedText + ' ...');
            }
        });
    }
    trimText('.trimmed_text .p_one', 100);
    trimText('.trimmed_text .p_two', 200);
});