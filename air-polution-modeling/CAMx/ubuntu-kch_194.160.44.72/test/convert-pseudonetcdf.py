#
#  Barron H. Henderson, Ph.D.
#   barronh.com; 352-682-3579
#
# coding: utf-8
#

import PseudoNetCDF as pnc

rawf = pnc.pncopen('testin.nc', format='ioapi')

f = rawf.renameDimensions(TSTEP='time', LAY='layer', ROW='Y', COL='X')

f.createVariable(
    'Lambert_Conformal', 'i', (),
    grid_mapping_name="lambert_conformal_conic",
    standard_parallel = [rawf.P_ALP, rawf.P_BET],
    longitude_of_central_meridian = rawf.XCENT,
    latitude_of_projection_origin = rawf.YCENT,
)

timev = f.createVariable(
    'time', 'd', ('time',),
    long_name = 'time',
    units='hours since 1970-01-01 00:00:00+0000',
)
f.variables['time'][:] = f.date2num(rawf.getTimes())

for key, var in f.variables.items():
    if var.dimensions[-2:] == ('Y', 'X'):
        var.grid_mapping = "Lambert_Conformal"


f.variables['latitude'].units = 'degrees_north'
f.variables['longitude'].units = 'degrees_east'

f.Conventions = 'CF-1.6'
f.save('testout.nc')


