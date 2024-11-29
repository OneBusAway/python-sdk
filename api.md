# Shared Types

```python
from onebusaway.types import References, ResponseWrapper
```

# AgenciesWithCoverage

Types:

```python
from onebusaway.types import AgenciesWithCoverageListResponse
```

Methods:

- <code title="get /api/where/agencies-with-coverage.json">client.agencies_with_coverage.<a href="./src/onebusaway/resources/agencies_with_coverage.py">list</a>() -> <a href="./src/onebusaway/types/agencies_with_coverage_list_response.py">AgenciesWithCoverageListResponse</a></code>

# Agency

Types:

```python
from onebusaway.types import AgencyRetrieveResponse
```

Methods:

- <code title="get /api/where/agency/{agencyID}.json">client.agency.<a href="./src/onebusaway/resources/agency.py">retrieve</a>(agency_id) -> <a href="./src/onebusaway/types/agency_retrieve_response.py">AgencyRetrieveResponse</a></code>

# VehiclesForAgency

Types:

```python
from onebusaway.types import VehiclesForAgencyListResponse
```

Methods:

- <code title="get /api/where/vehicles-for-agency/{agencyID}.json">client.vehicles_for_agency.<a href="./src/onebusaway/resources/vehicles_for_agency.py">list</a>(agency_id, \*\*<a href="src/onebusaway/types/vehicles_for_agency_list_params.py">params</a>) -> <a href="./src/onebusaway/types/vehicles_for_agency_list_response.py">VehiclesForAgencyListResponse</a></code>

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
from onebusaway.types import StopsForLocationListResponse
```

Methods:

- <code title="get /api/where/stops-for-location.json">client.stops_for_location.<a href="./src/onebusaway/resources/stops_for_location.py">list</a>(\*\*<a href="src/onebusaway/types/stops_for_location_list_params.py">params</a>) -> <a href="./src/onebusaway/types/stops_for_location_list_response.py">StopsForLocationListResponse</a></code>

# StopsForRoute

Types:

```python
from onebusaway.types import StopsForRouteListResponse
```

Methods:

- <code title="get /api/where/stops-for-route/{routeID}.json">client.stops_for_route.<a href="./src/onebusaway/resources/stops_for_route.py">list</a>(route_id, \*\*<a href="src/onebusaway/types/stops_for_route_list_params.py">params</a>) -> <a href="./src/onebusaway/types/stops_for_route_list_response.py">StopsForRouteListResponse</a></code>

# StopsForAgency

Types:

```python
from onebusaway.types import StopsForAgencyListResponse
```

Methods:

- <code title="get /api/where/stops-for-agency/{agencyID}.json">client.stops_for_agency.<a href="./src/onebusaway/resources/stops_for_agency.py">list</a>(agency_id) -> <a href="./src/onebusaway/types/stops_for_agency_list_response.py">StopsForAgencyListResponse</a></code>

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

# ScheduleForStop

Types:

```python
from onebusaway.types import ScheduleForStopRetrieveResponse
```

Methods:

- <code title="get /api/where/schedule-for-stop/{stopID}.json">client.schedule_for_stop.<a href="./src/onebusaway/resources/schedule_for_stop.py">retrieve</a>(stop_id, \*\*<a href="src/onebusaway/types/schedule_for_stop_retrieve_params.py">params</a>) -> <a href="./src/onebusaway/types/schedule_for_stop_retrieve_response.py">ScheduleForStopRetrieveResponse</a></code>

# Route

Types:

```python
from onebusaway.types import RouteRetrieveResponse
```

Methods:

- <code title="get /api/where/route/{routeID}.json">client.route.<a href="./src/onebusaway/resources/route.py">retrieve</a>(route_id) -> <a href="./src/onebusaway/types/route_retrieve_response.py">RouteRetrieveResponse</a></code>

# RouteIDsForAgency

Types:

```python
from onebusaway.types import RouteIDsForAgencyListResponse
```

Methods:

- <code title="get /api/where/route-ids-for-agency/{agencyID}.json">client.route_ids_for_agency.<a href="./src/onebusaway/resources/route_ids_for_agency.py">list</a>(agency_id) -> <a href="./src/onebusaway/types/route_ids_for_agency_list_response.py">RouteIDsForAgencyListResponse</a></code>

# RoutesForLocation

Types:

```python
from onebusaway.types import RoutesForLocationListResponse
```

Methods:

- <code title="get /api/where/routes-for-location.json">client.routes_for_location.<a href="./src/onebusaway/resources/routes_for_location.py">list</a>(\*\*<a href="src/onebusaway/types/routes_for_location_list_params.py">params</a>) -> <a href="./src/onebusaway/types/routes_for_location_list_response.py">RoutesForLocationListResponse</a></code>

# RoutesForAgency

Types:

```python
from onebusaway.types import RoutesForAgencyListResponse
```

Methods:

- <code title="get /api/where/routes-for-agency/{agencyID}.json">client.routes_for_agency.<a href="./src/onebusaway/resources/routes_for_agency.py">list</a>(agency_id) -> <a href="./src/onebusaway/types/routes_for_agency_list_response.py">RoutesForAgencyListResponse</a></code>

# ScheduleForRoute

Types:

```python
from onebusaway.types import ScheduleForRouteRetrieveResponse
```

Methods:

- <code title="get /api/where/schedule-for-route/{routeID}.json">client.schedule_for_route.<a href="./src/onebusaway/resources/schedule_for_route.py">retrieve</a>(route_id, \*\*<a href="src/onebusaway/types/schedule_for_route_retrieve_params.py">params</a>) -> <a href="./src/onebusaway/types/schedule_for_route_retrieve_response.py">ScheduleForRouteRetrieveResponse</a></code>

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
from onebusaway.types import TripsForLocationListResponse
```

