// Settings
var units = "KTOE";
var nodeWidth = 20;
var nodePadding = 40;
// var dataPathName = "/api/v1.0/json?geo=EU28&year=2015";
var dataPathName = "/api/v1.0/json" + window.location.search;
console.log("Query string: %s", dataPathName)

// Set the margin as well as width and height
var margin = {top: 10, right: 10, bottom: 10, left: 10},
    width = 3200 - margin.left - margin.right, //700
    height = 800 - margin.top - margin.bottom; //300

// Format the units / numbers
var formatNumber = d3.format(",.0f"), // zero decimal places
    format = function(d) { return formatNumber(d) + " " + units; },
    color = d3.scale.category20();

// Append the svg canvas to the page
// Positions the canvas onto the page in relation to the size and margins
// which are already defined
var svg = d3.select("#chart").append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
    .append("g")
    .attr("transform",
          "translate(" + margin.left + "," + margin.top + ")");

// Set the sankey diagram properties
var sankey = d3.sankey()
    .nodeWidth(nodeWidth)
    .nodePadding(nodePadding)
    .size([width, height]);

// Define the path variable as a pointer to the sankey function that makes the
// links between the nodes to bend into the right places (other nodes)
var path = sankey.link();

// load the data
d3.json(dataPathName, function(error, graph) {
  if (error) {
    window.location = dataPathName;
    throw error;
  }

    var nodeMap = {};
    graph.nodes.forEach(function(x) { nodeMap[x.name] = x; });
    graph.links = graph.links.map(function(x) {
      return {
        source: nodeMap[x.source],
        target: nodeMap[x.target],
        value: x.value
      };
    });

  // assign the data to the sankey function
  sankey
      .nodes(graph.nodes) // nodes are in graph.nodes of the data structure
      .links(graph.links)
      .layout(32);

// add links to the diagram
  var link = svg.append("g").selectAll(".link")
      .data(graph.links)
    .enter().append("path")
      .attr("class", "link")
      .attr("d", path)
      .style("stroke-width", function(d) { return Math.max(1, d.dy); })
      .sort(function(a, b) { return b.dy - a.dy; });

// add link titles
  link.append("title")
        .text(function(d) {
        return d.source.name + " → " +
                d.target.name + "\n" + format(d.value); });

// add in the nodes
  var node = svg.append("g").selectAll(".node")
      .data(graph.nodes)
    .enter().append("g")
      .attr("class", "node")
      .attr("transform", function(d) {
      return "translate(" + d.x + "," + d.y + ")"; })
    .call(d3.behavior.drag()
      .origin(function(d) { return d; })
      .on("dragstart", function() {
      this.parentNode.appendChild(this); })
      .on("drag", dragmove));

// add the rectangles for the nodes
  node.append("rect")
      .attr("height", function(d) { return d.dy; })
      .attr("width", sankey.nodeWidth())
      .style("fill", function(d) {
      return d.color = color(d.name.replace(/ .*/, "")); })
      .style("stroke", function(d) {
      return d3.rgb(d.color).darker(2); })
    .append("title")
      .text(function(d) {
      return d.name + "\n" + format(d.value); });

// add in the title for the nodes
  node.append("text")
      .attr("x", -6)
      .attr("y", function(d) { return d.dy / 2; })
      .attr("dy", ".35em")
      .attr("text-anchor", "end")
      .attr("transform", null)
      .text(function(d) { return d.name; })
    .filter(function(d) { return d.x < width / 2; })
      .attr("x", 6 + sankey.nodeWidth())
      .attr("text-anchor", "start");

// the function for moving the nodes
  function dragmove2(d) {
    d3.select(this).attr("transform",
        "translate(" + d.x + "," + (
                d.y = Math.max(0, Math.min(height - d.dy, d3.event.y))
            ) + ")");
    sankey.relayout();
    link.attr("d", path);
  }

  function dragmove(d) {
      d3.select(this).attr("transform",
          "translate(" + (
                  d.x = Math.max(0, Math.min(width - d.dx, d3.event.x))
             ) + "," + (
                  d.y = Math.max(0, Math.min(height - d.dy, d3.event.y))
              ) + ")");
      sankey.relayout();
      link.attr("d", path);
  }
});