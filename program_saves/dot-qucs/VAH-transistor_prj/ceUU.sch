<Qucs Schematic 0.0.19>
<Properties>
  <View=0,-62,916,800,1,0,62>
  <Grid=10,10,1>
  <DataSet=ceUU.dat>
  <DataDisplay=ceUU.dpl>
  <OpenDisplay=1>
  <Script=ceUU.m>
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
  <_BJT T1 1 250 100 -26 -122 0 1 "npn" 1 "1e-16" 1 "1" 1 "1" 0 "0" 0 "0" 0 "0" 1 "0" 0 "0" 0 "1.5" 0 "0" 0 "2" 0 "100" 1 "1" 0 "0" 0 "0" 0 "0" 0 "0" 0 "0" 0 "0" 0 "0.75" 0 "0.33" 0 "0" 0 "0.75" 0 "0.33" 0 "1.0" 0 "0" 0 "0.75" 0 "0" 0 "0.5" 0 "0.0" 0 "0.0" 0 "0.0" 0 "0.0" 0 "0.0" 0 "26.85" 0 "0.0" 0 "1.0" 0 "1.0" 0 "0.0" 0 "1.0" 0 "1.0" 0 "0.0" 0 "0.0" 0 "3.0" 0 "1.11" 0 "26.85" 0 "1.0" 0>
  <Vdc V1 1 100 130 18 -26 0 1 "Ucb" 1>
  <IProbe Ic 1 190 100 -26 16 0 0>
  <GND * 1 100 160 0 0 0 0>
  <GND * 1 250 130 0 0 0 0>
  <GND * 1 400 160 0 0 0 0>
  <.SW SW1 1 520 60 0 63 0 0 "SW2" 1 "lin" 1 "Ucb" 1 "-900mV" 1 "1V" 1 "41" 1>
  <.SW SW2 1 750 60 0 63 0 0 "DC1" 1 "lin" 1 "Ube" 1 "-1V" 1 "900mV" 1 "41" 1>
  <.DC DC1 1 520 350 0 63 0 0 "26.85" 0 "0.001" 0 "1 pA" 0 "1 uV" 0 "no" 0 "150" 0 "no" 0 "none" 0 "CroutLU" 0>
  <Vdc V3 1 400 130 -64 -26 0 3 "Ube" 1>
  <IProbe Ie 1 310 100 -26 16 0 0>
</Components>
<Wires>
  <100 100 160 100 "" 0 0 0 "">
  <340 100 400 100 "" 0 0 0 "">
</Wires>
<Diagrams>
</Diagrams>
<Paintings>
</Paintings>
