import plotly.express as px
import pandas as pd
import numpy as np
from collections import namedtuple
import sympy as sp


n = sp.Symbol('n')
a = sp.Symbol('a')
b = sp.Symbol('b')



position = [2*n-n**2,0*n,-.5*7*n**2+2]
print("Position:", position)


scale = 0.1

nums = [i * scale for i in range(0, int(1 / scale), 1)]


df = pd.DataFrame({
    "n": np.array(nums, dtype="float32"),
	"x": np.array([position[0].subs(n, i) for i in nums], dtype="float32"),
	"y": np.array([position[1].subs(n, i) for i in nums], dtype="float32"),
	"z": np.array([position[2].subs(n, i) for i in nums], dtype="float32"),
})


print(df)
fig = px.line_3d(df, x="x", y="y", z="z", hover_data="n")
fig.show()




input()