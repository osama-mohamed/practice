

var i = 0;
while (i <= 10) {
    console.log(i);
    i += 1;
}

var n = 0;
do {
    console.log(n);
    n += 1;
} while (n <= 10);


function generateYears(Start, End) {
    document.write('<select>');
        var year = Start;
        do {
            document.write("<option value=\"" + year + "\">" + year + "</option>");
            // document.write("<option value=" + year + ">" + year + "</option>");
            year += 1
        } while (year <= End);
    document.write('</select>');
}

generateYears(1900, 2020);


function oneClick() {
    var startYear = document.getElementById('year-start').value;
    var endYear = document.getElementById('year-end').value;
    generateYears(parseInt(startYear), parseInt(endYear));
}
