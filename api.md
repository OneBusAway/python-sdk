# Shared Types

```python
from open_transit.types import ResponseWrapper
```

# AgenciesWithCoverage

Types:

```python
from open_transit.types import AgenciesWithCoverageListResponse
```

Methods:

- <code title="get /api/where/agencies-with-coverage.json">client.agencies_with_coverage.<a href="./src/open_transit/resources/agencies_with_coverage.py">list</a>() -> <a href="./src/open_transit/types/agencies_with_coverage_list_response.py">AgenciesWithCoverageListResponse</a></code>

# Config

Types:

```python
from open_transit.types import ConfigRetrieveResponse
```

Methods:

- <code title="get /api/where/config.json">client.config.<a href="./src/open_transit/resources/config.py">retrieve</a>() -> <a href="./src/open_transit/types/config_retrieve_response.py">ConfigRetrieveResponse</a></code>

# CurrentTime

Types:

```python
from open_transit.types import CurrentTimeRetrieveResponse
```

Methods:

- <code title="get /api/where/current-time.json">client.current_time.<a href="./src/open_transit/resources/current_time.py">retrieve</a>() -> <a href="./src/open_transit/types/current_time_retrieve_response.py">CurrentTimeRetrieveResponse</a></code>

# StopsForLocation

Types:

```python
from open_transit.types import StopsForLocationListResponse
```

Methods:

- <code title="get /api/where/stops-for-location.json">client.stops_for_location.<a href="./src/open_transit/resources/stops_for_location.py">list</a>(\*\*<a href="src/open_transit/types/stops_for_location_list_params.py">params</a>) -> <a href="./src/open_transit/types/stops_for_location_list_response.py">StopsForLocationListResponse</a></code>

# ArrivalAndDepartureForStop

Types:

```python
from open_transit.types import ArrivalAndDepartureForStopRetrieveResponse
```

Methods:

- <code title="get /api/where/arrival-and-departure-for-stop/{stopID}.json">client.arrival_and_departure_for_stop.<a href="./src/open_transit/resources/arrival_and_departure_for_stop.py">retrieve</a>(stop_id, \*\*<a href="src/open_transit/types/arrival_and_departure_for_stop_retrieve_params.py">params</a>) -> <a href="./src/open_transit/types/arrival_and_departure_for_stop_retrieve_response.py">ArrivalAndDepartureForStopRetrieveResponse</a></code>

# ArrivalsAndDeparturesForStop

Types:

```python
from open_transit.types import ArrivalsAndDeparturesForStopListResponse
```

Methods:

- <code title="get /api/where/arrivals-and-departures-for-stop/{stopID}.json">client.arrivals_and_departures_for_stop.<a href="./src/open_transit/resources/arrivals_and_departures_for_stop.py">list</a>(stop_id) -> <a href="./src/open_transit/types/arrivals_and_departures_for_stop_list_response.py">ArrivalsAndDeparturesForStopListResponse</a></code>
