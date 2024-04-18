// Initialize the map
var map = L.map('map').setView([51.505, -0.09], 13);

// Add a tile layer (e.g., OpenStreetMap)
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '© OpenStreetMap contributors'
}).addTo(map);

// Define grid parameters
var gridBounds = [
    [40.6, -74.3], // Southwest corner
    [40.9, -73.7]  // Northeast corner
];
var gridSize = 0.1; // Grid cell size in degrees

// Add grid overlay to the map
function addGridOverlay() {
    // Create horizontal grid lines
    for (var lat = gridBounds[0][0]; lat <= gridBounds[1][0]; lat += gridSize) {
        L.polyline([[lat, gridBounds[0][1]], [lat, gridBounds[1][1]]], { color: 'blue', opacity: 0.5 }).addTo(map);
    }

    // Create vertical grid lines
    for (var lng = gridBounds[0][1]; lng <= gridBounds[1][1]; lng += gridSize) {
        L.polyline([[gridBounds[0][0], lng], [gridBounds[1][0], lng]], { color: 'blue', opacity: 0.5 }).addTo(map);
    }
}

// Call function to add grid overlay
addGridOverlay();

// Define marker locations
var markerLocations = [
    { lat: 40.7128, lng: -74.0060, name: 'New York City', description: 'The Big Apple' },
    { lat: 34.0522, lng: -118.2437, name: 'Los Angeles', description: 'City of Angels' },
    { lat: -1.286389, lng: 36.817223, name: 'Nairobi', description: 'Capital City of Kenya' },
    { lat: -4.0435, lng: 39.6682, name: 'Mombasa', description: 'Coastal City in Kenya' }
];

// Add markers to the map
function addMarkers() {
    markerLocations.forEach(function(location) {
        var marker = L.marker([location.lat, location.lng]).addTo(map);

        // Add popup with name and description
        marker.bindPopup('<b>' + location.name + '</b><br>' + location.description);

        // Add tooltip with name
        marker.bindTooltip(location.name);
    });
}

// Call function to add markers
addMarkers();




// Define function to handle map clicks
function handleMapClick(event) {
    // Extract coordinates of clicked location
    var latlng = event.latlng;
    var lat = latlng.lat;
    var lng = latlng.lng;

    // Create custom marker at clicked location
    var customMarker = L.marker([lat, lng], { draggable: true }).addTo(map);

    // Add popup with input form
    var popupContent = '<b>Custom Marker</b><br>' +
                       'Latitude: ' + lat.toFixed(6) + '<br>' +
                       'Longitude: ' + lng.toFixed(6) + '<br>' +
                       '<form>' +
                       'Name: <input type="text" id="markerName"><br>' +
                       '<button type="button" onclick="saveMarker()">Save</button>' +
                       '</form>';
    customMarker.bindPopup(popupContent).openPopup();
}

// Add click event listener to map
map.on('click', handleMapClick);

// Function to save marker data
function saveMarker() {
    var markerName = document.getElementById('markerName').value;
    // You can save the marker data or perform any other actions here
    console.log('Marker name:', markerName);
}


// Define function to handle marker drag start
function handleMarkerDragStart(event) {
    console.log('Marker drag started:', event.target);
}

// Define function to handle marker drag
function handleMarkerDrag(event) {
    console.log('Marker is being dragged:', event.target);
}

// Define function to handle marker drag end
function handleMarkerDragEnd(event) {
    var marker = event.target;
    var newPosition = marker.getLatLng();
    console.log('Marker drag ended:', newPosition);
    // You can save the new marker position or perform any other actions here
}

// Add drag event listeners to each custom marker
function addDragEventListeners() {
    map.eachLayer(function(layer) {
        if (layer instanceof L.Marker) {
            layer.on('dragstart', handleMarkerDragStart);
            layer.on('drag', handleMarkerDrag);
            layer.on('dragend', handleMarkerDragEnd);
        }
    });
}

// Call function to add drag event listeners
addDragEventListeners();


// Define function to handle location search
function searchLocation(query) {
    // Send request to geocoding service (OpenStreetMap Nominatim)
    var url = 'https://nominatim.openstreetmap.org/search?format=json&q=' + encodeURIComponent(query);
    fetch(url)
        .then(response => response.json())
        .then(data => {
            // Check if any results were found
            if (data.length > 0) {
                // Get coordinates of the first result
                var lat = parseFloat(data[0].lat);
                var lon = parseFloat(data[0].lon);
                
                // Center map on the searched location
                map.setView([lat, lon], 13);

                // Add marker at the searched location
                L.marker([lat, lon]).addTo(map)
                    .bindPopup(query)
                    .openPopup();
            } else {
                alert('Location not found');
            }
        })
        .catch(error => {
            console.error('Error searching location:', error);
            alert('An error occurred while searching for the location');
        });
}

// Define function to handle search form submission
function handleSearchFormSubmit(event) {
    event.preventDefault();
    var query = document.getElementById('searchInput').value;
    if (query.trim() !== '') {
        searchLocation(query);
    } else {
        alert('Please enter a location to search for');
    }
}

// Add event listener to search form
document.getElementById('searchForm').addEventListener('submit', handleSearchFormSubmit);
