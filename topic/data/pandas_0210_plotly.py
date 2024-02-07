'''
pip install -U kaleido
'''
import pandas as pd
#import matplotlib.pyplot as plt
pd.options.plotting.backend = "plotly"

df = pd.DataFrame(dict(a=[1,3,2], b=[3,2,1]))
fig = df.plot(title="Pandas Backend Example" , #template="simple_white",
              labels=dict(index="time", value="money", variable="option"))
fig.update_yaxes(tickprefix="$")
#fig.show()
#fig.savefig("0210-plotly.png")
fig.write_image("0210-plotly.png")
#fig = plt.figure()