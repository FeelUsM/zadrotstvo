<Qucs Schematic 0.0.19>
<Properties>
  <View=0,0,800,800,1,111,0>
  <Grid=10,10,1>
  <DataSet=cbUU.dat>
  <DataDisplay=cbUU.dpl>
  <OpenDisplay=1>
  <Script=cbUU.m>
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
  <_BJT T1 1 260 230 8 -26 0 0 "npn" 1 "1e-16" 1 "1" 1 "1" 0 "0" 0 "0" 0 "0" 1 "0" 0 "0" 0 "1.5" 0 "0" 0 "2" 0 "100" 1 "1" 0 "0" 0 "0" 0 "0" 0 "0" 0 "0" 0 "0" 0 "0.75" 0 "0.33" 0 "0" 0 "0.75" 0 "0.33" 0 "1.0" 0 "0" 0 "0.75" 0 "0" 0 "0.5" 0 "0.0" 0 "0.0" 0 "0.0" 0 "0.0" 0 "0.0" 0 "26.85" 0 "0.0" 0 "1.0" 0 "1.0" 0 "0.0" 0 "1.0" 0 "1.0" 0 "0.0" 0 "0.0" 0 "3.0" 0 "1.11" 0 "26.85" 0 "1.0" 0>
  <.SW SW1 1 430 100 0 63 0 0 "SW2" 1 "lin" 1 "Ube" 1 "-10V" 1 "2mV" 1 "41" 1>
  <.SW SW2 1 620 100 0 63 0 0 "DC1" 1 "lin" 1 "Uce" 1 "-200mV" 1 "10V" 1 "41" 1>
  <.DC DC1 1 430 340 0 63 0 0 "26.85" 0 "0.001" 0 "1 pA" 0 "1 uV" 0 "no" 0 "150" 0 "no" 0 "none" 0 "CroutLU" 0>
  <Vdc V1 1 150 140 -69 -26 1 1 "Uce" 1>
  <GND * 1 150 170 0 0 0 0>
  <IProbe Ic 1 230 110 -26 16 0 0>
  <IProbe Ib 1 200 230 -26 16 0 0>
  <Vdc V2 1 150 260 -64 -26 1 1 "Ube" 1>
  <GND * 1 150 290 0 0 0 0>
  <IProbe Ie 1 260 350 -42 -26 0 3>
  <GND * 1 260 380 0 0 0 0>
</Components>
<Wires>
  <260 110 260 200 "" 0 0 0 "">
  <150 110 200 110 "" 0 0 0 "">
  <150 230 170 230 "" 0 0 0 "">
  <260 260 260 320 "" 0 0 0 "">
</Wires>
<Diagrams>
</Diagrams>
<Paintings>
</Paintings>
