

var i = 0;
while (i <= 10) {
    console.log(i);
    i += 1;
}

function generateYears(Start, End) {
    document.write('<select>');
        var year = Start;
        while (year <= End) {
            document.write("<option value=\"" + year + "\">" + year + "</option>");
            // document.write("<option value=" + year + ">" + year + "</option>");
            year += 1
        }
    document.write('</select>');
}

generateYears(1900, 2020);


function oneClick() {
    var startYear = document.getElementById('year-start').value;
    var endYear = document.getElementById('year-end').value;
    generateYears(parseInt(startYear), parseInt(endYear));
}
