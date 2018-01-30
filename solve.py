#!/usr/bin/python3
# -*- coding: utf-8 -*-

import logging

logging.basicConfig()
logger = logging.getLogger('rssolver')
logger.setLevel(logging.INFO)
#logger.setLevel(logging.DEBUG)
appointments = [
    {
        "name": "Korrosion keramischer Werkstoffe",
        "monday" : [range(830, 1130)],
        "wednesday" : [range(1815, 1930)]
    },
    {
        "name" : "Kommunikative Usability - Übung Montag",
        "monday" : [range(1215, 1530)],
    },
    {
        "name" : "Kommunikative Usability - Übung Donnerstag",
        "monday" : [range(1215, 1330)],
        "thursday" : [range(1015, 1130)]
    },
    {
        "name" : "Werkstoffkunde der Hochtemperatur",
        "monday" : [range(1500, 1745)],
        "tuesday" : [range(1615, 1730)],
        "friday" : [range(1000, 1115)],
    },
    {
        "name" : "Feuerfeste Werkstoffe",
        "monday" : [range(830, 945),range(1615,1730)],
        "tuesday": [range(830, 945)],
        "friday" : [range(1215, 1330)],
    },
    {
        "name" : "Technologie der Gusswerkstoffe",
        "tuesday": [range(1315, 1430)],
        "wednesday" : [range(800, 1145)],
    },
    {
        "name" : "Thermochemie mineralischer Werkstoffe",
        "tuesday" : [range(830, 1115), range(1215,1330)],
        "wednesday" : [range(1030, 1145)],
        "thursday" : [range(1000, 1115)],
    },
    {
        "name" : "Berechnung und Auslegung Industrieofen",
        "wednesday" : [range(830, 945)],
        "friday" : [range(1015, 1130)],
    }
]

results = []

for a in range(len(appointments)):
    for b in range(a + 1, len(appointments)):
        for c in range(b + 1, len(appointments)):
            logger.debug("plan: %s, %s, %s" %(a,b,c))
            if ( a == b or b == c or c == a ):
                logger.debug("skip")
                break
            # try to place
            no_fit = False
            days = ["monday", "tuesday", "wednesday", "thursday", "friday"]
            plan = {}
            for day in days:
                plan[day] = []
                for app in [a, b, c]:
                    try:
                        logger.debug("  %s: fit '%s'" % (day, appointments[app]["name"]))
                        for item in appointments[app][day]:
                            if no_fit:
                                break
                            xs = set(plan[day])
                            if len(xs.intersection(item)) is not 0:
                                logger.debug("    found appointment overlap")
                                no_fit = True
                                break
                            plan[day] += item
                    except:
                        pass # free time
                if no_fit:
                    break
            if no_fit:
                logger.debug("  plan invalid")
                break
            # if we arrived here, no collisions found
            logger.info("Found valid plan")
            for app in [a,b,c]:
                logger.info("  %s" % appointments[app]['name'])
            results += plan




    # take three out of n
