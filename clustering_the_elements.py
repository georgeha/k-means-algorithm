__author__    = "George Chantzialexiou"
__copyright__ = "Copyright 2012-2013, The Pilot Program"
__license__   = "MIT"


import os, sys, math
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
        
    #----------------------READING THE CENTROIDS FILE-------------------------------#
        centroid = []
        data = open("centroidss.txt", "r")
        read_as_string_array = data.readline().split(',')
        centroid = map(float, read_as_string_array)
        data.close()
        #print centroid
    #--------------------END OF READING THE CENTROIDS FILE--------------------------#


    #-----------------READING THE CU FILE - WHICH IS THE ELEMENT FILE --------------#
        elements = []
        read_file = open('cu_%d.data' % cu, 'r')
        read_as_string_array = read_file.readline().split(',')
        elements = map(float, read_as_string_array)
        #print elements
    #--------------------END OF READING THE CU FILE---------------------------------#



    #-----------------START OF WRITING TO THE NEW FILES------------------------------#
        write_file = []
        for i in range(1,k+1):
            file_open = open('centroid_%d_%d.data' % (cu,i), 'w')
            write_file.append(file_open)

        # here we classify in which centroid each element belongs to and write it to the correct file.
        # The right element is the one that is closer to the centroid using the Euclidean distance function
        for i in range(0,len(elements)):
            El = get_distance(elements[i],0,centroid[0],0)   # i can change this because i only have one variable
            index = 0  # that means that this is the first centroid
            for j in range(1,k):
                El2 = get_distance(elements[i],0,centroid[j],0)
                if (El != min(El,El2)): 
                    index = j
                    El = El2  
            write_file[index].write(str(elements[i]))
            write_file[index].write(',')
    #-----------------END OF WRITING TO THENEW FILES------------------------------#

        for i in range(0,k):
            write_file[i].close() 

        sys.exit(0)