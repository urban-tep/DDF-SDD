.. _wps_interface:

Web Processing Services Interface
---------------------------------

This is the interface of Web Processing Services. They are provided by Urban TEP processing centres or by third party systems external to the platform. They are used by the portal that offers processing services to users through them.

The following normative references are applicable to this interface:

- `OGC Web Processing Service 1.0 <http://portal.opengeospatial.org/files/?artifact_id=24151>`_

WPS 2.0 will be considered for future evolution of the system. As soon as the open source implementations used will support functions like cancel it is intended to consider this also in the Urban TEP system.

The processing services offered by processing centres use the following parameters and conventions in the frame of WPS:

+------------------------------------+------------------------------------------------------------------------------+---------------------------------+
| Request element                    | Description                                                                  | Example value                   |
+====================================+==============================================================================+=================================+
| /wps:Execute/ows:Identifier        | identifier of the processor to be called,                                    |                                 |
|                                    | provided in response to getCapabilities WPS request                          | urbantep-subsetting~1.0~Subset  |
+------------------------------------+------------------------------------------------------------------------------+---------------------------------+
| /wps:Execute/wps:DataInputs        | identifier of the generic processing workflow type, e.g. L2Plus for          | L2Plus                          |
| [ows:Identifier='productionType']  | 'n outputs for n inputs, plus formatting', or L3 for 'additional             |                                 |
| /wps:Data/wps:LiteralData          | aggregation into one output product', workflow types provided in response    |                                 |
|                                    | to getCapabilities and describeProcess WPS request                           |                                 |
+------------------------------------+------------------------------------------------------------------------------+---------------------------------+
| /wps:Execute/wps:DataInputs        | user-provided name of the request                                            | GUF of Cairo                    |
| [ows:Identifier='productionName']  |                                                                              |                                 |
| /wps:Data/wps:LiteralData          |                                                                              |                                 |
|                                    |                                                                              |                                 |
+------------------------------------+------------------------------------------------------------------------------+---------------------------------+
| /wps:Execute/wps:DataInputs        | identifier of the dataset that shall be processed                            | DLR GUF 12m Europe Tiles (Urban |
| [ows:Identifier='inputDatasetName']| provided in response to the describeProcess WPS request                      | TEP)                            |
| /wps:Data/wps:LiteralData          |                                                                              |                                 |
+------------------------------------+------------------------------------------------------------------------------+---------------------------------+
| /wps:Execute/wps:DataInputs        | user-provided AOI as OGC well-known text (WKT) polygon                       | POLYGON((29.5 29.1,29.5 31.9,   |
| [ows:Identifier='regionWKT']       |                                                                              | 32.8 31.9,32.8 29.1,29.5 29.1)) |
| /wps:Data/wps:LiteralData          |                                                                              |                                 |
+------------------------------------+------------------------------------------------------------------------------+---------------------------------+
| /wps:Execute/wps:DataInputs        | identifier of the output file format to be used, one of NetCDF4, GeoTIFF     | GeoTIFF                         |
| [ows:Identifier='outputFormat']    |                                                                              |                                 |
| /wps:Data/wps:LiteralData          |                                                                              |                                 |
+------------------------------------+------------------------------------------------------------------------------+---------------------------------+
