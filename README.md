# python-seatsurfing

A Python client and library to interact with the [Seatsurfing](https://github.com/seatsurfing/) API.

> [!IMPORTANT]
> The library is a work in progress, not all functionality is available yet, or finalized.

## Installation

```sh
pip install python-seatsurfing
```

## Usage

Usage with known organization ID and credentials:

```py
from datetime import datetime
import seatsurfing

# Create client with authentication information
client = seatsurfing.Client(
    base_url="https://seatsurfing.example.com",
    organization_id = "9a2184f9-671f-440b-81f0-18e217af34f8",
    username="admin@seatsurfing.local",
    password="12345678",
)

# Get bookings for the next 30 days
from_date = datetime.today()
to_date = datetime.today() + timedelta(days=30)
bookings = client.booking.get_filtered_org_bookings(from_date, to_date)

print(bookings)
```

Usage with fetching data dynamically:

```py
from datetime import datetime
import seatsurfing

# Create unauthenticated client
client = seatsurfing.Client(base_url="https://seatsurfing.example.com")
# Fetch organization information
org = client.authentication.get_singleorg()

# Authenticate to the organization
client.login(organization_id=org.organization.id, username="admin@seatsurfing.local", password="1234678")

# Get bookings for the next 30 days
from_date = datetime.today()
to_date = datetime.today() + timedelta(days=30)
bookings = client.booking.get_filtered_org_bookings(from_date, to_date)

print(bookings)
```
