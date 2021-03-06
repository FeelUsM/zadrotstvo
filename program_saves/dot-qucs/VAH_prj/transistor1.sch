<Qucs Schematic 0.0.19>
<Properties>
  <View=0,0,1026,800,1,0,0>
  <Grid=10,10,1>
  <DataSet=transistor1.dat>
  <DataDisplay=transistor1.dpl>
  <OpenDisplay=1>
  <Script=transistor1.m>
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
  <Vdc V1 1 520 170 18 -26 0 1 "Uce" 1>
  <IProbe Ic 1 490 140 -26 -35 0 2>
  <Idc I1 1 260 200 18 -26 0 1 "Ib" 1>
  <_BJT T1 1 380 170 8 -26 0 0 "npn" 1 "1e-16" 1 "1" 1 "1" 0 "0" 0 "0" 0 "0" 1 "0" 0 "0" 0 "1.5" 0 "0" 0 "2" 0 "100" 1 "1" 0 "0" 0 "0" 0 "0" 0 "0" 0 "0" 0 "0" 0 "0.75" 0 "0.33" 0 "0" 0 "0.75" 0 "0.33" 0 "1.0" 0 "0" 0 "0.75" 0 "0" 0 "0.5" 0 "0.0" 0 "0.0" 0 "0.0" 0 "0.0" 0 "0.0" 0 "26.85" 0 "0.0" 0 "1.0" 0 "1.0" 0 "0.0" 0 "1.0" 0 "1.0" 0 "0.0" 0 "0.0" 0 "3.0" 0 "1.11" 0 "26.85" 0 "1.0" 0>
  <GND * 1 380 250 0 0 0 0>
  <GND * 1 520 250 0 0 0 0>
  <GND * 1 260 250 0 0 0 0>
  <.SW SW1 1 860 40 0 63 0 0 "SW2" 1 "lin" 1 "Uce" 1 "0.03V" 1 "1V" 1 "21" 1>
  <.SW SW2 1 680 40 0 63 0 0 "DC1" 1 "lin" 1 "Ib" 1 "0A" 1 "5mA" 1 "21" 1>
  <.DC DC1 1 680 270 0 63 0 0 "26.85" 0 "0.001" 0 "1 pA" 0 "1 uV" 0 "no" 0 "150" 0 "no" 0 "none" 0 "CroutLU" 0>
</Components>
<Wires>
  <380 140 460 140 "" 0 0 0 "">
  <260 170 350 170 "" 0 0 0 "">
  <380 200 380 250 "" 0 0 0 "">
  <520 200 520 250 "" 0 0 0 "">
  <260 230 260 250 "" 0 0 0 "">
  <260 170 260 170 "Ub" 290 140 0 "">
</Wires>
<Diagrams>
</Diagrams>
<Paintings>
</Paintings>
