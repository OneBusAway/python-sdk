# Shared Types

```python
from onebusaway.types import References, ResponseWrapper
```

# AgenciesWithCoverage

Types:

```python
from onebusaway.types import AgenciesWithCoverageRetrieveResponse
```

Methods:

- <code title="get /api/where/agencies-with-coverage.json">client.agencies_with_coverage.<a href="./src/onebusaway/resources/agencies_with_coverage.py">retrieve</a>() -> <a href="./src/onebusaway/types/agencies_with_coverage_retrieve_response.py">AgenciesWithCoverageRetrieveResponse</a></code>

# Agency

Types:

```python
from onebusaway.types import AgencyRetrieveResponse
```

Methods:

- <code title="get /api/where/agency/{agencyID}.json">client.agency.<a href="./src/onebusaway/resources/agency.py">retrieve</a>(agency_id) -> <a href="./src/onebusaway/types/agency_retrieve_response.py">AgencyRetrieveResponse</a></code>

# Config

Types:

```python
from onebusaway.types import ConfigRetrieveResponse
```

Methods:

- <code title="get /api/where/config.json">client.config.<a href="./src/onebusaway/resources/config.py">retrieve</a>() -> <a href="./src/onebusaway/types/config_retrieve_response.py">ConfigRetrieveResponse</a></code>

# CurrentTime

Types:

```python
from onebusaway.types import CurrentTimeRetrieveResponse
```

Methods:

- <code title="get /api/where/current-time.json">client.current_time.<a href="./src/onebusaway/resources/current_time.py">retrieve</a>() -> <a href="./src/onebusaway/types/current_time_retrieve_response.py">CurrentTimeRetrieveResponse</a></code>

# StopsForLocation

Types:

```python
from onebusaway.types import StopsForLocationRetrieveResponse
```

Methods:

- <code title="get /api/where/stops-for-location.json">client.stops_for_location.<a href="./src/onebusaway/resources/stops_for_location.py">retrieve</a>(\*\*<a href="src/onebusaway/types/stops_for_location_retrieve_params.py">params</a>) -> <a href="./src/onebusaway/types/stops_for_location_retrieve_response.py">StopsForLocationRetrieveResponse</a></code>

# StopsForRoute

Types:

```python
from onebusaway.types import StopsForRouteListResponse
```

Methods:

- <code title="get /api/where/stops-for-route/{routeID}.json">client.stops_for_route.<a href="./src/onebusaway/resources/stops_for_route.py">list</a>(route_id, \*\*<a href="src/onebusaway/types/stops_for_route_list_params.py">params</a>) -> <a href="./src/onebusaway/types/stops_for_route_list_response.py">StopsForRouteListResponse</a></code>

# Stop

Types:

```python
from onebusaway.types import StopRetrieveResponse
```

Methods:

- <code title="get /api/where/stop/{stopID}.json">client.stop.<a href="./src/onebusaway/resources/stop.py">retrieve</a>(stop_id) -> <a href="./src/onebusaway/types/stop_retrieve_response.py">StopRetrieveResponse</a></code>

# StopIDsForAgency

Types:

```python
from onebusaway.types import StopIDsForAgencyListResponse
```

Methods:

- <code title="get /api/where/stop-ids-for-agency/{agencyID}.json">client.stop_ids_for_agency.<a href="./src/onebusaway/resources/stop_ids_for_agency.py">list</a>(agency_id) -> <a href="./src/onebusaway/types/stop_ids_for_agency_list_response.py">StopIDsForAgencyListResponse</a></code>

# Route

Types:

```python
from onebusaway.types import RouteRetrieveResponse
```

Methods:

- <code title="get /api/where/route/{routeID}.json">client.route.<a href="./src/onebusaway/resources/route.py">retrieve</a>(route_id) -> <a href="./src/onebusaway/types/route_retrieve_response.py">RouteRetrieveResponse</a></code>

# ArrivalAndDeparture

Types:

```python
from onebusaway.types import ArrivalAndDepartureRetrieveResponse, ArrivalAndDepartureListResponse
```

Methods:

- <code title="get /api/where/arrival-and-departure-for-stop/{stopID}.json">client.arrival_and_departure.<a href="./src/onebusaway/resources/arrival_and_departure.py">retrieve</a>(stop_id, \*\*<a href="src/onebusaway/types/arrival_and_departure_retrieve_params.py">params</a>) -> <a href="./src/onebusaway/types/arrival_and_departure_retrieve_response.py">ArrivalAndDepartureRetrieveResponse</a></code>
- <code title="get /api/where/arrivals-and-departures-for-stop/{stopID}.json">client.arrival_and_departure.<a href="./src/onebusaway/resources/arrival_and_departure.py">list</a>(stop_id, \*\*<a href="src/onebusaway/types/arrival_and_departure_list_params.py">params</a>) -> <a href="./src/onebusaway/types/arrival_and_departure_list_response.py">ArrivalAndDepartureListResponse</a></code>

# Trip

Types:

```python
from onebusaway.types import TripRetrieveResponse
```

Methods:

- <code title="get /api/where/trip/{tripID}.json">client.trip.<a href="./src/onebusaway/resources/trip.py">retrieve</a>(trip_id) -> <a href="./src/onebusaway/types/trip_retrieve_response.py">TripRetrieveResponse</a></code>

# TripsForLocation

Types:

```python
from onebusaway.types import TripsForLocationRetrieveResponse
```

Methods:

- <code title="get /api/where/trips-for-location.json">client.trips_for_location.<a href="./src/onebusaway/resources/trips_for_location.py">retrieve</a>(\*\*<a href="src/onebusaway/types/trips_for_location_retrieve_params.py">params</a>) -> <a href="./src/onebusaway/types/trips_for_location_retrieve_response.py">TripsForLocationRetrieveResponse</a></code>

# TripDetails

Types:

```python
from onebusaway.types import TripDetailRetrieveResponse
```

Methods:

- <code title="get /api/where/trip-details/{tripID}.json">client.trip_details.<a href="./src/onebusaway/resources/trip_details.py">retrieve</a>(trip_id, \*\*<a href="src/onebusaway/types/trip_detail_retrieve_params.py">params</a>) -> <a href="./src/onebusaway/types/trip_detail_retrieve_response.py">TripDetailRetrieveResponse</a></code>

# TripForVehicle

Types:

```python
from onebusaway.types import TripForVehicleRetrieveResponse
```

Methods:

- <code title="get /api/where/trip-for-vehicle/{vehicleID}.json">client.trip_for_vehicle.<a href="./src/onebusaway/resources/trip_for_vehicle.py">retrieve</a>(vehicle_id, \*\*<a href="src/onebusaway/types/trip_for_vehicle_retrieve_params.py">params</a>) -> <a href="./src/onebusaway/types/trip_for_vehicle_retrieve_response.py">TripForVehicleRetrieveResponse</a></code>
