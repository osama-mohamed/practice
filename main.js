
// first method
if (window.location.hash) {
    if (window.location.hash.indexOf('osama') === 1) {
        window.location = 'https://www.fb.com/osama.mohamed.ms';
    }
} else {
    console.log('no hash is found here');
}


// second method
if (window.location.hash) {
    var hash = window.location.hash.substring(1);
    console.log(hash);
    if (hash === 'osama') {
        window.location = 'https://www.fb.com/osama.mohamed.ms';
    }
} else {
    console.log('no hash is found here too');
}
