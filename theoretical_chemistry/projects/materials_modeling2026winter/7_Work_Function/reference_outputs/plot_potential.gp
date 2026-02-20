set terminal pngcairo enhanced size 1200,900 font "Arial,14"
set output 'potential_plot.png'
set title 'Electrostatic Potential Averaging (z-direction)'
set xlabel 'Position along z-axis (Å)'
set ylabel 'Electrostatic Potential (eV)'
set grid linecolor rgb '#dddddd' linewidth 1
set key top right box linecolor rgb '#000000' linewidth 1

# Style settings
set style line 1 linecolor rgb '#ff0000' linewidth 2 pointsize 0.5
set style line 2 linecolor rgb '#0000ff' linewidth 3 pointsize 0.5
set style line 3 linecolor rgb '#00cc00' linewidth 2 dashtype 2

# Set ranges
set xr [0:15.0]
set autoscale y

# Fermi level line
set arrow from graph 0, first -4.2405 to graph 1, first -4.2405 nohead linestyle 3

plot 'potential_results/avg.dat' using ($1*0.529177):($2*13.6058) with lines linestyle 1 title 'Planar Average', \
     'potential_results/avg.dat' using ($1*0.529177):($3*13.6058) with lines linestyle 2 title 'Macroscopic Average', \
     -4.2405 with lines linestyle 3 title 'Fermi Level (-4.240 eV)'

# Add some annotations
set label "Cell length: 15.0 Å" at graph 0.05,0.95
set label "Fermi level: -4.240 eV" at graph 0.05,0.88
set label "Data from avg.dat" at graph 0.05,0.81

set output
