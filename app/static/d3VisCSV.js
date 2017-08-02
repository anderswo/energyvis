var units = "KTOE";
var dataPath = "/api/v1.0/csvdata";

// Set the margin as well as width and height
var margin = {top: 10, right: 10, bottom: 10, left: 10},
    width = 1400 - margin.left - margin.right,
    height = 740 - margin.top - margin.bottom;

// Format the units / numbers
var formatNumber = d3.format(",.0f"), // zero decimal places
    format = function(d) { return formatNumber(d) + " " + units; },
    color = d3.scale.category20();

// Append the svg canvas to the page
var svg = d3.select("#chart").append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
  .append("g")
    .attr("transform",
          "translate(" + margin.left + "," + margin.top + ")");

// Set the sankey diagram properties
var sankey = d3.sankey()
    .nodeWidth(36)
    .nodePadding(10)
    .size([width, height]);

var path = sankey.link();

// load the data with d3.csv instead of d3.json
//for another much simpler example uncomment the below
// d3.csv(dataPath, function(error, data) {
d3.csv(dataPath, function(error, data) {
  console.log('Collecting data from api: %s', dataPath);
    //set up graph in same style as original example but empty
    //Declares a graph to consist of two empty arrays called nodes and links
      graph = {"nodes" : [], "links" : []};

                data.forEach(function (d) {
                    graph.nodes.push({ "name": d.source });
                    graph.nodes.push({ "name": d.target });

                    graph.links.push({ "source": d.source, "target": d.target, "value": +d.value });
                });

                //thanks Mike Bostock https://groups.google.com/d/msg/d3-js/pl297cFtIQk/Eso4q_eBu1IJ
                //this handy little function returns only the distinct / unique nodes
                graph.nodes = d3.keys(d3.nest()
                         .key(function (d) { return d.name; })
                         .map(graph.nodes));

                //it appears d3 with force layout wants a numeric source and target
                //so loop through each link replacing the text with its index from node
                graph.links.forEach(function (d, i) {
                    graph.links[i].source = graph.nodes.indexOf(graph.links[i].source);
                    graph.links[i].target = graph.nodes.indexOf(graph.links[i].target);
                });

                //now loop through each nodes to make nodes an array of objects rather than an array of strings
                graph.nodes.forEach(function (d, i) {
                    graph.nodes[i] = { "name": d };
                });

  sankey
      .nodes(graph.nodes)
      .links(graph.links)
      .layout(32);

// add in the links
  var link = svg.append("g").selectAll(".link")
      .data(graph.links)
    .enter().append("path")
      .attr("class", "link")
      .attr("d", path)
      .style("stroke-width", function(d) { return Math.max(1, d.dy); })
      .sort(function(a, b) { return b.dy - a.dy; });

// add the link titles
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