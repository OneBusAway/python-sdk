# Where

## AgenciesWithCoverage

Types:

```python
from open_transit.types.where import AgenciesWithCoverageListResponse
```

Methods:

- <code title="get /api/where/agencies-with-coverage.json">client.where.agencies_with_coverage.<a href="./src/open_transit/resources/where/agencies_with_coverage.py">list</a>() -> <a href="./src/open_transit/types/where/agencies_with_coverage_list_response.py">AgenciesWithCoverageListResponse</a></code>

## Config

Types:

```python
from open_transit.types.where import ConfigRetrieveResponse
```

Methods:

- <code title="get /api/where/config.json">client.where.config.<a href="./src/open_transit/resources/where/config.py">retrieve</a>() -> <a href="./src/open_transit/types/where/config_retrieve_response.py">ConfigRetrieveResponse</a></code>

## CurrentTime

Types:

```python
from open_transit.types.where import CurrentTimeRetrieveResponse
```

Methods:

- <code title="get /api/where/current-time.json">client.where.current_time.<a href="./src/open_transit/resources/where/current_time.py">retrieve</a>() -> <a href="./src/open_transit/types/where/current_time_retrieve_response.py">CurrentTimeRetrieveResponse</a></code>

## StopsForLocation

Types:

```python
from open_transit.types.where import StopsForLocationListResponse
```

Methods:

- <code title="get /api/where/stops-for-location.json">client.where.stops_for_location.<a href="./src/open_transit/resources/where/stops_for_location.py">list</a>(\*\*<a href="src/open_transit/types/where/stops_for_location_list_params.py">params</a>) -> <a href="./src/open_transit/types/where/stops_for_location_list_response.py">StopsForLocationListResponse</a></code>

## Stop

### ArrivalAndDeparture

Types:

```python
from open_transit.types.where.stop import ArrivalAndDepartureRetrieveResponse
```

Methods:

- <code title="get /api/where/arrival-and-departure-for-stop/{stopID}.json">client.where.stop.arrival_and_departure.<a href="./src/open_transit/resources/where/stop/arrival_and_departure.py">retrieve</a>(stop_id, \*\*<a href="src/open_transit/types/where/stop/arrival_and_departure_retrieve_params.py">params</a>) -> <a href="./src/open_transit/types/where/stop/arrival_and_departure_retrieve_response.py">ArrivalAndDepartureRetrieveResponse</a></code>

### ArrivalsAndDepartures

Types:

```python
from open_transit.types.where.stop import ArrivalsAndDepartureListResponse
```

Methods:

- <code title="get /api/where/arrivals-and-departures-for-stop/{stopID}.json">client.where.stop.arrivals_and_departures.<a href="./src/open_transit/resources/where/stop/arrivals_and_departures.py">list</a>(stop_id) -> <a href="./src/open_transit/types/where/stop/arrivals_and_departure_list_response.py">ArrivalsAndDepartureListResponse</a></code>
