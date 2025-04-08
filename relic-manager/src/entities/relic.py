relic_mainstats = {
    # (initial, per-level)
    # from https://honkai-star-rail.fandom.com/wiki/Relic/Stats#Main_Stat_Values
    "SPD": (4.032, 1.4),
    "HP": (112.896, 39.5136),
    "HP%": (6.912, 2.4192),
    "ATK": (56.448, 19.7568),
    "ATK%": (6.912, 2.4192),
    "DEF%": (8.64, 3.024),
    "BE%": (10.368, 3.6277),
    "EHR%": (6.912, 2.4192),
    "ERR%": (3.1104, 1.0886),
    "OHB%": (5.5296, 1.9354),
    "ELEM%": (6.2208, 2.1773),
    "CRATE%": (5.184, 1.8144),
    "CDMG%": (10.368, 3.6288),
}

relic_substats = {
    # (low, mid, high) rolls of substats; 1 roll per 3 levels
    "SPD": (2, 2.3, 2.6),
    "HP": (33.87, 38.103755, 42.33751),
    "HP%": (3.456, 3.888, 4.32),
    "ATK": (16.935, 19.051877, 21.168754),
    "ATK%": (3.456, 3.888, 4.32),
    "DEF%": (4.32, 4.86, 5.4),
    "BE%": (5.184, 5.832, 6.48),
    "EHR%": (3.456, 3.888, 4.32),
    "RES%": (3.456, 3.888, 4.32),
    "CRATE%": (2.592, 2.916, 3.24),
    "CDMG%": (5.184, 5.832, 6.48),
}

class Relic:
    def __init__(self, id, relic_set, relic_type, level, mainstat, substats):
        """Relic constructor.

        Args:
            relic_set: Relic set name
            relic_type: Relic type (head, hands, body, feet, ball, rope)
            level: Relic level (integer, 1-15)
            mainstat: Mainstat type (
                                    hp, atk, hp%, atk%, def%, ehr, healing, crate, cdmg, spd,
                                    physical, fire, ice, wind, lightning, quantum, imaginary,
                                    be, err
                                    )
            substats: array of substat type-value pairs:
                type: (hp, hp%, atk, atk%, def, spd, crate, cdmg, ehr, be, effres)
        """

        self.id = id
        self.relic_set = relic_set
        self.relic_type = relic_type
        self.level = level
        self.mainstat = mainstat
        mainstat_stats = relic_mainstats[self.mainstat]
        self.mainstat_value = mainstat_stats[0] + self.level * mainstat_stats[1]
        self.substats = substats
