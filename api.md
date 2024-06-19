# Shared Types

```python
from onebusaway.types import ResponseWrapper
```

# AgenciesWithCoverage

Types:

```python
from onebusaway.types import AgenciesWithCoverageListResponse
```

Methods:

- <code title="get /api/where/agencies-with-coverage.json">client.agencies_with_coverage.<a href="./src/onebusaway/resources/agencies_with_coverage.py">list</a>() -> <a href="./src/onebusaway/types/agencies_with_coverage_list_response.py">AgenciesWithCoverageListResponse</a></code>

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

# ArrivalAndDepartureForStop

Types:

```python
from onebusaway.types import ArrivalAndDepartureForStopRetrieveResponse
```

Methods:

- <code title="get /api/where/arrival-and-departure-for-stop/{stopID}.json">client.arrival_and_departure_for_stop.<a href="./src/onebusaway/resources/arrival_and_departure_for_stop.py">retrieve</a>(stop_id, \*\*<a href="src/onebusaway/types/arrival_and_departure_for_stop_retrieve_params.py">params</a>) -> <a href="./src/onebusaway/types/arrival_and_departure_for_stop_retrieve_response.py">ArrivalAndDepartureForStopRetrieveResponse</a></code>

# ArrivalsAndDeparturesForStop

Types:

```python
from onebusaway.types import ArrivalsAndDeparturesForStopListResponse
```

Methods:

- <code title="get /api/where/arrivals-and-departures-for-stop/{stopID}.json">client.arrivals_and_departures_for_stop.<a href="./src/onebusaway/resources/arrivals_and_departures_for_stop.py">list</a>(stop_id) -> <a href="./src/onebusaway/types/arrivals_and_departures_for_stop_list_response.py">ArrivalsAndDeparturesForStopListResponse</a></code>
