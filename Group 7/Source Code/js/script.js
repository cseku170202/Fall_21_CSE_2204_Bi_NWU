// Get the input elements
const sourceInput = document.getElementById('source-input');
const verticesInput = document.getElementById('vertices-input');
const edgesInput = document.getElementById('edges-input');

// Get the visualization elements
const graphDisplay = document.getElementById('graph');
const resultDisplay = document.getElementById('result');

// Get the run button
const runButton = document.getElementById('run-button');

// Add event listener to the run button
runButton.addEventListener('click', () => {
  // Get the input values
  const source = parseInt(sourceInput.value);
  const vertices = parseInt(verticesInput.value);
  const edges = JSON.parse(edgesInput.value);

  // Run the Bellman-Ford algorithm
  const result = bellmanFord(source, vertices, edges);

  // Display the graph and result
  displayGraph(graphDisplay, vertices, edges, result);
  function displayResult(resultDisplay, result, sourceVertex) {
    const resultString = result.map((distance, index) => {
      return `Shortest path from ${sourceVertex} to ${index}: ${distance}`;
    }).join('\n');

    resultDisplay.textContent = resultString;
  }



});

// Bellman-Ford algorithm
function bellmanFord(source, vertices, edges) {
  // Initialize the distance array
  const distance = new Array(vertices).fill(Number.MAX_VALUE);
  distance[source] = 0;

  // Iterate through all the edges
  for (const edge of edges) {
    const { from, to, weight } = edge;

    if (distance[from] != Number.MAX_VALUE && distance[from] + weight < distance[to]) {
      distance[to] = distance[from] + weight;
    }
  }

  // Check for negative cycles
  for (const edge of edges) {
    const { from, to, weight } = edge;

    if (distance[from] != Number.MAX_VALUE && distance[from] + weight < distance[to]) {
      throw new Error('Negative cycle detected');
    }
  }

  // Return the distance array
  return distance;
}

// Display the graph
function displayGraph(graphDisplay, vertices, edges, result) {
  // Clear the graph display
  graphDisplay.innerHTML = '';

  // Create the graph SVG element
  const svg = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
  svg.setAttribute('viewBox', '0 0 600 500');

  // Draw the edges
  const edgePaths = edges.map(({ from, to, weight }) => {
    const fromX = 50 + from * 100;
    const fromY = 200 + result[from] * 50;
    const toX = 50 + to * 100;
    const toY = 200 + result[to] * 50;
    return { path: `M ${fromX},${fromY} L ${toX},${toY}`, fromX, fromY, toX, toY };
  });

  const edgeElements = edgePaths.map(({ path, fromX, fromY, toX, toY }) => {
    const element = document.createElementNS('http://www.w3.org/2000/svg', 'path');
    element.setAttribute('d', path);
    element.setAttribute('stroke', 'black');
    element.setAttribute('stroke-width', 2);
    element.setAttribute('marker-end', 'url(#arrowhead)');

    // Add an animated arrowhead to the edge
    const marker = document.createElementNS('http://www.w3.org/2000/svg', 'use');
    marker.setAttribute('href', '#arrowhead');
    const animate = document.createElementNS('http://www.w3.org/2000/svg', 'animateMotion');
    animate.setAttribute('dur', '2s');
    animate.setAttribute('repeatCount', 'indefinite');
    animate.setAttribute('path', `M ${fromX},${fromY} L ${toX},${toY}`);
    marker.appendChild(animate);
    element.appendChild(marker);

    return element;
  });

  svg.append(...edgeElements);

  // Draw the vertices
  for (let i = 0; i < vertices; i++) {
    const circle = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
    circle.setAttribute('cx', 50 + i * 100);
    circle.setAttribute('cy', 200 + result[i] * 50);
    circle.setAttribute('r', 20);
    circle.setAttribute('fill', 'white');

    const text = document.createElementNS('http://www.w3.org/2000/svg', 'text');
    text.setAttribute('x', 50 + i * 100);
    text.setAttribute('y', 200 + result[i] * 50);
    text.setAttribute('text-anchor', 'middle');
    text.setAttribute('alignment-baseline', 'middle');
    text.textContent = i;

    svg.appendChild(circle);
    svg.appendChild(text);
  }

  // Add the arrowhead marker
  const arrowhead = document.createElementNS('http://www.w3.org/2000/svg', 'marker');
  arrowhead.setAttribute('id', 'arrowhead');
  arrowhead.setAttribute('markerWidth', '10');
  arrowhead.setAttribute('markerHeight', '7');
  arrowhead.setAttribute('refX', '8');
  arrowhead.setAttribute('refY', '3.5');
  arrowhead.setAttribute('orient', 'auto');
  const path = document.createElementNS('http://www.w3.org/2000/svg', 'path');
  path.setAttribute('d', 'M 0,0 L 10,3.5 L 0,7 Z');
  path.setAttribute('fill', 'black');

  // Add the animation to the arrowhead
  const animate = document.createElementNS('http://www.w3.org/2000/svg', 'animate');
  animate.setAttribute('attributeName', 'opacity');
  animate.setAttribute('from', '0');
  animate.setAttribute('to', '1');
  animate.setAttribute('dur', '0.5s');
  animate.setAttribute('begin', 'indefinite');
  arrowhead.appendChild(animate);

  arrowhead.appendChild(path);
  svg.appendChild(arrowhead);

  graphDisplay.appendChild(svg);
};
