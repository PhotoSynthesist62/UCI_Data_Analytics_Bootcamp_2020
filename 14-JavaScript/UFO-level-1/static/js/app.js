const tableData = data;

// var button = d3.select("#button");
// var form = d3.select("#form");
const tbody= d3.select("tbody");
d3.selectAll("#filter-btn").on("click", runEnter);
// form.on("submit", runEnter);

function buildTable(data_arg) {
    tbody.html("");
    data_arg.forEach((dataRow) => {
        const row= tbody.append("tr");
        Object.values(dataRow).forEach((val) => {
            let cell = row.append("td");
                cell.text(val);
        });
    });
}

function runEnter() {
    // d3.event.preventDefault();
    const date = d3.select("#datetime").property("value")
    let filteredData= tableData;
    if(date){
        filteredData= filteredData.filter(row => row.datetime === date)
    }
    buildTable(filteredData)
}
buildTable(tableData)