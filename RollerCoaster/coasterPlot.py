import plotly.express as px
import pandas as pd
import numpy as np

df = pd.DataFrame({
    "n": np.array([1,2,3,4], dtype="int32"),
	"x": np.array([1,2,3,4], dtype="int32"),
	"y": np.array([1,3,2,4], dtype="int32"),
	"z": np.array([1,4,3,2], dtype="int32"),
})


print(df)
fig = px.line_3d(df, x="x", y="y", z="z", text="n")
fig.show()

input()