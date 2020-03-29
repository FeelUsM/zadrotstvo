struct CIE {
	uword	length
	size_t	CIE_id = 0xffffffff
	ubyte	version = 1
	char[]	augmentation - системно-зависимая запись
	uLEB128	code_alignment_factor
	sLEB128	data_alignment_factor
	ubyte	return_address_register - какой столбец таблицы правил обозначает адрес возврата ф-ции
	...		initial_instructions
	...		padding
}
struct FDE {
	uword	length
	void *	CIE_pointer
	void *	initial_location
	size_t	address_range - размер instructions
	...		instructions
}

возможные инструкции:
	undefined
	same_value
	offset(N)
	register(R) ???
	architectural

Instruction 			High_2	Low 6 Bits 	Operand 1 			Operand 2
DW_CFA_advance_loc 		0x1 	delta
DW_CFA_advance_loc1 	0 		0x02 		1-byte delta
DW_CFA_advance_loc2 	0 		0x03 		2-byte delta
DW_CFA_advance_loc4 	0 		0x04 		4-byte delta
	новая строка : location = current_clocation + (delta * code_alignment_factor)
DW_CFA_set_loc 			0 		0x01 		address
	новая строка : location = address // address должен быть больше чем текущий адрес
DW_CFA_remember_state 	0 		0x0a		
	правила текущей строки добавить в стек
DW_CFA_restore_state 	0 		0x0b		
	достать из стека правила и присвоить текущей строке

DW_CFA_offset 			0x2 	register 	ULEB128	offset
DW_CFA_offset_extended 	0 		0x05 		ULEB128 register 	ULEB128 offset
	rule(register) = offset(N = offset * data_alignment_factor)
DW_CFA_restore 			0x3 	register
DW_CFA_restore_extended 0 		0x06 		ULEB128 register
	rule(register) = rule(register) from initial_instructions from CIE
DW_CFA_undefined 		0 		0x07 		ULEB128 register
	rule(register) = undefined
DW_CFA_same_value		0 		0x08 		ULEB128 register
	rule(register) = same_value
DW_CFA_register 		0 		0x09 		ULEB128 register1 	ULEB128 register2
	rule(register2) = rule(register1) // или наоборот ???

DW_CFA_def_cfa 			0 		0x0c 		ULEB128 register 	ULEB128 offset
	??????? определить текущее правило CFA для использования предоставленного регистра и смещения. 
DW_CFA_def_cfa_register 0 		0x0d 		ULEB128 register
	??????? определить текущее правило CFA для использования предоставленного регистра (но смещение оставить прежним). 
DW_CFA_def_cfa_offset 	0 		0x0e 		ULEB128 offset
	??????? определить текущее правило CFA для использования предоставленного смещения (но регистр оставить прежним). 

DW_CFA_nop 				0 		0
	ни чего не делать
	
DW_CFA_lo_user 			0		0x1c
	???
DW_CFA_hi_user 			0 		0x3f
	???




struct _Unwind_Context; // opaque - скрыто системой
/*
В качестве основы мы принимаем таблицы дескрипторов раскрутки, 
описанные в базовом руководстве по соглашениям и архитектуре программного обеспечения Itanium .
https://www.intel.com/content/dam/www/public/us/en/documents/guides/itanium-software-runtime-architecture-guide.pdf

Наконец, подпрограмма индивидуальности для языка и поставщика будет сохранена компилятором 
	в дескрипторе размотки для стековых ФРЕЙМОВ, требующих обработки исключений
*/
//==================================================================
/*
Каждый из этих двух этапов использует и библиотеку раскручивания, и подпрограммы индивидуальности, 
поскольку валидность данного обработчика и механизм передачи ему управления зависят от языка, 
но метод определения местоположения и восстановления предыдущих кадров стека не зависит от языка.

типы:
	_Unwind_Reason_Code
	_Unwind_Action
		_Unwind_Exception_Cleanup_Fn
	_Unwind_Exception
вызываются из обычного кода:
	_Unwind_RaiseException
	_Unwind_ForcedUnwind
персональная функция:
	_Unwind_Stop_Fn
	__personality_routine
вызываются из персональной функции и stop-функции(от _Unwind_ForcedUnwind):
	_Unwind_GetGR
	_Unwind_SetGR
	_Unwind_GetIP
	_Unwind_SetIP
	_Unwind_GetLanguageSpecificData
	_Unwind_GetRegionStart
stop-функция(от _Unwind_ForcedUnwind) в случае успеха:
	сама превращается в "посадочную площадку"
персональная функция в случае успеха:
	устанавливает контекст и возвращает _URC_INSTALL_CONTEXT
вызываются из посадочной площадки:
	_Unwind_Resume
	_Unwind_DeleteException

заголовок catch-блока копирует исключение, и исходное исключение удаляет
тело catch-блока - обычный код - обработчиком в понимании библиотеки _Unwind не является
*/

