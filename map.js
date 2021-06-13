function init() {
map = new OpenLayers.Map("basicMap", {
    controls: [
               new OpenLayers.Control.Navigation(),
               new OpenLayers.Control.ArgParser(),
               new OpenLayers.Control.Attribution()
           ]
       });
var mapnik         = new OpenLayers.Layer.OSM();
var fromProjection = new OpenLayers.Projection("EPSG:4326");   // Transform from WGS 1984
var toProjection   = new OpenLayers.Projection("EPSG:900913"); // to Spherical Mercator Projection
var position       = new OpenLayers.LonLat(7.55785346031189,50.3625329673905).transform( fromProjection, toProjection);
var zoom           = 3

map.addLayer(mapnik);
map.setCenter(position, zoom );

var markers = new OpenLayers.Layer.Markers( "Markers" );
map.addLayer(markers);

var marker = new OpenLayers.Marker(position);

marker.events.register("click", map , function(e){ alert("click");
});

markers.addMarker(marker);
}