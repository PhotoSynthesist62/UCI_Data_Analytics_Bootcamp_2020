// You need to create a scatter plot between two of the data variables such as Healthcare vs. Poverty or Smokers vs. Age.

// Create the grid in which to place the chart
var svgWidth = 800;
var svgHeight = 500;

var margin = {
    top: 30,
    right: 0,
    bottom: 60,
    left: 30
};

var width = svgWidth - margin.left - margin.right;
var height = svgHeight - margin.top - margin.bottom;

//  Create  SVG wrapper, append w SVG group to contain it per the above specs.
var svg = d3.selectAll("#scatter")
    .append("svg")
    .attr("width", svgWidth)
    .attr("height", svgHeight);

var chartGroup = svg.append("g")
    .attr("transform", `translate(${margin.left}, ${margin.top})`);

// Import Data
d3.csv("./assets/data/data.csv").then(function (fileData) {

    // Print Data
    console.log(fileData);

    // Cast as numbers
    fileData.forEach(function (d) {
        d.smokes = +d.smokes;
        d.age = +d.age;
    });
    // Create Scale Function
    var xLinearScale = d3.scaleLinear()
        .domain([9, d3.max(fileData, d => d.smokes)])
        .range([0, width]);

    var yLinearScale = d3.scaleLinear()
        .domain([30, d3.max(fileData, d => d.age)])
        .range([height, 0]);

    // Create axis function
    var bottomAxis = d3.axisBottom(xLinearScale);
    var leftAxis = d3.axisLeft(yLinearScale);

    // Append axes to Chart
    chartGroup.append("g")
        .attr("transform", `translate(0, ${height})`)
        .call(bottomAxis);

    chartGroup.append("g")
        .call(leftAxis);

        // create circle data markers
        var circleMarks = chartGroup.selectAll("circle")
        .data(fileData)
        .enter()
        .append("circle")
        .attr("cx", d => xLinearScale(d.smokes))
        .attr("cy", d => yLinearScale(d.age))
        .attr("r", "10")
        // .attr("fill", "pink")
        .attr("opacity", ".5");

        var state = fileData.map(d => d.state);
        console.log("States", state);

        // var age = fileData.map(d => d.age);
        // console.log("age", age);

        // var smokers = fileData.map(d => d.smokes);
        // console.log("smokes", smokers);

        fileData.forEach(function (d) {
            d.smokes = +d.smokes;
            console.log("State:", d.state);
            console.log("Smokers:", d.smokes);
        });
    }).catch(function (error) {
        console.log(error);

});