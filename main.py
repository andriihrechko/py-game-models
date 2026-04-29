import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        data = json.load(file)

    for key in data:
        race = data[key]["race"]
        skills = race["skills"]
        race, _ = Race.objects.get_or_create(
            name=race["name"],
            description=race["description"]
        )
        if skills is not None:
            for skill in skills:
                Skill.objects.get_or_create(
                    race=race,
                    **skill
                )
        guild = data[key]["guild"]
        if guild is not None:
            guild, _ = Guild.objects.get_or_create(
                name=guild["name"],
                description=guild["description"]
            )
        Player.objects.create(
            nickname=key,
            email=data[key]["email"],
            bio=data[key]["bio"],
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
