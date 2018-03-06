var season = prompt('what is your favourite season ?');

switch (season) {
    case 'winter':
        alert('winter is very cold!');
        break;
    case 'summer':
        alert('summer is very hot!');
        break;
    case 'spring':
    case 'autumn':
        alert('This season is amazing!');
        break;
    default:
        alert('You did not write a valid season name!');
        break;
}