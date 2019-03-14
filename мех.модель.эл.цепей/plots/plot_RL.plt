set terminal png
set output 'RL.png'
unset xtics
set xlabel 't'
set multiplot layout 2,1
set ylabel 'U_L/U_0'
plot [-1:4] x<=0 ? 0 : (x<=2.95 ? exp(-x) : (x>2.95&&x<3 ? -1.5 : 0)) title 'U_L'
set ylabel 'I/I_0 (I_0=U_0/R)'
plot [-1:4] x<=0 ? 0 : (x<=2.95 ? 1-exp(-x) : 0) title 'I'
unset multiplot
