set terminal png
set output 'RC.png'
unset xtics
set xlabel 't'
set multiplot layout 2,1
set ylabel 'U_C/U_0'
plot [-1:4] x<=0 ? 0 : (x<=3 ? 1-exp(-x) : 1-exp(-3)) title 'U_C'
set ylabel 'I/I_0 (I_0=U_0/R)'
plot [-1:4] x<=0 ? 0 : (x<=3 ? exp(-x) : 0) title 'I'
unset multiplot
