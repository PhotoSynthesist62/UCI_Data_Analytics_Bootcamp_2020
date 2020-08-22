function init() {

  var picker = d3.select("#selDataset")

  d3.json("./data/samples.json").then((data) => {
    var subjectIDs = data.names;

    subjectIDs.forEach((id) => {
      picker
        .append("option")
        .text(id)
        .property("value", id);
    });

    var firstID = subjectIDs[0];
    buildCharts(firstID);
    buildMetadata(firstID);
  });
}

function optionChanged(newID) {
  buildCharts(newID);
  buildMetadata(newID);
}

function buildMetadata(id) {
  d3.json("./data/samples.json").then((data) => {
    var metadata = data.metadata
    var filterIDs = metadata.filter(idObject => idObject.id == id);
    var filteredIDs = filterIDs[0];
    var idData = d3.select("#sample-metadata");

    idData.html("");

    Object.entries(filteredIDs).forEach(([key, value]) => {
      idData.append("h6").text(`${key.toUpperCase()}: ${value}`);
    });
  });
};

function buildCharts(id) {
  d3.json("./data/samples.json").then((data) => {
    var samples = data.samples;
    var filterIDs = samples.filter(idObject => idObject.id == id);
    var filteredIDs = filterIDs[0];

    var otu_ids = filteredIDs.otu_ids;
    var otu_labels = filteredIDs.otu_labels;
    var sample_values = filteredIDs.sample_values;

    var bubbleTrace = [
      {
        x: otu_ids,
        y: sample_values,
        text: otu_labels,
        mode: "markers",
        marker: {
          color: otu_ids,
          colorscale: "Portland",
          size: sample_values,
        }
      }
    ];

    var bubbleLayout = {
      title: `Bacteria Cultures per Sample`,
      margin: { t: 0, b: 100 },
      hovermode: "closest",
      xaxis: { title: "OTU ID" },
      yaxis: { title: "Amount Found" }
    };

    Plotly.newPlot("bubble", bubbleTrace, bubbleLayout);

    var yticks = otu_ids.slice(0, 10).map(otuID =>
      `OTU ${otuID}`).reverse();

    var barTrace = [
      {
        x: sample_values.slice(0, 10).reverse(),
        y: yticks,
        text: otu_labels.slice(0, 10).reverse(),
        type: "bar",
        orientation: "h",
      }
    ];

    var barLayout = {
      title: `Top 10 Bacteria Cultures`,
      margin: { t: 30, l: 100 }
    };

    Plotly.newPlot("bar", barTrace, barLayout);

  });
}

init();