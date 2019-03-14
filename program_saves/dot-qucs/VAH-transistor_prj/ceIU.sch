<Qucs Schematic 0.0.19>
<Properties>
  <View=0,-62,800,800,1,0,62>
  <Grid=10,10,1>
  <DataSet=ceIU.dat>
  <DataDisplay=ceIU.dpl>
  <OpenDisplay=1>
  <Script=ceIU.m>
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
  <_BJT T1 1 230 100 -26 -122 0 1 "npn" 1 "1e-16" 1 "1" 1 "1" 0 "0" 0 "0" 0 "0" 1 "0" 0 "0" 0 "1.5" 0 "0" 0 "2" 0 "100" 1 "1" 0 "0" 0 "0" 0 "0" 0 "0" 0 "0" 0 "0" 0 "0.75" 0 "0.33" 0 "0" 0 "0.75" 0 "0.33" 0 "1.0" 0 "0" 0 "0.75" 0 "0" 0 "0.5" 0 "0.0" 0 "0.0" 0 "0.0" 0 "0.0" 0 "0.0" 0 "26.85" 0 "0.0" 0 "1.0" 0 "1.0" 0 "0.0" 0 "1.0" 0 "1.0" 0 "0.0" 0 "0.0" 0 "3.0" 0 "1.11" 0 "26.85" 0 "1.0" 0>
  <GND * 1 230 130 0 0 0 0>
  <Idc I1 1 120 130 18 -26 0 1 "Ic" 1>
  <Vdc V1 1 360 130 -64 -26 0 3 "Ube" 1>
  <IProbe Ie 1 290 100 -26 16 0 0>
  <GND * 1 360 160 0 0 0 0>
  <GND * 1 120 160 0 0 0 0>
  <.SW SW1 1 460 50 0 63 0 0 "SW2" 1 "lin" 1 "Ic" 1 "-1A" 1 "0" 1 "41" 1>
  <.SW SW2 1 650 50 0 63 0 0 "DC1" 1 "lin" 1 "Ube" 1 "-30V" 1 "0.9V" 1 "41" 1>
  <.DC DC1 1 460 400 0 63 0 0 "26.85" 0 "0.001" 0 "1 pA" 0 "1 uV" 0 "no" 0 "150" 0 "no" 0 "none" 0 "CroutLU" 0>
</Components>
<Wires>
  <320 100 360 100 "" 0 0 0 "">
  <120 100 200 100 "" 0 0 0 "">
  <120 100 120 100 "Ucb" 150 70 0 "">
</Wires>
<Diagrams>
</Diagrams>
<Paintings>
</Paintings>
