
Year= [2011,2012,2013,2014,2015,2016,2017,2018,2019,2020]
Duration = [103, 101, 99, 100, 100, 95, 95, 96, 93, 90]
movie_dict= {"years": Year, "duration":Duration}
print(movie_dict)

import pandas as pd
duration_df=pd.DataFrame(movie_dict)

import matplotlib.pyplot as plt
fig=plt.figure()

plt.plot(Year, Duration)
plt.title("Netflix Movie Duration 2011-2020")
plt.show()