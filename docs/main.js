function initDots() {
    let colors = ['#fc4d4f', '#feb73a', '#3ee3a1', '#8f3de6', '#2c49fd', '#fb4fdd'];

    let windowHight = $(window).height()
    let windowWidth = $(window).width() -20
    // let docHight = $(document).height()
    let docHight = $('.hero').height()
    if (docHight < windowHight) {
        docHight = windowHight - 30;
    }
    for (let i = 0; i < 22; i++) {
        let x = randomNumber(5, 10);
        let el = $('<span class="dot"></span>');
        el.css({
            display: 'block',
            width: x,
            height: x,
            opacity: randomNumber(.2, .8, false),
            // transform: `translateY(${randomNumber(0, docHight)}px)`,
            transform: `translateY(${docHight}px)`,
            backgroundColor: colors[randomNumber(0, colors.length - 1)],
            left: randomNumber(0, windowWidth),
        });
        $('.dots').append(el);
    }
    $('.dot').each(function () {
        let oldTransform = $(this).css('transform');
        oldTransform = oldTransform.replace('matrix(1, 0, 0, 1, 0, ', '')
        oldTransform = parseInt(oldTransform.replace(')', ''))
        animateDot(this, oldTransform, randomNumber(.1, .5, false), docHight)
    })
}

function animateDot(el, oldTransform, speed, docHight) {
    let newTransform = oldTransform - speed
    let $el = $(el);
    if (newTransform < -20) {
        newTransform = docHight;
        $el.css('transform', `translateY(${newTransform}px)`)
        animateDot(el, newTransform, speed, docHight)
    } else {
        setTimeout(() => {
            $el.css('transform', `translateY(${newTransform}px)`)
            animateDot(el, newTransform, speed, docHight)
        }, 1)
    }
}

function randomNumber(min = 0, max = 100, whole = true) {
    if (whole) return Math.floor(Math.random() * max) + min
    return (Math.random() * (max - min) + min).toFixed(4)
}


initDots();