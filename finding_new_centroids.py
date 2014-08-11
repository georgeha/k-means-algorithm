__author__    = "George Chantzialexiou"
__copyright__ = "Copyright 2012-2013, The Pilot Program"
__license__   = "MIT"


import os, sys,  math #, multiprocessing
from random import randint



def get_distance(dataPointX, dataPointY, centroidX, centroidY):
    
    # Calculate Euclidean distance.
    return math.sqrt(math.pow((centroidY - dataPointY), 2) + math.pow((centroidX - dataPointX), 2))
#------------------------------------------------------------------------------
#

################################################################################
##

if __name__ == "__main__":
    
    args = sys.argv[1:]
    cu = int(sys.argv[1])
    k = int(sys.argv[2])
    p = int(sys.argv[3])  # number of processors
    
    if (cu != p):
        number_of_files = (k/p)
    else:
        number_of_files = k  - (cu-1)*(k/p) # the last CU has to control and the remainder files of centroids 
    # Every CU have to manage k/p files of centroids
    #this is the file i will write the Centroids of this cu
    input_file = open('new_centroids_cu_%d.data' % cu, 'w')

    # open the centroids file to read the data
    read_file = open('centroidss.txt', 'r')
    read_as_string_array = read_file.readline().split(',')
    #print read_as_string_array
    Centroids_as_float = map(float, read_as_string_array)
    #print 'centroids: %f ' % Centroids_as_float[1]


    for i in range(1,number_of_files+1):
        j = i + (k/p)*(cu-1)
        read_file = open('centroid_%d.data' % j, 'r')
        read_as_string_array = read_file.readline().split(',')
        #print 'read as string array: ' % read_as_string_array
        del read_as_string_array[len(read_as_string_array)-1]
        #print(read_as_string_array)
        elements = map(float, read_as_string_array)
        #print read_as_int_array
        # now we have at this array the elements of a centroid

        sum_elements = 0
        #for i in range(0,len(Centroids_as_float))
        elements.append(Centroids_as_float[i-1])  # the centroids..we only add the missing elements which is the centroid of the file
        a = len(elements)

        
        for l in range(0,a):
            sum_elements = sum_elements + elements[l]   
        # find the median of xs and ys
        
        sum_elements = sum_elements / a   # median element now
        x_dist = elements[0]
        # searching for the new centroid
        min_dist = get_distance(sum_elements,0,x_dist,0)
        for l in range(1,a):
            dist2 = get_distance(sum_elements,0,elements[l],0)
            if (min_dist > dist2):
                min_dist = dist2
                x_dist = elements[l]
        input_file.write(str(x_dist))
        input_file.write(',')
        read_file.close()
    
    input_file.close()
    
    sys.exit(0)