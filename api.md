# Shared Types

```python
from open_transit.types import ResponseWrapper
```

# API

## Where

### AgenciesWithCoverage

Types:

```python
from open_transit.types.api.where import AgenciesWithCoverageListResponse
```

Methods:

- <code title="get /api/where/agencies-with-coverage.json">client.api.where.agencies_with_coverage.<a href="./src/open_transit/resources/api/where/agencies_with_coverage.py">list</a>() -> <a href="./src/open_transit/types/api/where/agencies_with_coverage_list_response.py">AgenciesWithCoverageListResponse</a></code>

### Config

Types:

```python
from open_transit.types.api.where import ConfigRetrieveResponse
```

Methods:

- <code title="get /api/where/config.json">client.api.where.config.<a href="./src/open_transit/resources/api/where/config.py">retrieve</a>() -> <a href="./src/open_transit/types/api/where/config_retrieve_response.py">ConfigRetrieveResponse</a></code>

### CurrentTime

Types:

```python
from open_transit.types.api.where import CurrentTimeRetrieveResponse
```

Methods:

- <code title="get /api/where/current-time.json">client.api.where.current_time.<a href="./src/open_transit/resources/api/where/current_time.py">retrieve</a>() -> <a href="./src/open_transit/types/api/where/current_time_retrieve_response.py">CurrentTimeRetrieveResponse</a></code>

### StopsForLocation

Types:

```python
from open_transit.types.api.where import StopsForLocationListResponse
```

Methods:

- <code title="get /api/where/stops-for-location.json">client.api.where.stops_for_location.<a href="./src/open_transit/resources/api/where/stops_for_location.py">list</a>(\*\*<a href="src/open_transit/types/api/where/stops_for_location_list_params.py">params</a>) -> <a href="./src/open_transit/types/api/where/stops_for_location_list_response.py">StopsForLocationListResponse</a></code>

### ArrivalAndDepartureForStop

Types:

```python
from open_transit.types.api.where import ArrivalAndDepartureForStopRetrieveResponse
```

Methods:

- <code title="get /api/where/arrival-and-departure-for-stop/{stopID}.json">client.api.where.arrival_and_departure_for_stop.<a href="./src/open_transit/resources/api/where/arrival_and_departure_for_stop.py">retrieve</a>(stop_id, \*\*<a href="src/open_transit/types/api/where/arrival_and_departure_for_stop_retrieve_params.py">params</a>) -> <a href="./src/open_transit/types/api/where/arrival_and_departure_for_stop_retrieve_response.py">ArrivalAndDepartureForStopRetrieveResponse</a></code>

### ArrivalsAndDeparturesForStop

Types:

```python
from open_transit.types.api.where import ArrivalsAndDeparturesForStopListResponse
```

Methods:

- <code title="get /api/where/arrivals-and-departures-for-stop/{stopID}.json">client.api.where.arrivals_and_departures_for_stop.<a href="./src/open_transit/resources/api/where/arrivals_and_departures_for_stop.py">list</a>(stop_id) -> <a href="./src/open_transit/types/api/where/arrivals_and_departures_for_stop_list_response.py">ArrivalsAndDeparturesForStopListResponse</a></code>
