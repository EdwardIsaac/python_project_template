import json
import anybadge


# Define thresholds: <2=red, <4=orange <8=yellow <10=green
thresholds = {30: 'red',
              50: 'orange',
              70: 'yellow',
              90: 'green'}

f = open("./coverage.json")
data = json.load(f)
percent = data["totals"]["percent_covered_display"]
#print(f'percent=[{percent}]')
#print(json.dumps(data, indent=3))
badge = anybadge.Badge('coverage',percent, thresholds=thresholds)
badge.write_badge('./coverage.svg', overwrite=True)
