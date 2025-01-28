from pydantic import BaseModel, Field


class Location(BaseModel):
    id: str
    organizationId: str
    map_width: int = Field(alias="mapWidth")
    map_height: int = Field(alias="mapHeight")
    map_mime_type: str = Field(alias="mapMimeType")
    name: str
    description: str
    max_concurrent_booking: int = Field(alias="maxConcurrentBookings")
    timezone: str
    enabled: bool


class Space(BaseModel):
    id: str
    available: bool
    location_id: str = Field(alias="locationId")
    location: Location
    name: str
    x: int
    y: int
    width: int
    height: int
    rotation: int


class Booking(BaseModel):
    id: str
    user_id: str = Field(alias="userId")
    user_email: str = Field(alias="userEmail")
    space: Space
    space_id: str = Field(alias="spaceId")
    enter: str
    leave: str
