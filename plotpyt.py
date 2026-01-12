"""matplotlib.pyplot is a state-based interface to matplotlib. It provides an implicit, MATLAB-like, way of plotting. It also opens figures on your screen, and acts as the figure GUI manager.

pyplot is mainly intended for interactive plots and simple cases of programmatic plot generation:

    import numpy as np
    import matplotlib.pyplot as plt

    x = np.arange(0, 5, 0.1)
    y = np.sin(x)
    plt.plot(x, y)
The explicit object-oriented API is recommended for complex plots, though pyplot is still usually used to create the figure and often the axes in the figure. See .pyplot.figure, .pyplot.subplots, and .pyplot.subplot_mosaic to create figures, and Axes API </api/axes_api> for the plotting methods on an Axes:

    import numpy as np
    import matplotlib.pyplot as plt

    x = np.arange(0, 5, 0.1)
    y = np.sin(x)
    fig, ax = plt.subplots()
    ax.plot(x, y)
See api_interfaces for an explanation of the tradeoffs between the implicit and explicit interfaces.


"""
# import matplotlib.pyplot as pyplot
# BAR_WIDTH = 0.35
# teama_results = (60,75,56,62,58)
# teamb_results = (55,68,80,73,55)

# index_teama = (1,2,3,4,5)
# index_teamb = [i + BAR_WIDTH/2 for i in index_teama]

# ticks = [i + BAR_WIDTH /2 for i in index_teama]
# tick_labels = ('lab1','lab2','lab3','lab4','lab5')

# pyplot.bar(index_teama,teama_results,BAR_WIDTH,color='b')
# pyplot.bar(index_teamb,teamb_results,BAR_WIDTH,color='g')

# pyplot.xlabel('Labs')
# pyplot.ylabel('Scores')
# pyplot.title ('Scores by Lab')
# pyplot.xticks(ticks,tick_labels)
# pyplot.legend()

# pyplot.show()
# ================ line chart ==========
# import matplotlib.pyplot as plt
# x = [1, 2, 3, 4, 5]
# y = [10, 12, 5, 8, 3]
# plt.plot(x, y)
# plt.title('Line Chart')
# plt.xlabel('X_axis')
# plt.ylabel('Y_axis')
# plt.show()
# =============== pie chart ===============
# import matplotlib.pyplot as plt
# labels = ['Category A', 'Category B','Category C']
# sizes = [10, 45, 25]
# plt.pie(sizes, labels = labels, autopct = '%1.1f%%')
# plt.title = ('pie chart')
# plt.show()
# ========= Histogram =============
# import matplotlib.pyplot as plt
# import numpy as np
# data = np.random.randn(1000)
# plt.hist(data, bins=30, edgecolor='black')
# plt.title('Histogram')
# plt.xlabel('Values')
# plt.ylabel('Frequency')
# plt.show()
# ========== Scatter plot ======= 
# import matplotlib.pyplot as plt
# import numpy as np

# x = np.random.rand(50)
# y = 2*x + 1 + 0.1 *np.random.rand(50)

# plt.scatter(x,y)
# plt.title('Scatter Plot')
# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')
# plt.show()
# ========== box plot =====
# from matplotlib import pyplot as plt
# import seaborn as sns
# import numpy as np
# data = [np.random.normal(0, std, 100) for std in range(1,4)]
# sns.boxplot(data = data)
# plt.title('Box Plot')
# plt.xlabel('Category')
# plt.ylabel('Values')
# plt.show()
# ========== violin plot ==========
# import matplotlib.pyplot as plt
# import seaborn as sns
# import numpy as np
# data =[np.random.normal(0, std, 100) for std in range(1, 4)]
# sns.violinplot(data=data)
# plt.title('violin plot')
# plt.xlabel('Category')
# plt.ylabel('Values')
# plt.show()
# ======== Heatmap ==========
# import matplotlib.pyplot as plt
# import seaborn as sns 
# import numpy as np
# data = np.random.rand(15,15)
# sns.heatmap(data, annot=True)
# plt.title('Heatmap')
# plt.show()
# ======== Area Chart ========
# import matplotlib.pyplot as plt
# x = [1,2,3,4,5]
# y1 = [10,15,25,30,35]
# y2 = [5,10,20,25,30]

# plt.fill_between(x, y1, y2, color = 'skyblue',alpha=0.4)
# plt.title('area chart')
# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')
# plt.show()
# ======= radar chart =======
# import matplotlib.pyplot as plt 
# import numpy as np
# labels = np.array (['A','B','C','D','E'])
# data = np.array([4,5,3,4,2])
# angles = np.linspace(0, 2 * np.pi, len(labels),endpoint=False)
# data = np.concatenate(((data, [data[0]])))
# angles = np.concatenate((angles, [angles[0]]))

# plt.polar(angles, data, marker='o')
# plt.fill(angles,data, alpha=0.25)
# plt.title('Radar Chart')
# plt.show()
# ======== coloured bar graph using matplotlib in python ====
# import matplotlib.pyplot as pyplot
# #set up the data
# labels = ('python', 'scala', 'c#', 'java','PHP')
# index =(1,2,3,4,5)#provide locations on x axis
# sizes = [45,10,15,30,32]
# #set up the bar chart
# pyplot.bar (index,sizes,tick_label=labels, color=('red', 'green', 'blue', 'yellow', 'orange'))
# #configure the layout 
# pyplot.ylabel('Usage')
# pyplot.xlabel('Programming Language')
# #  display the chart 
# pyplot.show()
# # clcoding.com
#============ stacked bar graph using matplotlib in python ======
import matplotlib.pyplot as pyplot
# set up the data 
labels = ('python', 'Scala', 'c#', 'java', 'PHP')
index = (1,2,3,4,5)
web_usage = [20, 2, 5, 10, 14]
data_science_usage = [15, 8, 5, 15,2]
games_usage =[10, 1, 5, 5, 4]
# set up the bar chart
pyplot.bar(index, web_usage, tick_label=labels,label='web' )
pyplot.bar(index, data_science_usage, tick_label=labels, label = 'data science',bottom=web_usage)
web_and_games_usage = [web_usage[i] + data_science_usage[i] for i in range(0, len(web_usage))]
pyplot.bar(index,games_usage,tick_label=labels,label='games',bottom=web_and_games_usage)
#configure the layout
pyplot.ylabel('Usage')
pyplot.xlabel('programming languages')
pyplot.legend()
pyplot.show()
