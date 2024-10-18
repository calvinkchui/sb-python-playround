import numpy as np

#Reproducibility
np.random.seed(1618033)

#Set 3 axis labels/dims
axis_1 = np.arange(2000,2010) #Years
axis_2 = np.arange(0,20) #Samples
axis_3 = np.array(["patient_%d" % i for i in range(0,3)]) #Patients

#Create random 3D array to simulate data from dims above
A_3D = np.random.random((years.size, samples.size, len(patients))) #(10, 20, 3)

#Create empty list to store 2D dataframes (axis_2=rows, axis_3=columns) along axis_1
list_of_dataframes=[]

#Iterate through all of the year indices
for i in range(axis_1.size):
    #Create dataframe of (samples, patients)
    DF_slice = pd.DataFrame(A_3D[i,:,:],index=axis_2,columns=axis_3)
    list_of_dataframes.append(DF_slice)
#     print(DF_slice) #preview of the 2D dataframes "slice" of the 3D array
#           patient_0  patient_1  patient_2
#      0    0.727753   0.154701   0.205916
#      1    0.796355   0.597207   0.897153
#      2    0.603955   0.469707   0.580368
#      3    0.365432   0.852758   0.293725
#      4    0.906906   0.355509   0.994513
#      5    0.576911   0.336848   0.265967
#     ...
#     19   0.583495   0.400417   0.020099

# DF_3D = pd.DataFrame(list_of_dataframes,index=axis_2, columns=axis_1)
# Error
# Shape of passed values is (1, 10), indices imply (10, 20)
