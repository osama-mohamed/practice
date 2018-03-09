
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