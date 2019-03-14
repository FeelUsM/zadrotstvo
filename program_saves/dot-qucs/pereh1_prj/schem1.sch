<Qucs Schematic 0.0.19>
<Properties>
  <View=0,0,877,800,1,0,0>
  <Grid=10,10,1>
  <DataSet=schem1.dat>
  <DataDisplay=schem1.dpl>
  <OpenDisplay=1>
  <Script=schem1.m>
  <RunScript=0>
  <showFrame=0>
  <FrameText0=Название>
  <FrameText1=Чертил:>
  <FrameText2=Дата:>
  <FrameText3=Версия:>
</Properties>
<Symbol>
</Symbol>
<Components>
  <Vdc V1 1 240 190 18 -26 0 1 "1 V" 1>
  <C C1 1 380 210 17 -26 0 1 "1000000 pF" 1 "0" 0 "neutral" 0>
  <R R1 1 380 140 15 -26 0 1 "200000 Ohm" 1 "26.85" 0 "0.0" 0 "0.0" 0 "26.85" 0 "european" 0>
  <.TR TR1 1 70 330 0 63 0 0 "lin" 1 "0" 1 "1000 ms" 1 "51" 0 "Trapezoidal" 0 "2" 0 "1 ns" 0 "1e-16" 0 "150" 0 "0.001" 0 "1 pA" 0 "1 uV" 0 "26.85" 0 "1e-3" 0 "1e-6" 0 "1" 0 "CroutLU" 0 "no" 0 "yes" 0 "0" 0>
  <IProbe Pr1 1 310 110 -26 16 0 0>
  <GND * 1 380 240 0 0 0 0>
</Components>
<Wires>
  <240 220 240 240 "" 0 0 0 "">
  <380 170 380 180 "" 0 0 0 "">
  <340 110 380 110 "" 0 0 0 "">
  <240 110 240 160 "" 0 0 0 "">
  <240 110 280 110 "" 0 0 0 "">
  <240 240 380 240 "" 0 0 0 "">
  <380 180 380 180 "Uc" 410 150 0 "">
</Wires>
<Diagrams>
</Diagrams>
<Paintings>
</Paintings>
