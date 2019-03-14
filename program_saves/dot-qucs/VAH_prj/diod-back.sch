<Qucs Schematic 0.0.19>
<Properties>
  <View=0,0,800,800,1,0,0>
  <Grid=10,10,1>
  <DataSet=diod-back.dat>
  <DataDisplay=diod-back.dpl>
  <OpenDisplay=1>
  <Script=diod-back.m>
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
  <Vdc V1 1 70 120 18 -26 0 1 "U1" 1>
  <Diode D1 1 290 120 -92 -26 0 3 "1e-15 A" 1 "1" 1 "10 fF" 1 "0.5" 0 "0.7 V" 0 "0.5" 0 "0.0 fF" 0 "0.0" 0 "2.0" 0 "0.0 Ohm" 0 "0.0 ps" 0 "0" 0 "0.0" 0 "1.0" 0 "1.0" 0 "0" 0 "1 mA" 0 "26.85" 0 "3.0" 0 "1.11" 0 "0.0" 0 "0.0" 0 "0.0" 0 "0.0" 0 "0.0" 0 "0.0" 0 "26.85" 0 "1.0" 0 "normal" 0>
  <IProbe I1 1 260 90 -26 16 0 0>
  <GND * 1 70 150 0 0 0 0>
  <GND * 1 290 150 0 0 0 0>
  <.SW SW1 1 60 250 0 63 0 0 "DC1" 1 "lin" 1 "U1" 1 "0V" 1 "1V" 1 "201" 1>
  <.DC DC1 1 270 250 0 63 0 0 "26.85" 0 "0.001" 0 "1 pA" 0 "1 uV" 0 "no" 0 "150" 0 "no" 0 "none" 0 "CroutLU" 0>
</Components>
<Wires>
  <70 90 230 90 "" 0 0 0 "">
</Wires>
<Diagrams>
</Diagrams>
<Paintings>
</Paintings>
