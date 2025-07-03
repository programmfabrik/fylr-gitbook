# geojson

The `geojson` type stores [GeoJSON](https://geojson.org/) according to [RFC 7946](https://datatracker.ietf.org/doc/html/rfc7946). For full **GeoJSON** support you need to use [**Opensearch**](https://opensearch.org/) as indexer or a licensed [**Elasticsearch**](https://www.elastic.co/subscriptions).

Also, for **fylr** you will need a license with **GeoJSON** support. The license is not needed to use **GeoJSON** over [**/api/db**](../api/endpoints/api-db.md), but it is for [**/api/search**](../api/endpoints/api-search.md).

## API

GeoJSON can contain multiple types of geo coordinates. The simplest type is Point which references a single point using latitude, longitude and altitude (optional):

```json
{
  "geo": {
    "type": "Point",
    "coordinates": [6.8652, 45.8326, 10]
  }
}
```

In this example sets a `Point` in column `geo`: The longitude is set to `6.8652`, latitude to `45.8326` and altitude to `10`. Other types storable in **GeoJSON** are: "Point", "MultiPoint", "LineString", "MultiLineString", "Polygon", "MultiPolygon", and "GeometryCollection". fylr also supports "Feature" and "FeatureCollection".

## Index

The type [`geo_shape`](https://www.elastic.co/guide/en/elasticsearch/reference/current/geo-shape.html) is used to store the **GeoJSON** value in the indexer.

**fylr** is not validating the data in detail (only types are checked), but the indexer does. So, in some cases, the API will accept the **GeoJSON** but the indexer won't, skipping the field and not indexing the data. In such a case, make sure to send valid **GeoJSON.** Use pages like [https://geojsonlint.com/](https://geojsonlint.com/) to validate your data.

However, due to the nature of how the indexers work, it is not possible to index data in nested tables. If your **GeoJSON** is inside a nested, you will not be able to see that data on the map or search for it. Please contact our support if you really need this feature, we can re-evaluate how much work it would be to put that in by merging the data into the top level.

The values of all `properties` of types "Feature" and "FeatureCollection" are collected and indexed as [`text`](text-text_oneline.md).

## Sorting

Sorting is not supported for the `geojson` type.

## Export

The **XML** exports the actual GeoJSON value in JSON format. For the above example:

```xml
<geo type="geo_json" column-api-id="2">
   {&#34;coordinates&#34;:[6.8652,45.8326,10],&#34;type&#34;:&#34;Point&#34;}
</geo>
```

The **CSV** contains the JSON as text:

```json
{"coordinates":[6.8652,45.8326,10],"type":"Point"}
```

Same with **JSON**, the export looks like this:

```json
{
  "geo": {
  "type": "Point",
  "coordinates": [
    6.8652,
    45.8326,
    10
  ]
},
```
