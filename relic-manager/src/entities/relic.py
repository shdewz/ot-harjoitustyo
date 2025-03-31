class Relic:
    def __init__(self, relic_id, relic_set, relic_type, level, mainstat, substats):
        """Relic constructor.

        Args:
            relic_set: Relic set name
            relic_type: Relic type (head, hands, body, feet, ball, rope)
            level: Relic level (integer, 1-15)
            mainstat: Mainstat type (hp, atk, hp%, atk%, def%, ehr, healing, crate, cdmg, spd, physical, fire, ice, wind, lightning, quantum, imaginary, be, err)
            substats: array of substat type-value pairs:
                type: (hp, hp%, atk, atk%, def, spd, crate, cdmg, ehr, be, effres)
        """

        self.id = relic_id
        self.relic_set = relic_set
        self.relic_type = relic_type
        self.level = level
        self.mainstat = mainstat
        self.substats = substats