<Qucs Schematic 0.0.19>
<Properties>
  <View=0,0,946,800,1,0,0>
  <Grid=10,10,1>
  <DataSet=transistor_cb.dat>
  <DataDisplay=transistor_cb.dpl>
  <OpenDisplay=1>
  <Script=transistor_cb.m>
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
  <_BJT T1 1 260 140 -26 -122 0 1 "npn" 1 "1e-16" 1 "1" 1 "1" 0 "0" 0 "0" 0 "0" 1 "0" 0 "0" 0 "1.5" 0 "0" 0 "2" 0 "100" 1 "1" 0 "0" 0 "0" 0 "0" 0 "0" 0 "0" 0 "0" 0 "0.75" 0 "0.33" 0 "0" 0 "0.75" 0 "0.33" 0 "1.0" 0 "0" 0 "0.75" 0 "0" 0 "0.5" 0 "0.0" 0 "0.0" 0 "0.0" 0 "0.0" 0 "0.0" 0 "26.85" 0 "0.0" 0 "1.0" 0 "1.0" 0 "0.0" 0 "1.0" 0 "1.0" 0 "0.0" 0 "0.0" 0 "3.0" 0 "1.11" 0 "26.85" 0 "1.0" 0>
  <GND * 1 260 170 0 0 0 0>
  <Idc I1 1 120 170 18 -26 0 1 "Ic" 1>
  <Idc I2 1 380 170 18 -26 0 1 "Ie" 1>
  <GND * 1 380 200 0 0 0 0>
  <GND * 1 120 200 0 0 0 0>
  <.SW SW1 1 540 50 0 63 0 0 "SW2" 1 "lin" 1 "Ic" 1 "-2nA" 1 "2nA" 1 "41" 1>
  <.SW SW2 1 780 50 0 63 0 0 "DC1" 1 "lin" 1 "Ie" 1 "-2nA" 1 "2nA" 1 "41" 1>
  <.DC DC1 1 540 340 0 63 0 0 "26.85" 0 "0.001" 0 "1 pA" 0 "1 uV" 0 "no" 0 "150" 0 "no" 0 "none" 0 "CroutLU" 0>
</Components>
<Wires>
  <120 140 230 140 "" 0 0 0 "">
  <290 140 380 140 "" 0 0 0 "">
  <120 140 120 140 "Ucb" 150 110 0 "">
  <380 140 380 140 "Ueb" 410 110 0 "">
</Wires>
<Diagrams>
</Diagrams>
<Paintings>
</Paintings>
