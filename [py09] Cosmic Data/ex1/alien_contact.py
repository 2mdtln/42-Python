# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   alien_contact.py                                    :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#   By: mtaheri <mtaheri@student.42istanbul.com.tr> +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#   Created: 2026/04/14 11:02:38 by mtaheri            #+#    #+#             #
#   Updated: 2026/04/14 11:34:56 by mtaheri           ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

from enum import Enum
from pydantic import BaseModel, Field, ValidationError, model_validator
from datetime import datetime
from typing import Optional


class ContactType(str, Enum):
    radio = "radio"
    visual = "visual"
    physical = "physical"
    telepathic = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(..., min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(..., min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(..., ge=0.0, le=10.0)
    duration_minutes: int = Field(..., ge=1, le=1440)
    witness_count: int = Field(..., ge=1, le=100)
    message_received: Optional[str] = Field(None, max_length=500)
    is_verified: bool = False

    @model_validator(mode="after")
    def validate_contact(self):
        if not self.contact_id.startswith("AC"):
            raise ValueError("Contact ID must start with 'AC'")
        if self.contact_type == ContactType.physical and not self.is_verified:
            raise ValueError("Physical contact reports must be verified")
        if (self.contact_type == ContactType.telepathic and
           self.witness_count < 3):
            raise ValueError("Telepathic contact requires < 3 witnesses")
        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError("Strong signals (> 7.0) should include messages")
        return self


def main():
    print("Alien Contact Log Validation")
    print("=" * 38)

    contact = AlienContact(
        contact_id="AC_2026_001",
        contact_type=ContactType.radio,
        location="Area 51, Nevada",
        timestamp="2026-04-14T12:42:42",
        signal_strength=8.5,
        duration_minutes=45,
        witness_count=5,
        message_received="Greetings from Zeta Reticuli",
        is_verified=True,
    )

    print("Valid contact report:")
    print(f"ID: {contact.contact_id}")
    print(f"Type: {contact.contact_type.value}")
    print(f"Location: {contact.location}")
    print(f"Signal: {contact.signal_strength}/10")
    print(f"Duration: {contact.duration_minutes} minutes")
    print(f"Witnesses: {contact.witness_count}")
    print(f"Message: '{contact.message_received}'")
    print("=" * 38)

    try:
        AlienContact(
            contact_id="AC_2011_002",
            timestamp="2011-11-11T11:11:11",
            location="Roswell, New Mexico",
            contact_type=ContactType.telepathic,
            signal_strength=6.0,
            duration_minutes=30,
            witness_count=1,  # boom
            is_verified=False,
        )
    except ValidationError as e:
        print("Expected validation error:")
        for error in e.errors():
            msg = error.get("ctx", {}).get("error", error["msg"])
            print(msg)


if __name__ == "__main__":
    main()
