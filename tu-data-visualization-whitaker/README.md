# NH19-Visualization

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/KirstieJane/NH19-Visualization/master?urlpath=lab)

A collection of notebooks demonstrating plotting with matplotlib.

### Matplotlib and Seaborn Galleries

The greatest part of matplotlib and seaborn are their galleries:

* https://matplotlib.org/3.1.0/gallery/index.html
* https://seaborn.pydata.org/examples/index.html

If you take nothing else from this session, please know that there are amazing examples that you can copy and paste and run for yourself.

These give you a great jumping off point for learning how to visualize your data.

### Installation

Visualisation tools change quite regularly, so the first step is to install an anaconda environment with the correct packages.
Don't forget to type `y` when conda asks you if you want to install some packages :smiley_cat:

```
conda create -n nh19-visualization python=3.7 nb_conda_kernels jupyter
```

Activate that environment and then install all the packages listed in the [requirements.txt](requirements.txt) file in this repository.

*If you don't run this command from inside of the repository then change `requirements.txt` to include the path (relative or absolute) to the file.*

```
conda activate nh19-visualization
pip install -r requirements.txt
```

Finally, make sure you can see this environment in [jupyter lab](https://jupyterlab.readthedocs.io/en/stable/).

```
python -m ipykernel install --user --name nh19-visualization
```

### Step by step tutorial

In 2017 Michael Vendetti and I published a paper on *"Neuroscientific insights into the development of analogical reasoning"*.
The code to recreate the figures from processed data is available at https://github.com/KirstieJane/NORA_WhitakerVendetti_DevSci2017.

The [DataViz_Scatter](DataViz_Scatter.ipynb) jupyter notebook is a step by step tutorial to plot figure 2 (shown below) from the paper.

![](https://raw.githubusercontent.com/KirstieJane/NORA_WhitakerVendetti_DevSci2017/master/FIGURES/Figure2_lowres.png)

## Other example notebooks

* Tal's Visualization in Python tutorial from last year: https://github.com/neurohackademy/visualization-in-python/blob/master/visualization-in-python.ipynb
* Raincloudplots: https://github.com/RainCloudPlots/RainCloudPlots
  * [Binder link](https://mybinder.org/v2/gh/RainCloudPlots/RainCloudPlots/master?filepath=tutorial_python%2Fraincloud_tutorial_python.ipynb)
* The citation advantage of linking publications to research data:
 https://github.com/alan-turing-institute/das-public
   * [Binder link](https://mybinder.org/v2/gh/alan-turing-institute/das-public/master?filepath=notebooks%2FDescriptiveFigures.ipynb)