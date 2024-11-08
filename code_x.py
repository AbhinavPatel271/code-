import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.DataFrame( { "Force" : [ 9 , 21 , 32 , 38 , 52 , 60 , 73 , 79 , 91 , 102 ] ,
                       "Acceleration" : [ 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 ]
                      })
X = pd.DataFrame(data.Acceleration)
y = data.Force

model = LinearRegression()
model.fit( X , y )
mass = model.coef_[0]

sns.regplot( data=data , y = "Force" , x = "Acceleration" , scatter_kws={'color': 'blue'}, line_kws={'color': 'red'}) 
plt.title( f"Approximate Mass: slope of line = {mass:.2f}" )
plt.show()

 