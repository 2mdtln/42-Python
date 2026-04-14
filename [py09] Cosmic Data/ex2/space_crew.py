# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   space_crew.py                                       :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#   By: mtaheri <mtaheri@student.42istanbul.com.tr> +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#   Created: 2026/04/14 11:34:56 by mtaheri            #+#    #+#             #
#   Updated: 2026/04/14 12:55:34 by mtaheri           ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

from enum import Enum
from pydantic import BaseModel, Field, ValidationError, model_validator
from datetime import datetime
from typing import List


class Rank(str, Enum):
    cadet = "cadet"
    officer = "officer"
    lieutenant = "lieutenant"
    captain = "captain"
    commander = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=2, max_length=50)
    rank: Rank
    age: int = Field(..., ge=18, le=80)
    specialization: str = Field(..., min_length=3, max_length=30)
    years_experience: int = Field(..., ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    mission_id: str = Field(..., min_length=5, max_length=15)
    mission_name: str = Field(..., min_length=3, max_length=100)
    destination: str = Field(..., min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(..., ge=1, le=3650)
    crew: List[CrewMember] = Field(..., min_length=1, max_length=12)
    mission_status: str = "planned"
    budget_millions: float = Field(..., ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def validate_mission(self):
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with 'M'")
        senior_ranks = {Rank.captain, Rank.commander}
        if not any(m.rank in senior_ranks for m in self.crew):
            raise ValueError("Mission must have at min 1 Commander or Captain")
        if self.duration_days > 365:
            experienced = sum(1 for m in self.crew if m.years_experience >= 5)
            if experienced / len(self.crew) < 0.5:
                raise ValueError(
                    "> 365 day missions need 50% experienced crew (5+ years)"
                )
        if not all(m.is_active for m in self.crew):
            raise ValueError("All crew members must be active")
        return self


def main():
    print("Space Mission Crew Validation")
    print("=" * 41)

    crew = [
        CrewMember(
            member_id="CM001",
            name="Sarah Connor",
            rank=Rank.commander,
            age=38,
            specialization="Mission Command",
            years_experience=15,
        ),
        CrewMember(
            member_id="CM002",
            name="John Smith",
            rank=Rank.lieutenant,
            age=30,
            specialization="Navigation",
            years_experience=8,
        ),
        CrewMember(
            member_id="CM003",
            name="Alice Johnson",
            rank=Rank.officer,
            age=26,
            specialization="Engineering",
            years_experience=5,
        ),
    ]

    mission = SpaceMission(
        mission_id="M2024_MARS",
        mission_name="Mars Colony Establishment",
        destination="Mars",
        launch_date="2024-06-01T09:00:00",
        duration_days=900,
        crew=crew,
        budget_millions=2500.0,
    )

    print("Valid mission created:")
    print(f"Mission: {mission.mission_name}")
    print(f"ID: {mission.mission_id}")
    print(f"Destination: {mission.destination}")
    print(f"Duration: {mission.duration_days} days")
    print(f"Budget: ${mission.budget_millions}M")
    print(f"Crew size: {len(mission.crew)}")
    print("Crew members:")
    for member in mission.crew:
        print(f"  - {member.name} ({member.rank.value})"
              f" - {member.specialization}")
    print("=" * 41)

    invalid_crew = [
        CrewMember(
            member_id="CM010",
            name="Bob Brown",
            rank=Rank.cadet,
            age=22,
            specialization="Piloting",
            years_experience=1,
        ),
    ]

    try:
        SpaceMission(
            mission_id="M2024_BAD",
            mission_name="Doomed Mission",
            destination="Venus",
            launch_date="2024-07-01T09:00:00",
            duration_days=180,
            crew=invalid_crew,
            budget_millions=500.0,
        )
    except ValidationError as e:
        print("Expected validation error:")
        for error in e.errors():
            msg = error.get("ctx", {}).get("error", error["msg"])
            print(msg)


if __name__ == "__main__":
    main()
