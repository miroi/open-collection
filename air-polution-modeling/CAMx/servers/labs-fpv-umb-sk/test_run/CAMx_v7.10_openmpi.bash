#!/bin/csh
#
# CAMx v7.10
#

###setenv NCPUS 8
###setenv OMP_NUM_THREADS 8
###setenv OMP_STACKSIZE 128M
limit stacksize unlimited

set EXEC      = "../../src/CAMx.v7.10.MPICH3.NCF4.pgf"
#
set RUN     = "v7.10.36.12"
set ICBC    = "../icbc"
set INPUT   = "../inputs"
set MET     = "../met"
set EMIS    = "../emiss"
set PTSRCE  = "../ptsrce"
set OUTPUT  = "../outputs"
#
mkdir -p $OUTPUT
#
#  --- Create the nodes file ---
#
cat << ieof > nodes
10.1.4.2:3
10.1.4.3:2
10.1.4.4:2
10.1.4.5:2
ieof
set NUMPROCS = 9
#
#  --- set the dates and times ----
#
set RESTART = "NO"
foreach today (10.162 11.163)
set JUL = $today:e
set CAL = $today:r
set CALDAY = 201606${CAL}
set YESTERDAY = `echo ${CALDAY} | awk '{printf("%d",$1-1)}'`
#
if( ${RESTART} == "NO" ) then
        set RESTART = "false"
else
        set RESTART = "true"
endif
#
#  --- Create the input file (always called CAMx.in)
#
cat << ieof > CAMx.in

 &CAMx_Control

 Run_Message      = 'CAMx 7.10 Test Problem -- CB6R4 CF SOAP $CALDAY',

!--- Model clock control ---

 Time_Zone        = 0,                 ! (0=UTC,5=EST,6=CST,7=MST,8=PST)
 Restart          = .${RESTART}.,
 Start_Date_Hour  = 2016,06,${CAL},0000,   ! (YYYY,MM,DD,HHmm)
 End_Date_Hour    = 2016,06,${CAL},2400,   ! (YYYY,MM,DD,HHmm)

 Maximum_Timestep    = 15.,            ! minutes
 Met_Input_Frequency = 60.,            ! minutes
 Ems_Input_Frequency = 60.,            ! minutes
 Output_Frequency    = 60.,            ! minutes

!--- Map projection parameters ---

 Map_Projection = 'LAMBERT',  ! (LAMBERT,POLAR,RPOLAR,MERCATOR,LATLON,UTM)
 UTM_Zone       = 0,
 Longitude_Pole = -97.,      ! deg (west<0,south<0)
 Latitude_Pole  =  40.,      ! deg (west<0,south<0)
 True_Latitude1 =  33.,      ! deg (west<0,south<0)
 True_Latitude2 =  45.,      ! deg (west<0,south<0, can = True_Latitude1)

!--- Parameters for the master (first) grid ---

 Number_of_Grids      = 2,
 Master_SW_XCoord     = -2556.,        ! km or deg, SW corner of cell(1,1)
 Master_SW_YCoord     = -1872.,        ! km or deg, SW corner of cell (1,1)
 Master_Cell_XSize    = 36.,           ! km or deg
 Master_Cell_YSize    = 36.,           ! km or deg
 Master_Grid_Columns  = 158,
 Master_Grid_Rows     = 91,
 Number_of_Layers     = 20,

!--- Parameters for the second grid ---

 Nest_Meshing_Factor(2) = 3,           ! Cell size relative to master grid
 Nest_Beg_I_Index(2)    = 85,          ! Relative to master grid
 Nest_End_I_Index(2)    = 134,         ! Relative to master grid
 Nest_Beg_J_Index(2)    = 26,          ! Relative to master grid
 Nest_End_J_Index(2)    = 74,          ! Relative to master grid

!--- Model options ---

 Diagnostic_Error_Check = .false.,      ! True = will stop after model setup
 Flexi_Nest             = .false.,      ! True = expect flexi-nested inputs
 Advection_Solver       = 'PPM',        ! (PPM,BOTT)
 Chemistry_Solver       = 'EBI',        ! (EBI,LSODE)
 PiG_Submodel           = 'None',       ! (None,GREASD,IRON)
 Probing_Tool           = 'None',       ! (None,SA,DDM,HDDM,PA,IPR,IRR,RTRAC,RTCMC)
 Chemistry              = .true.,
 Drydep_Model           = 'ZHANG03',    ! (None,WESELY89,ZHANG03)
 Bidi_NH3_Drydep        = .false.,
 Wet_Deposition         = .true.,
 ACM2_Diffusion         = .false.,
 Surface_Model          = .false.,
 Inline_Ix_Emissions    = .true.,
 Super_Stepping         = .true.,
 Gridded_Emissions      = .true.,
 Point_Emissions        = .true.,
 Ignore_Emission_Dates  = .true.,

