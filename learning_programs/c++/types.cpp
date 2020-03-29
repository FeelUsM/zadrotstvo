
void foo(int k(void)){
	;
}
int bar(){
	return 3;
}


int main(){
typedef const int T1;
typedef const int T1;
typedef int * T2;
typedef int & T3;
typedef int && T4;
typedef int T5[];
typedef int T6[7];
typedef int T7(void); 
typedef auto T8(int) -> int;
typedef void T9(int);

//--- const int ---
//typedef const int const T11;// дублирование «const»
typedef const int * T12;
typedef const int & T13;
typedef const int && T14;
typedef const int T15[];
typedef const int T16[7];
typedef const int T17(void);
typedef auto T18(int) -> const int;
typedef void T19(const int k);

//--- int* ---
typedef int* const T21;
typedef int* * T22;
typedef int* & T23;
typedef int* && T24;
typedef int* T25[];
typedef int* T26[7];
typedef int* T27(void);
typedef auto T28(int) -> int*;
typedef void T29(int * k);

//--- int& ---
//typedef int& const T31; // квалификаторы «const» не могут быть применены к «int&»
//typedef int& * T32; // недопустимая декларация указателя на «int&»
//typedef int& & T33; // Недопустимо определять ссылку на «int&», которая не будет определением типа или аргументом шаблона
//typedef int& && T34; // Недопустимо определять ссылку на «int&», которая не будет определением типа или аргументом шаблона
//typedef int& T35[]; // декларация «T35» как массива ссылок
//typedef int& T36[7]; // декларация «T36» как массива ссылок
typedef int& T37(void);
typedef auto T38(int) -> int&;
typedef void T39(int & k);

//--- int&& ---
//typedef int&& const T41; // квалификаторы «const» не могут быть применены к «int&&»
//typedef int&& * T42; //  недопустимая декларация указателя на «int&&»
//typedef int&& & T43; //  Недопустимо определять ссылку на «int&&», которая не будет определением типа или аргументом шаблона
//typedef int&& && T44; //  Недопустимо определять ссылку на «int&&», которая не будет определением типа или аргументом шаблона
//typedef int&& T45[]; // декларация «T45» как массива ссылок
//typedef int&& T46[7]; // декларация «T46» как массива ссылок
typedef int&& T47(void);
typedef auto T48(int) -> int&&;
typedef void T49(int && k);

//--- int T5[] ---
//typedef int (const T51)[]; //expected unqualified-id before «const»
typedef int (*T52)[];
typedef int (&T53)[];
typedef int (&&T54)[];
//typedef int (T55[])[]; // декларация многомерного массива «T56» должна определять границы для всех размерностей, кроме первой
//typedef int (T56[7])[]; // декларация многомерного массива «T56» должна определять границы для всех размерностей, кроме первой
//typedef int (T57(void))[]; // «T57» объявлена как функция, возвращающая массив
typedef auto T58(int) -> int [];
typedef void T59(int k[]);

//--- int T6[7] ---
//typedef int (const T61)[7]; //expected unqualified-id before «const»
typedef int (*T62)[7];
typedef int (&T63)[7];
typedef int (&&T64)[7];
typedef int (T65[])[7];  typedef int T65[][7];
typedef int (T66[7])[7]; typedef int T66[7][7];
//typedef int (T67(void))[7]; // «T57» объявлена как функция, возвращающая массив
typedef auto T68(int) -> int [7];
typedef void T69(int k[7]);

//--- int T7(void); ---
//typedef int (const T71)(void); // expected unqualified-id before «const»
typedef int (*T72)(void);
typedef int (&T73)(void);
typedef int (&&T74)(void);
//typedef int (T75[])(void); // декларация «T75» как массива функций
//typedef int (T76[7])(void); // декларация «T76» как массива функций
//typedef int (T77(void))(void); // «T77» объявлена как функция, возвращающая функцию
//typedef auto T78(int) -> int(int); // результат функции не может иметь тип функции
typedef void T79(int k(void));  foo(bar); foo(*bar); // ?!?!?!?!

//--- auto T8(int) -> int ---
//typedef ((int) -> int) const T81; // expected unqualified-id before «auto»
//typedef (auto(int) -> int)*T82; // expected unqualified-id before «auto»
//typedef (auto(int) -> int)&T83; // expected unqualified-id before «auto»
//typedef (auto(int) -> int)&&T84; // expected unqualified-id before «auto»
//typedef (auto(int) -> int) T85[]; // expected unqualified-id before «auto»
//typedef (auto(int) -> int) T86[7]; // expected unqualified-id before «auto»
//typedef (auto(int) -> int) T87(void); // expected unqualified-id before «auto»
//typedef auto T88(void) -> (auto(int) -> int); // expected unqualified-id before «auto»
typedef void T89(auto k(int) -> int);

//--- void T9(int); ---
//typedef void (const T91)(int); // expected unqualified-id before «const»
typedef void (*T92)(int);
typedef void (&T93)(int);
typedef void (&&T94)(int);
//typedef void (T95[])(int); // декларация «T75» как массива функций
//typedef void (T96[7])(int); // декларация «T76» как массива функций
//typedef void (T97(void))(int); // «T77» объявлена как функция, возвращающая функцию
//typedef auto T98(int) -> void(int); // результат функции не может иметь тип функции
typedef void T99(void k(int));  foo(bar); foo(*bar); // ?!?!?!?!

//тип                 тип const тип*  тип&    тип&&   тип[]   тип[7]  тип()   auto()->тип     void (тип)
//const int           .         OK    OK      OK      OK      OK      OK      OK              OK      
//int *               OK        OK    OK      OK      OK      OK      OK      OK              OK      
//int &               .         .     .       .       .       .       OK      OK              OK      
//int &&              .         .     .       .       .       .       OK      OK              OK      
//int []              .         OK    OK      OK      .       .       .       OK              OK      
//int [7]             .         OK    OK      OK      OK      OK      .       OK              OK      
//int (void)          .         OK    OK      OK      .       .       .       .               OK      
//auto (void) -> int  .         .     .       .       .       .       .       .               OK      
//void (int)          .         OK    OK      OK      .       .       .       .               OK      


}