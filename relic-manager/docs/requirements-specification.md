# Software requirements specification

## Purpose

This software allows users to manage, sort, score, etc. relics from the gacha game *Honkai: Star Rail*. The user may create different profiles, i.e. to separate relics from multiple game accounts.

Relics each have a *set* and a *type*. Each relic has one *main stat* determined by the type, and up to 4 different *sub stats*. Relics may be enhanced up to level 15. Each level increments the main stat by a predetermined amount, and every 3 levels increments one random sub stat by a set amount. Scoring prioritizes relics with high **crit rate/damage** and **speed** stats, as well as **attack** slightly less.

## Functionality

- The user can choose which profile to use
- The user sees a list of all added relics
  - This list may be sorted and filtered by various parameters
- The program will calculate a score for each added relic based on their stats
- The user can add relics to the database
- The user can modify existing relics to update their stats
- The user can remove relics from the database