typedef enum {
	_URC_NO_REASON = 0,
	_URC_FOREIGN_EXCEPTION_CAUGHT = 1,
	_URC_FATAL_PHASE2_ERROR = 2,
	_URC_FATAL_PHASE1_ERROR = 3,
	_URC_NORMAL_STOP = 4,
	_URC_END_OF_STACK = 5,
	_URC_HANDLER_FOUND = 6,
	_URC_INSTALL_CONTEXT = 7,
	_URC_CONTINUE_UNWIND = 8
} _Unwind_Reason_Code;

typedef int _Unwind_Action;
static const _Unwind_Action _UA_SEARCH_PHASE = 1;
static const _Unwind_Action _UA_CLEANUP_PHASE = 2;
static const _Unwind_Action _UA_HANDLER_FRAME = 4;
static const _Unwind_Action _UA_FORCE_UNWIND = 8;

typedef void 
(*_Unwind_Exception_Cleanup_Fn)(
	_Unwind_Reason_Code reason,
	struct _Unwind_Exception *exc
);
struct _Unwind_Exception {
	uint64			 exception_class; // тип исключения (производитель,язык)
	_Unwind_Exception_Cleanup_Fn exception_cleanup; // деструктор
	uint64			 private_1;
	uint64			 private_2;
};

/*
откуда можно вызывать функции интерфейса:
из обычного кода (инициировать размотку: _Unwind_RaiseException, _Unwind_ForcedUnwind)
из посадочных площадок (завершать (_Unwind_DeleteException) или продолжать размотку(_Unwind_Resume))
из персональной или stop- функции (работа с контекстом ...)
*/

/*
посадочная площадка - часть обчного кода (откуда return будет в обычный код)
куда можно передать управление через контекст
*/

//-------------------

_Unwind_Reason_Code 
_Unwind_RaiseException( struct _Unwind_Exception *exception_object ); // <<<<<<<<<<<<<<<<<<<<<<
/*
объект исключения аллоцируется языковой средой
не возвращается, если не произошли ошибки
возможные ошибки:
	_URC_END_OF_STACK - обработчик не найден; c++ обычно вызывает uncaught_exception() ...
	_URC_FATAL_PHASE1_ERROR
	_URC_FATAL_PHASE2_ERROR
		- непредвиденная ошибка, например поврежден стек
		c++ обычно вызывает terminate()
*/

// typedef ...(*_Unwind_Stop_Fn)(...)
_Unwind_Reason_Code 
_Unwind_ForcedUnwind( // <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
	struct _Unwind_Exception *exception_object,
	_Unwind_Stop_Fn stop,
	void *stop_parameter 
);
/*
выполняет только фазу очистки (например long jmp или завершение потока)
не возвращается, если не произошли ошибки (_URC_END_OF_STACK или _URC_FATAL_PHASE2_ERROR или что-то еще)
возможные ошибки:
	_URC_FATAL_PHASE2_ERROR
*/

// ---------------------

// параметр _Unwind_ForcedUnwind
typedef _Unwind_Reason_Code 
(*_Unwind_Stop_Fn)(
	int version,
	_Unwind_Action actions,
	uint64 exceptionClass,
	struct _Unwind_Exception *exceptionObject,
	struct _Unwind_Context *context,
	void *stop_parameter // дополнительная информация к исключению
);
// как в индивидуальной подпрограмме + stop_parameter
/*
когда stop-функция идентифицирует целевой кадр
	она не возвращается и передает управление пользовательскому коду обычно после вызова _Unwind_DeleteException()
	! никакой установки контекста и никаких посадочных площадок
когда stop-функция НЕ идентифицирует - она возвращает
	_URC_NO_REASON - тогда библиотека _Unwind вызывает персональную подпрограмму на этом фрейме
		с параметрами _UA_FORCE_UNWIND и _UA_CLEANUP_PHASE
		после этого разматывает 1 фрейм и снова вызывает stop-функцию
	_URC_END_OF_STACK - 
		после того как был отвергнут последний фрейм
			библиотека _Unwind вызывает stop-функцию с context=NULL
			stop-функция может эту ситуацию обработать, а может вернуть _URC_END_OF_STACK
	_URC_FATAL_PHASE2_ERROR
*/

