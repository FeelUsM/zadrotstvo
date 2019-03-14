<Qucs Schematic 0.0.19>
<Properties>
  <View=0,-52,916,800,1,0,52>
  <Grid=10,10,1>
  <DataSet=ceUURR.dat>
  <DataDisplay=ceUURR.dpl>
  <OpenDisplay=1>
  <Script=ceUURR.m>
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
  <_BJT T1 1 250 110 -26 -122 0 1 "npn" 1 "1e-16" 1 "1" 1 "1" 0 "0" 0 "0" 0 "0" 1 "0" 0 "0" 0 "1.5" 0 "0" 0 "2" 0 "100" 1 "1" 0 "0" 0 "0" 0 "0" 0 "0" 0 "0" 0 "0" 0 "0.75" 0 "0.33" 0 "0" 0 "0.75" 0 "0.33" 0 "1.0" 0 "0" 0 "0.75" 0 "0" 0 "0.5" 0 "0.0" 0 "0.0" 0 "0.0" 0 "0.0" 0 "0.0" 0 "26.85" 0 "0.0" 0 "1.0" 0 "1.0" 0 "0.0" 0 "1.0" 0 "1.0" 0 "0.0" 0 "0.0" 0 "3.0" 0 "1.11" 0 "26.85" 0 "1.0" 0>
  <IProbe Ic1 1 190 110 -26 16 0 0>
  <GND * 1 250 140 0 0 0 0>
  <.SW SW1 1 520 70 0 63 0 0 "SW2" 1 "lin" 1 "Ucb" 1 "-1V" 1 "1V" 1 "41" 1>
  <.SW SW2 1 750 70 0 63 0 0 "DC1" 1 "lin" 1 "Ube" 1 "-1V" 1 "1V" 1 "41" 1>
  <.DC DC1 1 520 360 0 63 0 0 "26.85" 0 "0.001" 0 "1 pA" 0 "1 uV" 0 "no" 0 "150" 0 "no" 0 "none" 0 "CroutLU" 0>
  <IProbe Ie1 1 310 110 -26 16 0 0>
  <R R2 1 370 110 -26 15 0 0 "50 Ohm" 1 "26.85" 0 "0.0" 0 "0.0" 0 "26.85" 0 "european" 0>
  <R R3 1 130 110 -26 15 0 0 "50 Ohm" 1 "26.85" 0 "0.0" 0 "0.0" 0 "26.85" 0 "european" 0>
  <Vdc V1 1 20 140 18 -26 0 1 "Ucb" 1>
  <GND * 1 20 170 0 0 0 0>
  <GND * 1 480 170 0 0 0 0>
  <Vdc V2 1 480 140 -64 -26 0 3 "Ube" 1>
</Components>
<Wires>
  <20 110 100 110 "" 0 0 0 "">
  <400 110 480 110 "" 0 0 0 "">
</Wires>
<Diagrams>
</Diagrams>
<Paintings>
</Paintings>
