(function () {

	'use strict';
	/* global L */
	var map;
	var usaStates;

/* Project specific Javascript goes here. */
    $(document).ready(function () {

    map = L.mapbox.map('map', 'aclaval.ng3dimeg');
    var dataurl = '/state.geojson';
    // Download GeoJSON via Ajax
    $.getJSON(dataurl, function (data) {
        // Add GeoJSON layer
        usaStates = L.geoJson(data, {style: style}).addTo(map);
    });

	});

	function style(feature) {
	    return {
	        fillColor: getColor(feature.properties.pourcentageAfricanAmerican),
	        weight: 1,
	        opacity: 1,
	        color: 'white',
	        dashArray: '3',
	        fillOpacity: 0.6
	    };
	}

	function getColor(d) {
		return d > 35 ? '#003380' :
			d > 30  ? '#0044AA' :
			d > 25  ? '#0055D4' :
			d > 20  ? '#0066FF' :
			d > 15   ? '#2A7FFF' :
			d > 10   ? '#5599FF' :
			d > 5   ? '#80B3FF' :
				'#D5E5FF';
	}

}());