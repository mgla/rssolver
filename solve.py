#!/usr/bin/python3

appointments = [
    {
        "_comment": "Korrosion kermaischer Werkstoffe",
        "monday" : [range(830, 1530)],
        "wednesday" : [range(1815, 1930)]
    },
    {
        "_comment" : "Kommunikative Usability",
        "monday" : [range(1215, 1330)],
        "thursday" : [range(1015, 1130)]
    },
    {
        "_comment" : "Werkstoffkunde der hochtemp",
        "monday" : [range(1500, 1745)],
        "tuesday" : [range(1615, 1730)],
        "friday" : [range(1000, 1115)],
    }
]

results = []

for a in range(len(appointments)):
    for b in range(a + 1, len(appointments)):
        for c in range(b + 1, len(appointments)):
            print("plan: %s, %s, %s" %(a,b,c))
            if ( a == b or b == c or c == a ):
                print("skip")
                break
            # try to place
            no_fit = False
            days = ["monday", "tuesday", "wednesday", "thursday", "friday"]
            plan = {}
            for day in days:
                print("%s: fit '%s'" % (day, appointments[a]["_comment"]))
                plan[day] = []
                for app in [a, b, c]:
                    for item in appointments[app][day]:
                        xs = set(plan[day])
                        if not len(xs.intersection(appointments[app][day])):
                            no_fit = True
                            break
                        plan[day] += appointments[app][day]
                if no_fit:
                    break
            if no_fit:
                print("plan invalid")
                break
            # if we arrived here, no collisions found
            print("Found valid plan")
            results += plan




    # take three out of n
