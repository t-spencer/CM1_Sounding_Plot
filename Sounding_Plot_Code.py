# -*- coding: utf-8 -*-
"""
Sounding_Plot_Code.py
Copyright (C) 2016 Trenton W. Spencer

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

   For full license, see <http://www.gnu.org/licenses/>.
"""
__author__ = 'Trenton Spencer'
__version__ = 2.0
__license__ = "GNU GPL v3"
"""
Created on Wed Nov 2 04:20:37 2016
@author: Trenton Spencer, TAMU Meteorology '17
Contact: trentspencer144@gmail.com
Latest version can be found on github at https://github.com/t-spencer/CM1_Sounding_Plot

This code requires installation of the netCDF4 and pymeteo packages. You may plot both types of 
sounding in the same execution by simply uncommenting both sets of lines (delete #)
"""
#-------------------------------------(Begin Code)--------------------------------------------------------------
"""
If you want to plot cm1 output soundings from the CM1 output data in netCDF format,
uncomment and edit these lines
"""
#input_filename1 = 'OriginalSounding.nc'
#output_filename1 = 'cm1_sounding'
#output_format1 = '.pdf'  # You can use .pdf , .jpg , or .png

'''
If you want to plot the input sounding (i.e. not output from cm1) following the required cm1 format,
uncomment and edit these lines
''' 
#input_filename2 = 'input_sounding'
#output_filename2 = 'test'
#output_format2 = '.pdf' # You can use .pdf , .jpg , or .png



'''
-----------------------------------------------------------------------------------------------------------------
Changes below this line should not be necessary
-----------------------------------------------------------------------------------------------------------------
'''

# Imports necessary packages
import pymeteo.skewt as skewt
import netCDF4 as nc
import matplotlib.pyplot as plt

class SoundingPlot:
    def __init__(self, input_filename, output_filename, output_format):
        self.filename = input_filename
        self.output = output_filename
        self.format = output_format
        
    def outputgen(self):
        '''Creates the output filename'''
        self.output_filename = self.output + self.format
    
    def ncplot(self):
        '''Plots the sounding from the netCDF4 ouput of CM1'''
        file = nc.Dataset(self.filename)
        qv = file['qv'][0,:,0,0]
        z = file['z'][:]
        th = file['th'][0,:,0,0]
        p = file['prs'][0,:,0,0]
        u = file['u'][0,:,0,0]
        v = file['v'][0,:,0,0]
        fig1 = plt.figure(figsize = (15,10))
        ax1 = fig1.add_subplot(111)
        skewt.plot_sounding_axes(ax1)
        skewt.plot_sounding(ax1, z, th, p, qv, u, v)
        skewt.plot_legend(ax1)
        fig1.savefig(self.output_filename)
        
    def inputplot(self):
        '''Plots the sounding from the standard format CM1 input sounding file'''
        plt.figure(figsize = (15,10))
        skewt.plot_sounding_data(self.filename, self.output_filename)

print('''\n CM1 Sounding Plot Program \n Author: Trent Spencer, TAMU Meteorology '17 \n \n Plotting Data...''')        
try:
    Sound1 = SoundingPlot(input_filename1, output_filename1, output_format1)
    Sound1.outputgen()
    Sound1.ncplot()
except:
    pass

try:
    Sound2 = SoundingPlot(input_filename2, output_filename2, output_format2)
    Sound2.outputgen()
    Sound2.inputplot()
except:
    pass
print('''\n Plotting Complete!''')
    