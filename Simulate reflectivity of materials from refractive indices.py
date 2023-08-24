import csv
import math
import statistics
import numpy as np
from matplotlib import pyplot as plt

refractive_index_path = 'C:/Users/fhan/Desktop/Reflectivity Simulation\Refractive index.csv'
with open(refractive_index_path, 'r') as csvfile:
    reader = csv.reader(csvfile)
    reader_rows = [row for row in reader]
i = 0
while True:
    if reader_rows[i][0] == '700':
        row_700 = i
    elif reader_rows[i][0] == '350':
        row_350 = i
        break
    i +=1
wavelength = [float(reader_rows[i][0]) for i in range(row_700,row_350+1)]
refractive_index = [float(reader_rows[i][1]) for i in range(row_700,row_350+1)]

air_refractive_index = [1]*351

AOI = np.linspace(0,90,901)

reflectivity_S = []
reflectivity_P = []
for theta in AOI:
    reflectivity_S_elememnt = list(abs((np.array(air_refractive_index)*math.cos(math.pi*theta/180)-np.array(refractive_index)*(1-(np.array(air_refractive_index)/np.array(refractive_index)*math.sin(math.pi*theta/180))**2)**0.5)/(np.array(air_refractive_index)*math.cos(math.pi*theta/180)+np.array(refractive_index)*(1-(np.array(air_refractive_index)/np.array(refractive_index)*math.sin(math.pi*theta/180))**2)**0.5))**2)
    reflectivity_S.append(reflectivity_S_elememnt)
    reflectivity_P_elememnt = list(abs((np.array(air_refractive_index)*(1-(np.array(air_refractive_index)/np.array(refractive_index)*math.sin(math.pi*theta/180))**2)**0.5-np.array(refractive_index)*math.cos(math.pi*theta/180))/(np.array(air_refractive_index)*(1-(np.array(air_refractive_index)/np.array(refractive_index)*math.sin(math.pi*theta/180))**2)**0.5+np.array(refractive_index)*math.cos(math.pi*theta/180)))**2)
    reflectivity_P.append(reflectivity_P_elememnt)    

r_S_blue = []
r_S_green = []
r_S_red = []
r_P_blue = []
r_P_green = []
r_P_red = []
for i in range(0,len(AOI)):
    wavelength_blue = []
    reflectivity_S_blue = []
    reflectivity_P_blue = []
    wavelength_green = []
    reflectivity_S_green = []
    reflectivity_P_green = []
    wavelength_red = []
    reflectivity_S_red = []
    reflectivity_P_red = []
    for j in range(0, len(wavelength)):
        if 610 <= wavelength[j] <= 630:
            wavelength_red.append(wavelength[j])
            reflectivity_S_red.append(reflectivity_S[i][j])
            reflectivity_P_red.append(reflectivity_P[i][j])
        elif 505 <= wavelength[j] <= 535:
            wavelength_green.append(wavelength[j])
            reflectivity_S_green.append(reflectivity_S[i][j])
            reflectivity_P_green.append(reflectivity_P[i][j])
        elif 450 <= wavelength[j] <= 470:
            wavelength_blue.append(wavelength[j])
            reflectivity_S_blue.append(reflectivity_S[i][j])
            reflectivity_P_blue.append(reflectivity_P[i][j])
    r_S_blue.append(statistics.mean(reflectivity_S_blue))
    r_P_blue.append(statistics.mean(reflectivity_P_blue))
    r_S_green.append(statistics.mean(reflectivity_S_green))
    r_P_green.append(statistics.mean(reflectivity_P_green))
    r_S_red.append(statistics.mean(reflectivity_S_red))
    r_P_red.append(statistics.mean(reflectivity_P_red))

plt.plot(AOI,r_S_blue,color='blue',linewidth=1.0,label='S-polarized')
plt.plot(AOI,r_S_green,color='green',linewidth=1.0,label='S-polarized')
plt.plot(AOI,r_S_red,color='red',linewidth=1.0,label='S-polarized')
plt.plot(AOI,r_P_blue,color='blue',linestyle='dashed',linewidth=1.0,label='P-polarized')
plt.plot(AOI,r_P_green,color='green',linestyle='dashed',linewidth=1.0,label='P-polarized')
plt.plot(AOI,r_P_red,color='red',linestyle='dashed',linewidth=1.0,label='P-polarized')
plt.title('Reflectivity for S- and P-polarized lights')
plt.xlim(0,90)
plt.ylim(0,1)
plt.xlabel('AOI')
plt.ylabel('Reflectivity, r')
plt.legend()
plt.grid()
plt.show()