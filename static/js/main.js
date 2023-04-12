function tableSearch() {
    let input, filter, table, tr, td, th, i, j, textValue;
    input = document.getElementById('search_id');
    filter = input.value.toUpperCase();
    table = document.getElementById('datatable')
    tr = table.getElementsByTagName('tr')
    th = table.getElementsByTagName("th");
    for (i = 1; i < tr.length; i++) {
        tr[i].style.display = "none";
        for (j = 0; j < th.length; j++) {
            td = tr[i].getElementsByTagName("td")[j];
            if (td) {
                if (td.innerHTML.toUpperCase().indexOf(filter) > -1) {
                    tr[i].style.display = "";
                    break;
                }
            }
        }
    }
}


let rows = document.getElementById("datatable").getElementsByTagName("tbody")
    [0].getElementsByTagName("tr");

// loops through each row
let cells;
for (let i = 0; i < rows.length; i++) {
    cells = rows[i].getElementsByTagName('td');
    console.log(cells[11].innerHTML)
    if (cells[11].innerHTML === 'Waiting')
        rows[i].className = "waiting-warning";
    // if (cells[11].innerHTML === 'Given' || cells[11].innerHTML === '')
    //     rows[i].className = '';
}

function filterTable() {
    // Variables
    let dropdown, table, rows, cells, country, filter;
    dropdown = document.getElementById("status_id");
    table = document.getElementById("datatable");
    rows = table.getElementsByTagName("tr");
    filter = dropdown.value;

    // Loops through rows and hides those with countries that don't match the filter
    for (let row of rows) { // `for...of` loops through the NodeList
        cells = row.getElementsByTagName("td");
        country = cells[11] || null; // gets the 12 nd `td` or nothing
        // if the filter is set to 'All', or this is the header row, or 2nd `td` text matches filter
        // console.log(country)
        if (country !== null) {
            console.log(filter)
            if (filter === 0 || filter === "0") {
                if (country.innerHTML === "Waiting") {
                    row.style.display = ""; // shows this row
                } else {
                    row.style.display = "none"; // hides this row
                }
            }
            if (filter === 1 || filter === "1") {
                if (country.innerHTML === "Given") {
                    row.style.display = ""; // shows this row
                } else {
                    row.style.display = "none"; // hides this row
                }
            }
            if (filter === "") {
                row.style.display = "";
            }
        }
    }
}

$('#id_login').one('submit', function() {
    $(this).find('input[type="submit"]').attr('disabled','disabled');
});