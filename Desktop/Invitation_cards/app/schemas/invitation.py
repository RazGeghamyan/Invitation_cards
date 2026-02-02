from pydantic import BaseModel, ConfigDict
from typing import Optional, List, Dict, Any, TYPE_CHECKING
from datetime import datetime

if TYPE_CHECKING:
    from .invitation_media import InvitationMediaSchema
    from .rsvp import RSVPResponseSchema


class InvitationBase(BaseModel):
    slug: str
    event_title: str
    event_date: datetime  # 📅 Ավելացվեց՝ պարտադիր է թայմերի համար
    template_id: int
    music_url: Optional[str] = None
    order_id: Optional[int] = None

    # JSON դաշտերը՝ դինամիկ տեքստերի և վայրերի համար
    content_data: Optional[Dict[str, Any]] = None  # 📝 Ավելացվեց
    locations_data: Optional[List[Dict[str, Any]]] = None  # 📍 Ավելացվեց

    guest_token: Optional[str] = None


class InvitationCreate(InvitationBase):
    admin_token: Optional[str] = None


class InvitationSchema(InvitationBase):
    id: int
    created_at: datetime
    admin_token: str

    # Pydantic v2-ում օգտագործվում է model_config, բայց Config-ը նույնպես աշխատում է
    model_config = ConfigDict(from_attributes=True)


class InvitationFullSchema(InvitationSchema):
    media_files: List["InvitationMediaSchema"] = []
    responses: List["RSVPResponseSchema"] = []