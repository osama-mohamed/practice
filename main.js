

function generateYears(Start, End) {
    document.write('<select>');
        var year;
        for (year = Start; year <= End; year += 1) {
            document.write("<option value=\"" + year + "\">" + year + "</option>");
            // document.write("<option value=" + year + ">" + year + "</option>");
        }
    document.write('</select>');
}

generateYears(1900, 2020);


function oneClick() {
    var startYear = document.getElementById('year-start').value;
    var endYear = document.getElementById('year-end').value;
    generateYears(parseInt(startYear), parseInt(endYear));
}
