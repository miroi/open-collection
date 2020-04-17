#!/usr/bin/python3

#
#  Barron H. Henderson, Ph.D.
#   barronh.com; 352-682-3579
#
# coding: utf-8
#

print("going to import PseudoNetCDF as pnc")
import PseudoNetCDF as pnc

print("going to open nc file ...")
rawf = pnc.pncopen('testin.nc', format='ioapi')

print("going to rename dimensions ...")
f = rawf.renameDimensions(TSTEP='time', LAY='layer', ROW='Y', COL='X')

print("going to create variable...")
f.createVariable(
    'Lambert_Conformal', 'i', (),
    grid_mapping_name="lambert_conformal_conic",
    standard_parallel = [rawf.P_ALP, rawf.P_BET],
    longitude_of_central_meridian = rawf.XCENT,
    latitude_of_projection_origin = rawf.YCENT,
)

print("setting timev...")

timev = f.createVariable(
    'time', 'd', ('time',),
    long_name = 'time',
    units='hours since 1970-01-01 00:00:00+0000',
)

print("doing f.date2num...")
f.variables['time'][:] = f.date2num(rawf.getTimes())

print("starting cycle...")
for key, var in f.variables.items():
    print("var=",var,"key=",key)
    if var.dimensions[-2:] == ('Y', 'X'):
        var.grid_mapping = "Lambert_Conformal"


f.variables['latitude'].units = 'degrees_north'
f.variables['longitude'].units = 'degrees_east'

f.Conventions = 'CF-1.6'


print("saving output file...")
f.save('testout.nc')

