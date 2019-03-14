<Qucs Schematic 0.0.19>
<Properties>
  <View=0,-62,800,800,1,0,62>
  <Grid=10,10,1>
  <DataSet=ceUI.dat>
  <DataDisplay=ceUI.dpl>
  <OpenDisplay=1>
  <Script=ceUI.m>
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
  <Idc I1 1 340 130 -69 -26 0 3 "Ie" 1>
  <IProbe Ic 1 170 100 -26 16 0 0>
  <Vdc V1 1 60 130 18 -26 0 1 "Ucb" 1>
  <GND * 1 340 160 0 0 0 0>
  <GND * 1 230 130 0 0 0 0>
  <GND * 1 60 160 0 0 0 0>
  <.SW SW1 1 490 60 0 63 0 0 "SW2" 1 "lin" 1 "Ucb" 1 "-0.9V" 1 "10V" 1 "41" 1>
  <.SW SW2 1 670 60 0 63 0 0 "DC1" 1 "lin" 1 "Ie" 1 "0" 1 "1A" 1 "41" 1>
  <.DC DC1 1 490 330 0 63 0 0 "26.85" 0 "0.001" 0 "1 pA" 0 "1 uV" 0 "no" 0 "150" 0 "no" 0 "none" 0 "CroutLU" 0>
</Components>
<Wires>
  <60 100 140 100 "" 0 0 0 "">
  <260 100 340 100 "" 0 0 0 "">
  <340 100 340 100 "Ueb" 370 70 0 "">
</Wires>
<Diagrams>
</Diagrams>
<Paintings>
</Paintings>
