from datetime import datetime
import json
import logging
from seatsurfing.common.http_client import SeatsurfingHttpClient
from seatsurfing.models.booking import Booking as BookingModel

logger = logging.getLogger(__name__)


class Booking(SeatsurfingHttpClient):
    def get_own_booking(self, booking_id: str):
        r = self._get(f"/booking/{booking_id}")
        logger.debug(r)

    def get_filtered_org_bookings(
        self, from_date: datetime, to_date: datetime
    ) -> list[BookingModel]:
        """
        Get filtered org bookings.

        Currently supports time period.
        """
        from_date_str = from_date.strftime("%Y-%m-%dT%H:%M:%SZ")
        to_date_str = to_date.strftime("%Y-%m-%dT%H:%M:%SZ")
        data = {"start": from_date_str, "end": to_date_str}
        r = self._post("/booking/filter/", data=data)

        return [BookingModel(**x) for x in r]