!--- Output specifications ---

 Root_Output_Name         = '$OUTPUT/CAMx.$RUN.${CALDAY}',
 Average_Output_3D        = .false.,
 NetCDF_Format_Output     = .true.,
 NetCDF_Use_Compression   = .false.,
 Output_Species_Names(1)   = 'NO',     ! or set "ALL" or "ALLR"
 Output_Species_Names(2)   = 'NO2',
 Output_Species_Names(3)   = 'O3',
 Output_Species_Names(4)   = 'SO2',
 Output_Species_Names(5)   = 'H2O2',
 Output_Species_Names(6)   = 'HNO3',
 Output_Species_Names(7)   = 'NH3',
 Output_Species_Names(8)   = 'PNO3',
 Output_Species_Names(9)   = 'PSO4',
 Output_Species_Names(10)  = 'PNH4',
 Output_Species_Names(11)  = 'POA',
 Output_Species_Names(12)  = 'PEC',
 Output_Species_Names(13)  = 'FPRM',
 Output_Species_Names(14)  = 'CPRM',
 Output_Species_Names(15)  = 'CCRS',
 Output_Species_Names(16)  = 'FCRS',
 Output_Species_Names(17)  = 'SOA1',
 Output_Species_Names(18)  = 'SOA2',
 Output_Species_Names(19)  = 'SOA3',
 Output_Species_Names(20)  = 'SOA4',

!--- Input files ---

 Chemistry_Parameters = '$INPUT/CAMx7.1.chemparam.CB6r4_CF2',
 Photolysis_Rates     = '$INPUT/tuv.do_CB6r4.${CALDAY}',
 Ozone_Column         = '$INPUT/o3map.201606.txt',
 Initial_Conditions   = '$ICBC/ic.36km.${CALDAY}.GMT.hr0.nc',
 Boundary_Conditions  = '$ICBC/bc.36km.${CALDAY}.GMT.nc',
 Point_Sources(1)     = '$PTSRCE/point.camx.othpt.${CALDAY}.nc',
 Point_Sources(2)     = '$PTSRCE/point.camx.ptnonipm.${CALDAY}.nc',
 Point_Sources(3)     = '$PTSRCE/point.camx.pt_oilgas.${CALDAY}.nc',
 Master_Grid_Restart  = '$OUTPUT/CAMx.$RUN.${YESTERDAY}.inst',
 Nested_Grid_Restart  = '$OUTPUT/CAMx.$RUN.${YESTERDAY}.finst',
 PiG_Restart          = ' ',

 Surface_Grid(1) = '$MET/camx.lu.36km.${CALDAY}.nc',
 Met3D_Grid(1)   = '$MET/camx.3d.36km.${CALDAY}.nc',
 Met2D_Grid(1)   = '$MET/camx.2d.36km.${CALDAY}.nc',
 Vdiff_Grid(1)   = '$MET/camx.kv.36km.${CALDAY}.YSU.nc',
 Emiss_Grid(1,1) = '$EMIS/camx_area.area.${CALDAY}.36km.nc',
 Emiss_Grid(1,2) = '$EMIS/camx_area.mobile.${CALDAY}.36km.nc',
 Emiss_Grid(1,3) = '$EMIS/camx_area.pt.${CALDAY}.36km.nc',
 Emiss_Grid(1,4) = '$EMIS/camx_area.natural.${CALDAY}.36km.nc',

 Surface_Grid(2) = '$MET/camx.lu.12km.${CALDAY}.nc',
 Met3D_Grid(2)   = '$MET/camx.3d.12km.${CALDAY}.nc',
 Met2D_Grid(2)   = '$MET/camx.2d.12km.${CALDAY}.nc',
 Vdiff_Grid(2)   = '$MET/camx.kv.12km.${CALDAY}.YSU.nc',
 Emiss_Grid(2,1) = '$EMIS/camx_area.area.${CALDAY}.12km.nc',
 Emiss_Grid(2,2) = '$EMIS/camx_area.mobile.${CALDAY}.12km.nc',
 Emiss_Grid(2,3) = '$EMIS/camx_area.pt.${CALDAY}.12km.nc',
 Emiss_Grid(2,4) = '$EMIS/camx_area.natural.${CALDAY}.12km.nc',

 /
!-------------------------------------------------------------------------------

ieof

#
#  --- Execute the model ---
#
if( ! { mpiexec -launcher rsh -machinefile nodes -np $NUMPROCS $EXEC } ) then
   exit
endif
set RESTART = "YES"

end