// будет сохранена компилятором в дескрипторе размотки для стековых ФРЕЙМОВ
_Unwind_Reason_Code 
(*__personality_routine)( // <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
	int version, // версия интерфейса(?) библиотеки _Unwind 
	_Unwind_Action actions, // что требуется от пресональной функции, флаги
	uint64 exceptionClass, // тип исключения (производитель,язык)
	struct _Unwind_Exception *exceptionObject, // собственно сиключение
	struct _Unwind_Context *context //
);
/*
_UA_SEARCH_PHASE = 1;
	проверить, содержит ли текущий ФРЕЙМ обработчик
	-> _URC_HANDLER_FOUND / _URC_CONTINUE_UNWIND

_UA_CLEANUP_PHASE = 2;
	выполнить очистку самостоятельно (или при помощи других функций)
	-> _URC_CONTINUE_UNWIND
	настроить регистры (context) для передачи управления на посадочную площадку
	-> _URC_INSTALL_CONTEXT
_UA_HANDLER_FRAME = 4; - совместно с _UA_CLEANUP_PHASE
	передается в фазе 2, если в фазе 1 на этом фрейме _URC_HANDLER_FOUND.
	индивидуальной функции нельзя менять свое мнение, и здесь должен выполниться обработчик
_UA_FORCE_UNWIND = 8; - совместно с _UA_CLEANUP_PHASE
	указывает, что персональная функция вернет _URC_CONTINUE_UNWIND
		или вернет _URC_INSTALL_CONTEXT, но посадочная площадка вызовет _Unwind_Resume()
*/

//---------------

uint64 _Unwind_GetGR(struct _Unwind_Context *context, int index);
// Эта функция возвращает 64-битное значение данного общего регистра. 
// Регистр идентифицируется его индексом: 
void   _Unwind_SetGR(struct _Unwind_Context *context, int index, uint64 new_value);
// Эта функция устанавливает 64-битное значение данного регистра, идентифицируемого его индексом. 
uint64 _Unwind_GetIP(struct _Unwind_Context *context);
// Эта функция возвращает 64-битное значение указателя инструкций (IP).
void   _Unwind_SetIP(struct _Unwind_Context *context,            uint64 new_value);
// Эта функция устанавливает значение указателя инструкций (IP) для подпрограммы, определенной контекстом раскрутки.
uint64 _Unwind_GetLanguageSpecificData(struct _Unwind_Context *context);
// Эта подпрограмма возвращает адрес области данных для конкретного языка для текущего кадра стека. (LSDA)
uint64 _Unwind_GetRegionStart(struct _Unwind_Context *context);
// Эта подпрограмма возвращает адрес начала процедуры или фрагмента кода, описанного текущим блоком дескриптора разматывания.
/*
гарантируется работа _Unwind_SetGR и _Unwind_SetIP только в индивидуальной функции и только если она потом вернет _URC_INSTALL_CONTEXT
*/

//-----------------------------

void _Unwind_Resume (struct _Unwind_Exception *exception_object);
/*
если посадочная площадка выполнила очистку, но не продолжает нормальное выполнение
должен вызываться тогда и только тогда, когда индивидуальная функция не возвращала _URC_HANDLER_FOUND во время фазы 1.
*/

void _Unwind_DeleteException(struct _Unwind_Exception *exception_object);
/*
если посадочная площадка выполнила обработку исключения (даже иностранного), и оно больше не нужно
(а потом продолжает нормальное выполнение)
*/

// =================================================================================
// CXxAbi


struct __cxa_exception { // заголовок исключения
	std::type_info *	exceptionType;
	void (*exceptionDestructor) (void *); 
	unexpected_handler	unexpectedHandler;
	terminate_handler	terminateHandler;
	
