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


Edit the example:
^^^^^^^^^^^^^^^^^
|
|
|

.. toctree::
   :maxdepth: 2



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

