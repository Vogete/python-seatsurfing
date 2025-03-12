# python-seatsurfing

A Python client and library to interact with the [Seatsurfing](https://github.com/seatsurfing/) API.

> [!IMPORTANT]
> The library is a work in progress, not all functionality is available yet, or finalized.

## Installation

```sh
pip install python-seatsurfing
```

## Usage

Basic usage:

```py
from datetime import datetime
import seatsurfing

# Create client by authenticating with username/password
client = seatsurfing.Client(
    base_url="https://seatsurfing.example.com",
    username="admin@seatsurfing.local",
    password="12345678",
)

# Get bookings for the next 30 days
from_date = datetime.today()
to_date = datetime.today() + timedelta(days=30)
bookings = client.booking.get_filtered_org_bookings(from_date, to_date)

print(bookings)
```