	__cxa_exception *	nextException;
	int					handlerCount;
	
	int				handlerSwitchValue;
	const char *	actionRecord;
	const char *	languageSpecificData;
	void *			catchTemp;
	void *			adjustedPtr;
	/*
		
	*/

	_Unwind_Exception	unwindHeader;
};
// объект исключения идет сразу за этой структурой
// указатель указывает на него

struct __cxa_eh_globals {
	__cxa_exception *	caughtExceptions;
	unsigned int		uncaughtExceptions;
};
__cxa_eh_globals *__cxa_get_globals(void):
__cxa_eh_globals *__cxa_get_globals_fast(void):
// поддерживается для каждого потока

void unexpected();
void terminate();
// ---------------------------

/*
	throw X;
выдаст код, приближающий шаблон:
	// Allocate -- never throws:
	temp1 = __cxa_allocate_exception(sizeof(X));

	// Construct the exception object:
	#if COPY_ELISION
	  [evaluate X into temp1]
	#else
	  [evaluate X into temp2]
	  copy-constructor(temp1, temp2)
	  // Landing Pad L1 if this throws
	#endif

	// Pass the exception object to unwind library:
	__cxa_throw(temp1, type_info<X>, destructor<X>); // Never returns

	// Landing pad for copy constructor:
	L1: __cxa_free_exception(temp1) // never throws
*/

void *__cxa_allocate_exception(size_t thrown_size);
// если не может выделить память - использует буфер
// если не хватает буфера - вызывает terminate()
void __cxa_free_exception(void *thrown_exception);

void __cxa_throw (void *thrown_exception, std::type_info *tinfo, void (*destr) (void *) );
/* никогда не возвращается
__cxa_exception *header = ((__cxa_exception *) thrown_exception - 1);
заполняет unexpectedHandler, terminateHandler, exceptionType, exceptionDestructor, unwindHeader.exception_class
__cxa_get_globals()->uncaughtException++
??? 
	когда и кем будут заполнены unwindHeader.exception_cleanup, nextException, handlerCount ???
_Unwind_RaiseException(thrown_exception)
если что-то вернулось, то terminate() или что-то наподобие
*/

// ---------------------------

_Unwind_Reason_Code 
(*__personality_routine)(
	int version,
	_Unwind_Action actions,
	uint64 exceptionClass,
	struct _Unwind_Exception *exceptionObject,
	struct _Unwind_Context *context
);

// ---------------------------

void *__cxa_get_exception_ptr ( void *exceptionObject );
/* При входе обработчик должен вызвать:
	Эта подпрограмма возвращает скорректированный указатель на объект исключения. 
	(Скорректированный указатель обычно вычисляется процедурой индивидуальности на этапе 1 и сохраняется в объекте исключения.)
*/
void *__cxa_begin_catch ( void *exceptionObject );
/* После инициализации параметра catch обработчик должен вызвать:
	handlerCount++
	помещаем исключение в __cxa_get_globals()->caughtExceptions, если его там нет еще
	__cxa_get_globals()->uncaughtException--
	Возвращает скорректированный указатель на объект исключения.
*/
/*Если инициализация параметра catch тривиальна 
	(например, нет формального параметра catch или у параметра нет конструктора копирования), 
	вызовы __cxa_get_exception_ptr()и __cxa_begin_catch()могут быть объединены в один вызов __cxa_begin_catch().
*/

// если надо, можно вызвать terminate()

// если надо узнать тип исключения, можно вызвать
std::type_info *__cxa_current_exception_type ();

void __cxa_rethrow ();
/* Если собираешься перебрасывать, вызови:
	помечает объект исключения в верхней части стека catchExceptions (определенным реализацией) как переброшенный.
		Если стек catchExceptions пуст, он вызывает terminate()
*/

void __cxa_end_catch ();
/*При выходе по любой причине обработчик должен вызвать:
	Находит последнее обнаруженное исключение и уменьшает его количество обработчиков.
	Удаляет исключение из стека перехваченных исключений, если счетчик обработчиков обнуляется.
	Уничтожает исключение, если счетчик обработчиков обнуляется, и исключение не было переброшено throw.
*/

// если надо - выполняем очистку

// если собирались перебрасывать - вызываем _Unwind_Resume()