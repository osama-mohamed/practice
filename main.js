

var i = 0;
for (; i <= 10; i += 1) {
    if (i === 4) {
        break;
    }
    console.log(i);
}


var a = 0;
for (; a <= 10; a += 1) {
    if (a === 4) {
        continue;
    }
    console.log(a);
}


var x,y;

MainLoop:
for (x = 1; x <= 12; x += 1) {
    ChildLoop:
    for (y = 1; y <= 12; y += 1) {
        if (y === 6) {
            // break ChildLoop;
            // break MainLoop;
            // continue ChildLoop;
            // continue MainLoop;
        }
        console.log(x, y);
    }
    console.log('*********')
}
