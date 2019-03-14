<Qucs Schematic 0.0.19>
<Properties>
  <View=0,0,926,800,1,0,0>
  <Grid=10,10,1>
  <DataSet=transistor_ce_II.dat>
  <DataDisplay=transistor_ce_II.dpl>
  <OpenDisplay=1>
  <Script=transistor_ce_II.m>
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
  <_BJT T1 1 240 180 -26 -122 0 1 "npn" 1 "1e-16" 1 "1" 1 "1" 0 "0" 0 "0" 0 "0" 1 "0" 0 "0" 0 "1.5" 0 "0" 0 "2" 0 "100" 1 "1" 0 "0" 0 "0" 0 "0" 0 "0" 0 "0" 0 "0" 0 "0.75" 0 "0.33" 0 "0" 0 "0.75" 0 "0.33" 0 "1.0" 0 "0" 0 "0.75" 0 "0" 0 "0.5" 0 "0.0" 0 "0.0" 0 "0.0" 0 "0.0" 0 "0.0" 0 "26.85" 0 "0.0" 0 "1.0" 0 "1.0" 0 "0.0" 0 "1.0" 0 "1.0" 0 "0.0" 0 "0.0" 0 "3.0" 0 "1.11" 0 "26.85" 0 "1.0" 0>
  <Idc I1 1 100 210 18 -26 0 1 "Ic" 1>
  <GND * 1 100 240 0 0 0 0>
  <.SW SW1 1 520 90 0 63 0 0 "SW2" 1 "lin" 1 "Ic" 1 "-2uA" 1 "2uA" 1 "41" 1>
  <.SW SW2 1 760 90 0 63 0 0 "DC1" 1 "lin" 1 "Ib" 1 "-2uA" 1 "2uA" 1 "41" 1>
  <.DC DC1 1 520 380 0 63 0 0 "26.85" 0 "0.001" 0 "1 pA" 0 "1 uV" 0 "no" 0 "150" 0 "no" 0 "none" 0 "CroutLU" 0>
  <GND * 1 360 180 0 0 0 0>
  <Idc I2 1 240 240 18 -26 0 1 "Ib" 1>
  <GND * 1 240 270 0 0 0 0>
</Components>
<Wires>
  <100 180 210 180 "" 0 0 0 "">
  <270 180 360 180 "" 0 0 0 "">
  <240 210 240 210 "Ube" 270 180 0 "">
  <100 180 100 180 "Uce" 130 150 0 "">
</Wires>
<Diagrams>
</Diagrams>
<Paintings>
</Paintings>
