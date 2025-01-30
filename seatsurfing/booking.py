from datetime import datetime
import json
import logging
from seatsurfing.common.http_client import SeatsurfingHttpClient
from seatsurfing.models.booking import Booking, BookingCreateOrUpdateDTO

logger = logging.getLogger(__name__)


# TODO: this whole thing needs a lot of docs and hints still.


class Bookings(SeatsurfingHttpClient):
    """
    Documentation: https://seatsurfing.io/docs/rest-api#bookings
    """

    def get_bookings(self):
        """Unfinished"""
        r = self._get("/booking/")
        return [Booking(**x) for x in r.json()]

    def get_booking(self, booking_id: str):
        """Unfinished"""
        r = self._get(f"/booking/{booking_id}")
        return Booking(**(r.json()))

    def get_filtered_org_bookings(
        self, from_date: datetime, to_date: datetime
    ) -> list[Booking]:
        """
        Get filtered org bookings.

        Currently supports time period.
        """
        from_date_str = from_date.strftime("%Y-%m-%dT%H:%M:%SZ")
        to_date_str = to_date.strftime("%Y-%m-%dT%H:%M:%SZ")
        data = {"start": from_date_str, "end": to_date_str}
        r = self._post("/booking/filter/", data=data)
        return [Booking(**x) for x in r.json()]

    def create_booking(
        self,
        booking_id: str,
        enter: str,
        leave: str,
        space_id: str,
        user_email: str = "",
    ):
        """
        `user_email` should only be filled out if you are an admin, and can create bookings on behalf of others.
        """
        data = BookingCreateOrUpdateDTO(
            enter=enter, leave=leave, spaceId=space_id, userEmail=user_email
        )
        self._post(f"/booking/{booking_id}", data=data)

    def update_booking(
        self, booking_id: str, enter: str, leave: str, space_id: str, user_email: str
    ):
        data = BookingCreateOrUpdateDTO(
            enter=enter, leave=leave, spaceId=space_id, userEmail=user_email
        )
        self._put(f"/booking/{booking_id}", data=data)

    def delete_booking(self, booking_id: str):
        self._delete(f"/booking/{booking_id}")
