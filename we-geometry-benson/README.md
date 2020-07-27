# Neurohackademy 2020: Introduction to the Structure and Geometry of the Human Brain

**Author**: Noah C. Benson &lt;[nben@uw.edu](mailto:nben@uw.edu)&gt;

This github repository encodes a tutorial on the geometry of the
human brain, and how we represent data in the context of brain structure.
This tutorial was written for the 2020 Neurohackademy summer course at 
the University of Washington.

The tutorial is a notebook (`class-tutorial.ipynb` in this repository) that
can be executed inside of a [docker](https://docker.com/) container. In order to
run this tutorial, you will need to have docker installed. Optionally, if you want
to examine a Human Connectome Project (HCP) subject instead of a FreeSurfer subject,
see the section ["Getting HCP Credentials" section](#credentials), below.

To run the tutorial, make sure that your local port 8888 is free, then perform
the following:

```bash
# In bash:
# Clone the repository
> git clone https://github.com/noahbenson/neurohackademy2020
...
> cd neurohackademy2020
# Start the jupyter notebook server by bringing up the docker
> docker-compose up
```

This last command should produce a large amount of output as the docker container is built
and started. Once it has started, it should finish by printing a web address that looks
somethin like the following:

```
...
Attaching to neurohackademy2020
neurohackademy2020    | Executing the command: jupyter notebook
neurohackademy2020    | [I 22:28:43.171 NotebookApp] Writing notebook server cookie secret to /home/jovyan/.local/share/jupyter/runtime/notebook_cookie_secret
neurohackademy2020    | [I 22:28:44.106 NotebookApp] JupyterLab extension loaded from /opt/conda/lib/python3.7/site-packages/jupyterlab
neurohackademy2020    | [I 22:28:44.106 NotebookApp] JupyterLab application directory is /opt/conda/share/jupyter/lab
neurohackademy2020    | [I 22:28:44.109 NotebookApp] Serving notebooks from local directory: /home/jovyan
neurohackademy2020    | [I 22:28:44.110 NotebookApp] The Jupyter Notebook is running at:
neurohackademy2020    | [I 22:28:44.110 NotebookApp] http://(58e2ccd31ba9 or 127.0.0.1):8888/?token=e2f1bd8b37c875799a77198bc240af1b32e1ebc967e04801
neurohackademy2020    | [I 22:28:44.110 NotebookApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
neurohackademy2020    | [C 22:28:44.116 NotebookApp]
neurohackademy2020    |
neurohackademy2020    |     To access the notebook, open this file in a browser:
neurohackademy2020    |         file:///home/jovyan/.local/share/jupyter/runtime/nbserver-7-open.html
neurohackademy2020    |     Or copy and paste one of these URLs:
neurohackademy2020    |         http://(58e2ccd31ba9 or 127.0.0.1):8888/?token=e2f1bd8b37c875799a77198bc240af1b32e1ebc967e04801
```

This final line is telling you how to connect to the notebook server. Basically, copy
everything starting with the "`:8888/`" to the end of the line and paste it into your
browser after "`localhost`", so in this case, you would point your browser to
`localhost:8888/?token=e2f1bd8b37c875799a77198bc240af1b32e1ebc967e04801`. This should
connect you to the notebook server. Click on the `work` directory then on the
`class-notebook.ipynb` file to open the notebook. From there, follow the text and
code in the notebook.

If you want to be able to connect to the HCP dataset, you will need to run the following
in `bash` prior to running `docker-compose`:

```bash
# OPTIONAL: If you want to connect to the HCP dataset, run these lines prior
# to running `docker-compose up`.
# Export our HCP credentials; if you have credentials in a file:
> export HCP_CREDENTIALS="`cat ~/.hcp-passwd`"
# If you just have them as a key and secret:
> export HCP_CREDENTIALS="<key>:<secret>"
```


### <a name="credentials"></a> Getting HCP Credentials


set of Amazon S3 credentials from the HCP. To obtain these credentials, visit
their [database site](https://db.humanconnectome.org/), register for the site,
then request Amazon S3 credentials for the 1200 subject release (see the
 below for detailed
instructions).

Neuropythy uses Amazon's S3 service to obtain structural data from the HCP,
which hosts mosts of its public data there. In order to access these data, you
must obtain a set of S3 credentials from the HCP with access to their S3
buckets. To obtain these credentials, follow these instructions:

1. Point your browser to https://db.humanconnectome.org/ --this should load a
   login page with the title "Access HCP Data Releases"
2. Click the "Register" button in the lower right of the "Create an Account"
   section.
3. Fill out the dialog box that pops up and click "Register". You should get
   a verification email; follow any instructions that it contains.
4. You should now be able to go back to https://db.humanconnectome.org/ and
   log in.
5. Once you have logged in, you should see a page titled "Public Connectome
   Data" with a number of cards below it. The top card should be titled
   "WU-Minn HCP Data - 1200 Subjects" Within this card should be a bunch of
   text describing the dataset and some statistics about it. Near the bottom
   of the card is the word "ACCESS:" followed by a button labeled "Data Use
   Terms Required". Click this button and accept the terms of use that
   appear.
6. The "ACCESS:" tag should now be next to a checkmark and a link labeled
   "Open Access Terms Accepted". Just to the right of this link should be a
   button with the Amazon AWS logo (three yellow cubes) that says something
   about Amazon S3 access. Click this button to bring up the AWS Connection
   Manager dialog; it should have a large button that lets you generate an
   AWS Access Key and Secret. Click this button and follow the instructions
   if any.
7. The access key and secret should look something like this:  
   Key: AKAIG8RT71SWARPYUFUS  
   Secret: TJ/9SJF+AF3J619FA+FAE83+AF3318SXN/K31JB19J4  
   (These are not real credentials).  
   Copy the key and secret and paste them into a file in your home
   directory that you can remember. I recommend using ~/.hcp-passwd, as that
   is the file I will assume you have placed your credentials in during my
   tutorial. When you paste the key and secret into the file, separate them
   by a colon (:) character. For the fake key and secret given above, the
   file would contain the following:  
   AKAIG8RT71SWARPYUFUS:TJ/9SJF+AF3J619FA+FAE83+AF3318SXN/K31JB19J4

For eneral information on configuring neuropythy, including how to setup the HCP
auto-downloading mechanism, see the [neuropythy configuration wiki
page](https://github.com/noahbenson/neuropythy/wiki/Configuration).

### License 

This README file is part of the neurohackademy 2020 tutorial.

This tutorial is free software: you can redistribute it and/or Modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation, either version 3 of the License, or (at your option) any later
version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
PARTICULAR PURPOSE.  See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with
this program.  If not, see <http://www.gnu.org/licenses/>.

