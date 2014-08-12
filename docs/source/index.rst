Welcome to k-means algorithm documentation!
===========================================
| This algorithm implements the k-means algorithm using the RADICAL PILOT API.
| RADICAL-Pilot needs Python >= 2.6. All dependencies are installed automatically by the installer. Besides that, RADICAL-Pilot needs access to a MongoDB database that is reachable from the internet. User groups within the same institution or project can share a single MongoDB instance.
|
Hands-on Job Sumbimission:
^^^^^^^^^^^^^^^^^^^^^^^^^^
In order to make this example work, we need first to  install the following:::

	virtualenv $HOME/myenv
	source $HOME/myenv/bin/activate

Install Radical-Pilot API::
	
	pip install radical.pilot:

Install MondoDB (only if you want to run locally):

	Linux Users::

		apt-get -y install scons libssl-dev libboost-filesystem-dev libboost-program-options-dev libboost-system-dev libboost-thread-dev
		git clone -b r2.6.3 https://github.com/mongodb/mongo.git
		cd mongo
		scons --64 --ssl all
		scons --64 --ssl --prefix=/usr install

	Mac Users::

		brew install mongodb
		mkdir -p /data/db
		chmod 755 /data/db
		mongod


Finally, you need to download the source files of k-means algorithm::
	
	curl -O https://raw.githubusercontent.com/georgeha/k-means-algorithm/master/k-means.py

	curl -O https://raw.githubusercontent.com/georgeha/k-means-algorithm/master/clustering_the_elements.py

	curl -O https://raw.githubusercontent.com/georgeha/k-means-algorithm/master/finding_new_centroids.py

	curl -O https://raw.githubusercontent.com/georgeha/k-means-algorithm/master/dataset2.data



Run the Code:
^^^^^^^^^^^^^

To give it a test drive try via command line the following command::
	
	python k-means.py 3

where 3 is the number of clusters the user wants to create.


More About this algorithm:
^^^^^^^^^^^^^^^^^^^^^^^^^^
This algorithm creates the clusters of the elements found in the dataset2.data file. You can create your own file or create a new dataset 
file using the following generator::
	
	curl -O https://raw.githubusercontent.com/georgeha/k-means-algorithm/master/creating_dataset.py

run via command line::

	python creating_dataset.py (number_of_elements)

The algorithm takes the elements from the dataset2.data file. Then, it chooses the first k centroids using the
quickselect algorithm. 
It divides into number_of_cores files the initial file and pass each file as an argument to each Compute Unit.
Every Compute Unit return the elements into the correct centroid_cu_k.data file and then it composes the files into 
k centroid_k.data files. In order to find the new centroids, we  pass each centroid_k file as an argument to each Compute 
Unit, and in every compute unit the calculate the new centroids. If we have convergence we stop the algorithm, otherwise
we start a new iteration.

.. toctree::
   :maxdepth: 2



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

