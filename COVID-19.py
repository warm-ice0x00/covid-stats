from datetime import datetime

import numpy
import pandas as pd
from matplotlib import pyplot

cases = pd.read_csv("https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data"
                    "/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv")
rateDict = {}
fig, ax = pyplot.subplots(figsize=(11.85, 6.66))

# Australia
casesByRegion = cases[(cases["Country/Region"] == "Australia")]
rateDict["Australia"] = (casesByRegion[casesByRegion.columns[-1]].sum() - casesByRegion[
    casesByRegion.columns[-15]].sum()) / 25788217
# Belgium
casesByRegion = cases[(cases["Country/Region"] == "Belgium") & cases["Province/State"].isnull()]
rateDict["Belgium"] = (casesByRegion[casesByRegion.columns[-1]] - casesByRegion[
    casesByRegion.columns[-15]]).sum() / 11632334
# Canada
casesByRegion = cases[(cases["Country/Region"] == "Canada")]
rateDict["Canada"] = (casesByRegion[casesByRegion.columns[-1]].sum() - casesByRegion[
    casesByRegion.columns[-15]].sum()) / 38067913
# China
casesByRegion = cases[cases["Country/Region"].isin(["China", "Taiwan*"])]
rateDict["China"] = (casesByRegion[casesByRegion.columns[-1]].sum() - casesByRegion[
    casesByRegion.columns[-15]].sum()) / 1476282301
# Denmark
casesByRegion = cases[(cases["Country/Region"] == "Denmark") & cases["Province/State"].isnull()]
rateDict["Denmark"] = (casesByRegion[casesByRegion.columns[-1]] - casesByRegion[
    casesByRegion.columns[-15]]).sum() / 5813302
# France
casesByRegion = cases[(cases["Country/Region"] == "France")]
rateDict["France"] = (casesByRegion[casesByRegion.columns[-1]].sum() - casesByRegion[
    casesByRegion.columns[-15]].sum()) / 68325350
# Germany
casesByRegion = cases[(cases["Country/Region"] == "Germany") & cases["Province/State"].isnull()]
rateDict["Germany"] = (casesByRegion[casesByRegion.columns[-1]] - casesByRegion[
    casesByRegion.columns[-15]]).sum() / 83900471
# Japan
casesByRegion = cases[(cases["Country/Region"] == "Japan") & cases["Province/State"].isnull()]
rateDict["Japan"] = (casesByRegion[casesByRegion.columns[-1]] - casesByRegion[
    casesByRegion.columns[-15]]).sum() / 126050796
# Netherlands
casesByRegion = cases[(cases["Country/Region"] == "Netherlands")]
rateDict["Netherlands"] = (casesByRegion[casesByRegion.columns[-1]].sum() - casesByRegion[
    casesByRegion.columns[-15]].sum()) / 17514951
# Singapore
casesByRegion = cases[(cases["Country/Region"] == "Singapore") & cases["Province/State"].isnull()]
rateDict["Singapore"] = (casesByRegion[casesByRegion.columns[-1]] - casesByRegion[
    casesByRegion.columns[-15]]).sum() / 5896684
# Sweden
casesByRegion = cases[(cases["Country/Region"] == "Sweden") & cases["Province/State"].isnull()]
rateDict["Sweden"] = (casesByRegion[casesByRegion.columns[-1]] - casesByRegion[
    casesByRegion.columns[-15]]).sum() / 10160159
# Switzerland
casesByRegion = cases[(cases["Country/Region"] == "Switzerland") & cases["Province/State"].isnull()]
rateDict["Switzerland"] = (casesByRegion[casesByRegion.columns[-1]] - casesByRegion[
    casesByRegion.columns[-15]]).sum() / 8715494
# United Kingdom
casesByRegion = cases[(cases["Country/Region"] == "United Kingdom") & cases["Province/State"].isnull()]
rateDict["United Kingdom"] = (casesByRegion[casesByRegion.columns[-1]] - casesByRegion[
    casesByRegion.columns[-15]]).sum() / 68207114
# United States
casesByRegion = cases[(cases["Country/Region"] == "US") & cases["Province/State"].isnull()]
rateDict["United States"] = (casesByRegion[casesByRegion.columns[-1]] - casesByRegion[
    casesByRegion.columns[-15]]).sum() / 336130735
# World
rateDict["World"] = (cases[cases.columns[-1]].sum() - cases[cases.columns[-15]].sum()) / 7874965732

rateDict = dict(sorted(rateDict.items(), key=lambda item: item[1]))  # Sort by values
rateDict = {k: v * 100000 for (k, v) in rateDict.items()}
y_pos = numpy.arange(len(rateDict))
rects = ax.barh(y_pos, rateDict.values(), color="orange")
ax.axvline(x=25, color="red", linestyle="dashed", label="Threshold")
for rect in rects:
    width = rect.get_width()
    ax.annotate("%.1f" % width, xy=(width, rect.get_y() + rect.get_height() / 2), xytext=(3, 0),
                textcoords="offset points", ha="left", va="center")
ax.spines["right"].set_visible(False)
ax.spines["top"].set_visible(False)
ax.set_yticks(y_pos)
ax.set_yticklabels(rateDict.keys())
ax.set_title("Cases in Last 14 Days per 100,000 Population, " + datetime.utcnow().strftime("%Y-%m-%d"))
pyplot.legend(loc="best")
pyplot.savefig("COVID-19.png", dpi=300)
