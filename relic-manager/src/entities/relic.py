import math

relic_mainstats = {
    # (full name, initial, per-level)
    # from https://honkai-star-rail.fandom.com/wiki/Relic/Stats#Main_Stat_Values
    "SPD": ("Speed", 4.032, 1.4),
    "HP": ("HP", 112.896, 39.5136),
    "HP%": ("HP%", 6.912, 2.4192),
    "ATK": ("ATK", 56.448, 19.7568),
    "ATK%": ("ATK%", 6.912, 2.4192),
    "DEF%": ("DEF%", 8.64, 3.024),
    "BE%": ("Break Effect", 10.368, 3.6277),
    "EHR%": ("Effect Hit Rate", 6.912, 2.4192),
    "ERR%": ("Energy Recharge Rate", 3.1104, 1.0886),
    "OHB%": ("Overall Healing Bonus", 5.5296, 1.9354),
    "ELEM%": ("Elemental Damage", 6.2208, 2.1773),
    "CRATE%": ("Crit Rate", 5.184, 1.8144),
    "CDMG%": ("Crit Damage", 10.368, 3.6288),
}

relic_substats = {
    # (full name, low, mid, high, weight) rolls of substats; 1 roll per 3 levels
    "SPD": ("Speed", 2, 2.3, 2.6, 1),
    "HP": ("HP", 33.87, 38.103755, 42.33751, 0.25),
    "HP%": ("HP%", 3.456, 3.888, 4.32, 0.25),
    "ATK": ("ATK", 16.935, 19.051877, 21.168754, 0.75),
    "ATK%": ("ATK%", 3.456, 3.888, 4.32, 0.75),
    "DEF": ("DEF", 33.87, 38.103755, 42.33751, 0.25),
    "DEF%": ("DEF%", 4.32, 4.86, 5.4, 0.25),
    "BE%": ("Break Effect", 5.184, 5.832, 6.48, 0.25),
    "EHR%": ("Effect Hit Rate", 3.456, 3.888, 4.32, 0.25),
    "RES%": ("Effect RES", 3.456, 3.888, 4.32, 0.25),
    "CRATE%": ("Crit Rate", 2.592, 2.916, 3.24, 1),
    "CDMG%": ("Crit Damage", 5.184, 5.832, 6.48, 1),
}

relic_types = {
    # 0 = standard, 1 = planar; for set separation
    "Head": 0,
    "Hands": 0,
    "Body": 0,
    "Feet": 0,
    "Ball": 1,
    "Rope": 1
}

relic_sets = {
    # 0 = standard, 1 = planar; for type separation
    "Band of Sizzling Thunder": 0,
    "Champion of Streetwise Boxing": 0,
    "Eagle of Twilight Line": 0,
    "Firesmith of Lava-Forging": 0,
    "Genius of Brilliant Stars": 0,
    "Guard of Wuthering Snow": 0,
    "Hero of Triumphant Song": 0,
    "Hunter of Glacial Forest": 0,
    "Iron Cavalry Against the Scourge": 0,
    "Knight of Purity Palace": 0,
    "Longevous Disciple": 0,
    "Messenger Traversing Hackerspace": 0,
    "Musketeer of Wild Wheat": 0,
    "Passerby of Wandering Cloud": 0,
    "Pioneer Diver of Dead Waters": 0,
    "Poet of Mourning Collapse": 0,
    "Prisoner in Deep Confinement": 0,
    "Sacerdos' Relived Ordeal": 0,
    "Scholar Lost in Erudition": 0,
    "The Ashblazing Grand Duke": 0,
    "The Wind-Soaring Valorous": 0,
    "Thief of Shooting Meteor": 0,
    "Wastelander of Banditry Desert": 0,
    "Watchmaker, Master of Dream Machinations": 0,
    "Belobog of the Architects": 1,
    "Bone Collection's Serene Demesne": 1,
    "Broken Keel": 1,
    "Celestial Differentiator": 1,
    "Duran, Dynasty of Running Wolves": 1,
    "Firmament Frontline: Glamoth": 1,
    "Fleet of the Ageless": 1,
    "Forge of the Kalpagni Lantern": 1,
    "Giant Tree of Rapt Brooding": 1,
    "Inert Salsotto": 1,
    "Izumo Gensei and Takama Divine Realm": 1,
    "Lushaka, the Sunken Seas": 1,
    "Pan-Cosmic Commercial Enterprise": 1,
    "Penacony, Land of the Dreams": 1,
    "Rutilant Arena": 1,
    "Sigonia, the Unclaimed Desolation": 1,
    "Space Sealing Station": 1,
    "Sprightly Vonwacq": 1,
    "Talia: Kingdom of Banditry": 1,
    "The Wondrous BananAmusement Park": 1
}

relic_grades = ["F", "D", "C", "B", "A", "S", "SS", "SSS"]

class Relic:
    def __init__(self, relic_id, relic_set, relic_type, level, mainstat, substats):
        """Relic constructor.

        Args:
            relic_set: Relic set name
            relic_type: Relic type (head, hands, body, feet, ball, rope)
            level: Relic level (integer, 1-15)
            mainstat: Mainstat type (
                                    hp, atk, hp%, atk%, def%, ehr%, ohb%, crate%, cdmg%, spd,
                                    physical, fire, ice, wind, lightning, quantum, imaginary,
                                    be%, err%
                                    )
            substats: array of substat type-value pairs:
                type: (hp, hp%, atk, atk%, def, def%, spd, crate%, cdmg%, ehr%, be%, res%)
        """

        self.relic_id = relic_id
        self.relic_set = relic_set
        self.relic_type = relic_type
        self.level = level
        self.mainstat = mainstat
        mainstat_stats = relic_mainstats[self.mainstat]
        self.mainstat_value = mainstat_stats[1] + self.level * mainstat_stats[2]
        self.substats = substats
        self.score = self._calculate_score()

    def _calculate_score(self):
        """Calculates a score for the relic based on main and substats.

        Stats are normalized against the value of Crit DMG (64.8) at level 15
        and assigned a weight based on importance, with Crit, ATK and SPD prioritized.
        A letter grade is assigned in increments of 5 score.
        
        Returns:
            Returns a string score for the relic including the letter grade
        """

        substat_score = 0
        for substat in self.substats:
            reference_stat = (relic_mainstats["HP"] if substat[0] == "DEF"
                              else relic_mainstats["EHR%"] if substat[0] == "RES%"
                              else relic_mainstats[substat[0]])
            normalization = 64.8 / (reference_stat[1] + 15 * reference_stat[2])
            weight = relic_substats[substat[0]][4]
            score = normalization * weight * substat[1]
            substat_score += score

        grade_score = relic_grades[min(math.floor(substat_score / 5) - 1, 7)]

        return f"{math.floor(substat_score)} ({grade_score})"