Methods:

- <code title="get /api/where/trips-for-location.json">client.trips_for_location.<a href="./src/onebusaway/resources/trips_for_location.py">list</a>(\*\*<a href="src/onebusaway/types/trips_for_location_list_params.py">params</a>) -> <a href="./src/onebusaway/types/trips_for_location_list_response.py">TripsForLocationListResponse</a></code>

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

# TripsForRoute

Types:

```python
from onebusaway.types import TripsForRouteListResponse
```

Methods:

- <code title="get /api/where/trips-for-route/{routeID}.json">client.trips_for_route.<a href="./src/onebusaway/resources/trips_for_route.py">list</a>(route_id, \*\*<a href="src/onebusaway/types/trips_for_route_list_params.py">params</a>) -> <a href="./src/onebusaway/types/trips_for_route_list_response.py">TripsForRouteListResponse</a></code>

# ReportProblemWithStop

Methods:

- <code title="get /api/where/report-problem-with-stop/{stopID}.json">client.report_problem_with_stop.<a href="./src/onebusaway/resources/report_problem_with_stop.py">retrieve</a>(stop_id, \*\*<a href="src/onebusaway/types/report_problem_with_stop_retrieve_params.py">params</a>) -> <a href="./src/onebusaway/types/shared/response_wrapper.py">ResponseWrapper</a></code>

# ReportProblemWithTrip

Methods:

- <code title="get /api/where/report-problem-with-trip/{tripID}.json">client.report_problem_with_trip.<a href="./src/onebusaway/resources/report_problem_with_trip.py">retrieve</a>(trip_id, \*\*<a href="src/onebusaway/types/report_problem_with_trip_retrieve_params.py">params</a>) -> <a href="./src/onebusaway/types/shared/response_wrapper.py">ResponseWrapper</a></code>

# SearchForStop

Types:

```python
from onebusaway.types import SearchForStopListResponse
```

Methods:

- <code title="get /api/where/search/stop.json">client.search_for_stop.<a href="./src/onebusaway/resources/search_for_stop.py">list</a>(\*\*<a href="src/onebusaway/types/search_for_stop_list_params.py">params</a>) -> <a href="./src/onebusaway/types/search_for_stop_list_response.py">SearchForStopListResponse</a></code>

# SearchForRoute

Types:

```python
from onebusaway.types import SearchForRouteListResponse
```

Methods:

- <code title="get /api/where/search/route.json">client.search_for_route.<a href="./src/onebusaway/resources/search_for_route.py">list</a>(\*\*<a href="src/onebusaway/types/search_for_route_list_params.py">params</a>) -> <a href="./src/onebusaway/types/search_for_route_list_response.py">SearchForRouteListResponse</a></code>

# Block

Types:

```python
from onebusaway.types import BlockRetrieveResponse
```

Methods:

- <code title="get /api/where/block/{blockID}.json">client.block.<a href="./src/onebusaway/resources/block.py">retrieve</a>(block_id) -> <a href="./src/onebusaway/types/block_retrieve_response.py">BlockRetrieveResponse</a></code>

# Shape

Types:

```python
from onebusaway.types import ShapeRetrieveResponse
```

Methods:

- <code title="get /api/where/shape/{shapeID}.json">client.shape.<a href="./src/onebusaway/resources/shape.py">retrieve</a>(shape_id) -> <a href="./src/onebusaway/types/shape_retrieve_response.py">ShapeRetrieveResponse</a></code>
