<Qucs Schematic 0.0.19>
<Properties>
  <View=0,0,800,800,1,0,0>
  <Grid=10,10,1>
  <DataSet=main.dat>
  <DataDisplay=main.dpl>
  <OpenDisplay=1>
  <Script=main.m>
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
  <.DC DC1 1 230 430 0 63 0 0 "26.85" 0 "0.001" 0 "1 pA" 0 "1 uV" 0 "no" 0 "150" 0 "no" 0 "none" 0 "CroutLU" 0>
  <Diode D1 1 260 110 15 -26 0 1 "1e-15 A" 1 "1" 1 "10 fF" 1 "0.5" 0 "0.7 V" 0 "0.5" 0 "0.0 fF" 0 "0.0" 0 "2.0" 0 "0.0 Ohm" 0 "0.0 ps" 0 "0" 0 "0.0" 0 "1.0" 0 "1.0" 0 "0" 0 "1 mA" 0 "26.85" 0 "3.0" 0 "1.11" 0 "0.0" 0 "0.0" 0 "0.0" 0 "0.0" 0 "0.0" 0 "0.0" 0 "26.85" 0 "1.0" 0 "normal" 0>
  <GND * 1 140 140 0 0 0 0>
  <GND * 1 260 140 0 0 0 0>
  <Idc I1 1 140 110 18 -26 0 1 "I0" 1>
  <.SW SW1 1 50 320 0 63 0 0 "DC1" 1 "lin" 1 "I0" 1 "0mA" 1 "0.000001mA" 1 "201" 1>
</Components>
<Wires>
  <140 80 260 80 "" 0 0 0 "">
  <260 80 260 80 "U0" 290 50 0 "">
</Wires>
<Diagrams>
</Diagrams>
<Paintings>
</Paintings>
