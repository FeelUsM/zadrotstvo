=== 0. Preprocessor statement ===
	include

	define
	redefine
	undefine

	условие
		>
		>=
		<
		<=
		= or ==
		!=
		&&
		||
		exists()		существует ли выражение или $-переменная
		isdefined()		определена ли переменная препроцессора
		isfactorized()	факторизовано ли выражение или $-переменная
		isnumerical()	является ли числом выражение или $-переменная
		maxpowerof()	максимальная степень символа, с которой он был объявлен, или общая максимальная степень
		minpowerof()	минимальная степень символа, с которой он был объявлен
		termsin()		количество членов в выражении или $-переменной

	if
	ifdef
	ifndef
	else
	elseif
	endif
	
	switch
	case
	default
	break
	endswitch

	do
	breakdo
	enddo

	procedure
	endprocedure
	call

	inside
	reverseinclude
	endinside
	
	opendictionary
	closedictionary
	usedictionary

	external
	setexternal
	rmexternal
	toexternal
	fromexternal
	setexternalattr

	addseparator
	rmseparator

	system
	pipe

	preout
	write 
	show
	prompt
	printtimes
	message

	appendpath
	prependpath

	add
	append
	create
	remove
	clearoptimize
	close
	commentchar
	exchange
	factdollar
	optimize
	procedureextension
	setrandom
	skipextrasymbols
	timeoutafter

	reset
	terminate
=== 1. Declaration statement ===
	s[ymbols] <list of symbols to be declared>;
		x#r		действительный (по умолчанию)
		x#c		комплексный
		x#i		мнимый
		x#=number	x^number==1; x^(number+1)==x
		x(:5)	x^(number+1)==0
		x(-3:)	x^-(number+1)==0
		x(-3:5) 	

	f[unctions] <list of functions to be declared>; - некоммутирующие
		name#r		The function is considered to be a real function (default).
		name#c		The function is considered to be a complex function. This means that internally two spaces are reserved. One for the variable name and one for its complex conjugate name#.
		name#i		The function is considered to be imaginary.
		name(s[ymmetric])		The function is totally symmetric. This means that during normalization FORM will order the arguments according to its internal notion of order by trying permutations. The result will depend on the order of declaration of variables.
		name(a[ntisymmetric])	The function is totally antisymmetric. This means that during normalization FORM will order the arguments according to its internal notion of order and if the resulting permutation of arguments is odd the coefficient of the term will change sign. The order will depend on the order of declaration of variables.
		name(c[yclesymmetric])	The function is cycle symmetric in all its arguments. This means that during normalization FORM will order the arguments according to its internal notion of order by trying cyclic permutations. The result will depend on the order of declaration of variables.
		name(r[cyclesymmetric)	
		name(r[cyclic])
		name(r[eversecyclic])	The function is reverse cycle symmetric in all its arguments. This means that during normalization FORM will order the arguments according to its internal notion of order by trying cyclic permutations and/or a complete reverse order of all arguments. The result will depend on the order of declaration of variables.
		name<number
		name<=number
		name>number
		name>=number
			The function has a restriction on the number of arguments. If the number of arguments of an occurrence of the function is not fulfilling the condition during normalization FORM will set the term equal to zero.
		примеры:
			f1#i(symmetric)>=4<8;
			f1#i<=8;
	c[functions] <list of functions to be declared>; - коммутирующие
	co[mmuting] <list of functions to be declared>;	- коммутирующие
	n[functions] <list of functions to be declared>; - некоммутирующие

	d[imension] <number or symbol>;	размерность по умолчанию
		для индексов, у которых не указана размерность
		и для фиктивных индексов
		по умолчанию 4
	index, indices < список индексов для объявления > ; 
		name = dim 
			0	индекс не может быть суммирован, и сокращения индекса для этого индекса не выполняются.
			не указан - выбирается утановленный в dimension
		N1_? ... N3_? - фиктивные индексы при выводе
			
	v[ectors] <list of vectors to be declared>;

	t[ensors] <list of tensors to be declared>; - коммутирующие
	ct[ensors] <list of tensors to be declared>; - коммутирующие
	nt[ensors] <list of tensors to be declared>; - некоммутирующие

	auto[declare] < тип переменной > < список объявляемых переменных > ; 
		s[ymbol]
		v[ector]
		i[ndex]
		i[ndices]
		f[unctions]
		nf[unctions]
		cf[unctions]
		co[mmuting]
		t[ensors]
		nt[ensors]
		ct[ensors]

	off <keyword>;
  	off <keyword> <option>;	
		statistics		Turns off the printing of statistics.
		stats			Same as `Off statistics'.

		shortstatistics	Переводит запись статистики из режима стенографии в обычный режим статистики, в котором каждое сообщение статистики занимает три строки текста и одну пустую строку.
		shortstats		Same as `Off shortstatistics'.

		finalstats		Turns off the last line of statistics that is normally printed at the end of the run (introduced in version 3.2).
		processstats	Turns the process by process printing of the statistics in PARFORM off. Only the master process will be printing statistics. Other versions of FORM will ignore this option.
		wtimestats		Disables the wall-clock time in the timing information in the statistics on the master.
		threadstats		Turns off the thread by thread printing of the statistics in TFORM. Only the master thread will be printing statistics. Other versions of FORM will ignore this option.

		oldfactarg		Switches the use of the FactArg statement 7.54 to the new mode of version 4 or later in which expressions in the argument of the mentioned function are completely factored over the rationals. The default is off.

		allnames		Turns the allnames mode off. The default.
		names			Turns the names mode off. This is the default.

		allwarnings		Turns off the printing of all warnings.
		warnings		Turns off the printing of warnings.

		highfirst		Puts the sorting in a low first mode.
		insidefirst		Not active at the moment.
		lowfirst		Leaves the default low first mode and puts the sorting in a high first mode.
		powerfirst		Puts the sorting back into `highfirst' mode.

		checkpoint		Deactivates the checkpoint mechanism. See 4.1.
		compress		Turns compression mode off.
		nospacesinnumbers	Allows very long numbers to be printed with leading blank spaces at the beginning of a new line. The numbers are usually broken up by placing a backslash character at the end of the line and then continuing at the next line. For cosmetic purposes FORM puts usually a few blank spaces at the beginning of the line. FORM itself can read this but some programs cannot. This option can be turned off by the `on nospacesinnumbers;' statement. The printing of the blank characters can be restored by turning this variable off. See also page 17 for a corresponding variable in the setup file.
		parallel		Disallows the running of the program in parallel mode (only relevant for parallel versions of FORM).
		propercount		Turns the propercounting mode off. This means that for the generated terms in the statistics not only the `ground level' terms are counted but also terms that were generated inside function arguments.
		properorder		Turns the properorder mode off. This is the default.
		setup			Switches off the mode in which the setup parameters are printed. This is the default.
		threadloadbalancing		Disables the loadbalancing mechanism of TFORM in parallel mode. In other versions of FORM this option is ignored.
		threads			Disallows multithreaded running in TFORM. In other versions of FORM this option is ignored.
		totalsize		Switches the totalsize mode off. For a more detailed description of the totalsize mode, see the "On TotalSize;" command 7.107.

	on

	table <options> <table to be declared>;
		0 аргументов - разреженная - можно указать количество аргументов
		check		проверка границ массива
		relax		отменяет обязательность заполнения всех элементов
		sparse		разреженная, укажите только количество индексов. Поиск через сбалансированное дерево
		strict		все элементы должны быть заполнены к концу модуля, в котором объявлена таблица
		zerofill	неопределнные элементы считаются 0
		onefill		неопределнные элементы считаются 1
		   Symbol x;
		   Table t1(1:3,-2:4);	
		   Table t2(0:3,0:3,x?);
		   Table sparse,t3(4);	ctable
	ntable
	fill <tableelement> = <expression> [,<moreexpressions>];
	fillexpression

	cleartable
	deallocatetable

	set <set to be declared>[(option)]:<element> [<more elements>];
		sets of symbols, 
		sets of functions, =tables,tensors
		sets of vectors, 
		sets of indices
		sets of numbers.
		int_		This is a set of symbols. It refers to all integer numbers that fit inside a FORM word. 
		pos_		This is a set of symbols. They are the positive integers that fit inside a FORM word. 
		pos0_		A set of symbols. They are all non-negative integers that fit inside a FORM word. 
		neg_		A set of symbols. They are all negative integers that fit inside a FORM word. 
		neg0_		A set of symbols. They are all non-positive integers that fit inside a FORM word. 
		symbol_		The set of all formal symbols. It excludes integers, numbers and whole function arguments. 
		fixed_		The set of all fixed indices. 
		index_		The set of all indices. 
		vector_		The set of all (auto)declared vectors. 
		number_		The set of all rational numbers. 
		even_		This is a set of symbols. It refers to all even integer numbers that fit inside a FORM word. 
		odd_		This is a set of symbols. It refers to all odd integer numbers that fit inside a FORM word. 
		dummyindices_ This is a set of indices. It refers to all indices of the type Nm_? (m a positive integer) that were obtained by summing over indices with a sum statement
		{перечисление через ,}
		{<5} {>4,<=10}
	commuteinset

	polyfun <name of function>;		устанавливает функцию, которая будет считаться коэффициентом
  	polyfun;						сбрасывает такую функцию
	polyratfun						функция с числителем и знаменателем
	moduleoption

	compress
	extrasymbols
	fi [xindex] {< число > : < значение > }; 
	funpowers
	insidefirst
	load
	save
	modulus
	processbucketsize
	propercount
	threadbucketsize
	metric
	unittrace
	write 
	nwrite
=== 2. Specification statement ===
	collect <name of function>;
  	collect <name of function> <name of other function>;
  	collect <name of function> <name of other function> <percentage>;
		как-то собирает polyfun
	drop;
  	drop <list of expressions>;
		данные выражения перестают обрабатываеться, но доступны в rhs
		после окончания данного модуля они удаляются полностью
	ndrop;
  	ndrop <list of expressions>;
		отменяет drop. Применяется так:
			drop; Ndrop f1,f2;
	skip	как drop, только вконце модуля не удаляет
	nskip
	delete
	keep
	hide
	nhide
	unhide
	nunhide
	pushhide
	pophide
	inparallel
	notinparallel
=== 3. Definition statement ===
	l[ocal] <name> = <expression>;
  	l[ocal] <names of expressions>;
		будет утеряно при .store
		можно переопределять глобальные переменные (без =)
	g[lobal] <name> = <expression>;
  	g[lobal] <names of expressions>;
		при .store перестанет быть активным, можно будет использовать справа
		слева от = могут быть параметры, которые можно обойти функцией replace_
		
	gfactorized
	lfactorized
	intohide
=== 4. Executable Statement ===
  	Print [<options>] "<format string>" [<objects>];
		печатает текущий терм
		%t	текущий	 терм со знаком
		%T	текущий	 терм без знака (если +)
		%w	номер текущегог потока
		%W	номер текущегог потока и CPU-time
		%$	$-выражение
		%%	%
		%в конце строки - отключает перенос строки в конце конструкции
		\n	\n

	totensor [nosquare] [functions] [!<vector or set>] <vector> <tensor>;
  	totensor [nosquare] [functions] [!<vector or set>] <tensor> <vector>;
	tovector <tensor> <vector>;
  	tovector <vector> <tensor>;
	contract; 					сворачивает только одну пару леви-чевит
	contract <number>; 			сворачивает так, чтобы осталось n или n+1 леви-чевит
	contract:<number>; 			сворачивает только одну пару леви-чевит и в ней	сворачивает n индексов
	contract:<number> <number>; 
	sum <list of indices>;		сворачивает указанные индексы

	trace4	след гамма-матриц
	tracen	след гамма-матриц
	
	id[entify] [<options>] <pattern> = <expression>;
		function? 	<- function
		tensor?		<- tensor
		index?		<- index
		vector?		<- вне функций: vector
					   как аргумент функции: выражение, где 
						все термы содержат один вектор без индексов
		symbol?		<- вне функций: symbol
					   как аргумент функции: скаларные объекты: 
						символы, числа и выражения, без свободных индексов и векторов без индексов
		?xxx		<- группа аргументов функции
						не работает с симметричными и антисимметричными функциями
						CFunction f(symmetric),ff;
						Multiply replace_(f,ff);
		a?set[n]	{a,b,c} - тоже set
		a?aa?bb	= a	=== a?aa[n] = bb[n]
		
		only		степени должны точно совпадать
		multi		заменяет только единожды в любой степени (по умолчанию?)
		many		работает с каждым термом пока может
		once		заменяет только единожды в любой степени
		ifmatch-> <label>
		ifnomatch->	<label>
		disorder	упорядочивает?
		all			
	ifmatch -> <label> <pattern> = <expression>;
		id ifmatch-> ....
	ifnomatch
		id ifnomatch-> ....
	idnew
	idold
	also
		
  	repeat <executable statement>
	repeat;
	endrepeat;
	while
	endwhile
	do $loopvar = lowvalue,highvalue{,increment};
	enddo

	mu[ltiply] [<option>] <expression>;
		left
		right


	r[edefine] <preprocessor variable> "<string>";
	setexitflag
	exit

	<condition>
		count(symbols/dotproducts/functions/tensors/tables/vectors+vfd,weight)
		match(pattern) -> количество совпадений
		expression(expr1,expr2,...) - совпадает ли хотябы с одним из данных
		occurs(var1,var2,...) - встречается ли хотябы одна переменная в данном терме
		findloop(<replaceloop args>)
		multipleof(x)==y - y делится на x
		<целое число>
		coefficient		коэффициент текущего терма
		$-переменная
	goto
	label
	if ( <condition> );
	if ( <condition> ) <executable statement>
	elseif
	else
	endif
	inexpression,name(s) of expression(s);
		if ( expression(expr) );
	endinexpression
	switch
	case
	default
	endswitch
	break
	
	argument [<argument specifications>] {<name of function/set> [<argument specifications>]};
		если ничего не указано - для всех функций и всех их аргументов
		числа - для данных аргументов всех функций
		функция или множество функций {f1,f2}, после которых номера аргументов - ну ты понел
	endargument;
	factarg options {<name of function/set> [<argument specifications>]};
		раскладывает полином на множители (on/off oldfactarg)
		f(a*b*c) -> f(a,b,c)
		(0) - удаляет коэффициент
		(-1)- коэффициент объединяет со знаком
		(1) - отделяет коэффициент от знака
	splitarg options {<name of function/set> [<argument specifications>]};
		f(a+b+c) -> f(a,b,c)
		(term) - отделяет только термы, кратные данному и помещает их после текущегог аргумента
		((term)) - отделяет только заданный терм и помещает его после текущегог аргумента
	splitfirstarg {<name of function/set> [<argument specifications>]};
		f(a+b+c) -> f(b+c,a)
	splitlastarg {<name of function/set> [<argument specifications>]};
		f(a+b+c) -> f(a+b,c)
	transform,function(s),<one or more transformations>;
		диапозон (r1,r2) - (1,4) (2,last) (last-6, last-2)

		raplace(r1,r2)=(x1,y1,x2,y2,...)	mul replace_(x1,y1,x2,y2,...)
		permute(1,3,5)(2,6)					применяет циклы
		reverse(r1,r2)
		dedup(r1,r2)						удаляет дубликаты
		cycle(r1,r2)=+/-num
		addargs(r1,r2)						см splitarg
		mulargs(r1,r2)						см factarg
		dropargs(r1,r2)
		selectargs(r1,r2)					drop все кроме seleted

		encode(r1,r2):base=num				
		decode(r1,r2):base=num
		implode(r1,r2) 						см argexplode
		explode(r1,r2) 						см argimplode
		islindon(r1,r2)=(yes,no)
		tolindon(r1,r2)=(yes,no)
	argexplode
	argimplode
	symm[etrize] {<name of function/tensor> [<argument specifications>];}
		сортирует аргументы функции
	antisymmetrize
		сртирует рагументы, и каждая перестановка добавляет множитель -1
	cyclesymmetrize
		приводит в наиболее упорядоченную форму путем циклической перестановки
		см transform islindon
	rcyclesymmetrize
		приводит в наиболее упорядоченную форму путем циклической перестановки и реверса
		
	dis[card];	- выкидывает текущий терм
	

	inside
	endinside

	term;		- текущий терм начинает рассматриваться как выражение
	sort;		- как .sort, только внутри term
	endterm


	copyspectator
	createspectator
	emptyspectator
	tospectator
	removespectator

	frompolynomial
	topolynomial

	putinside
	antiputinside

	apply
	argtoextrasymbol
	chainin
	chainout
	chisholm
	denominators
	disorder
	dropcoefficient
	dropsymbols
	factdollar
	makeinteger
	many
	merge
	multi
	normalize
	once
	only
	ratio
	renumber
	select
	shuffle
	stuffle
	testuse

	replaceloop
	tryreplace


=== 5. Output control statement ===
	b[rackets][+][-] <list of names>;	вынести за скобки указанное
	ab[rackets]   [+][-] <list of names>;	
	antib[rackets][+][-] <list of names>;	вынести за скобки всё кроме указанного

	fo[rmat] <option>;

	Print [<options>];
  	Print {[<options>] <expression>};
		+f	печатать только в лог-файл
		-f	(default) печатать и в stdout и в logfile
		+s 	каждый терм на новой строке (single term mode)
		+ss	каждый терм и каждая группа терма с новой строки
		+sss каждый символ с новой строки
	print[] {[<options>] <name>};
		в скобках печатает не их содержимое, а количество термов
	np[rint] <list of names of expressions>;
		наподобие nskip

	factorize
	unfactorize
	nfactorize
	nunfactorize

	printtable



tablebase

.sort 	continue
.global	защищает объявления (declarations) от удаления .store
.store 	store globals, remove locals, continue, а также удаляет объявления (declarations)
см также Specification statement: skip,nskip,drop,ndrop
.clear 	restart softly
.end 	terminate


Functions
	i_
	pi_

	abs_(x) 		absolute value
	exp_
	bernoulli_(n) 	Bernoulli number		t/(1-exp(-t)) = sum_n bernoulli_(n)*t^n
	binom_(n,k)		binomial coefficient	n!/k!(n-k)!
	delta_(x) 		delta function			1 if x==0 else 0
	delta_(x,y) 	delta function			1 if x==y else 0
	deltap_(x) 		delta prime function	0 if x==0 else 1
	deltap_(x,y) 	delta prime function	0 if x==y else 1
	fac_(n) 		factorial				n!
	invfac_(n) 		inverse factorial		1/n!
	max_, min_(...)	maximum and minimum value
	mod_(n,k) 		modulo arithmetic of integers
	mod2_
	div_
	root_(n,x)		root function			
	sig_(x) 		sign function			1 if x>=0 else -1
	sign_(n) 		signature for integers	(-1)^n
	theta_(x) 		theta function			1 if x>=0 else 0
	theta_(x,y)		theta function			1 if x>=y else 0
	thetap_(x) 		theta prime function	1 if x>0 else 0
	thetap_(x,y)	theta prime function	1 if x>y else 0

	d_(i,j)			kronecker delta
	e_(i,j,k,...)	levi-chevita
	dd_(i,j,k,l,...)четное (even) количество индексов - полностью симметричный тензор, составленный из d_

	gi_(i)				едининая
	g_(i,mu,..)
	g5_(i) = g_(i,5_)
	g6_(i) = g_(i,6_)
	g7_(i) = g_(i,7_)
						i-спиновый индекс

	sum_(symbol,start,stop,expr)
	sum_(symbol,start,stop,step,expr)
	gcd_(x1,x2,...)	НОД, аргументы могут быть выражениями
	coeff_			коэффициент текущего терма
	num_			числитель коэффициента текущего терма
	den_			знаменатель коэффициента текущего терма
	extrasymbols_	...
	
	replace_(a,b,c,d,...)множитель терма - заменяет в терме все вхождения a на b, c на d,...
	reverse_		аргумент функции - заменяется аргументами функции в обратном порядке
	factorin_		
	firstbracket_(exprname)
	firstterm_(exprname)
	id_
	integer_
	inverse_
	makerational_
	match_
	maxpowerof_
	minpowerof_
	mul_
	nargs_
	node_
	nterms_
	numfactors_
	partitions_
	pattern_
	perm_
	poly_
	prime_
	putfirst_
	random_
	ranperm_
	rem_
	setfun_
	sump_
	table_
	tbl_
	term_
	termsin_
	termsinbracket_
	topologies_
	conjg_
	content_
	count_
	denom_
	distrib_
	dum_
	dummy_
	dummyten_
	exteuclidean_
	extrasymbol_
	
	farg_			только для внутреннего пользования

	---
	sqrt_	The regular square root.
	sin_	The sine function.
	cos_	The cosine function.
	tan_	The tangent function.
	asin_	The inverse of the sine function.
	acos_	The inverse of the cosine function.
	atan_	The inverse of the tangent function.
	atan2_	Another inverse of the tangent function.
	sinh_	The hyperbolic sine function.
	cosh_	The hyperbolic cosine function.
	tanh_	The hyperbolic tangent function.
	asinh_	The inverse of the hyperbolic sine function.
	acosh_	The inverse of the hyperbolic cosine function.
	atanh_	The inverse of the hyperbolic tangent function.
	ln_		The natural logarithm.
	li2_	The dilogarithm function.
	lin_	The polylogarithm function.	

Параметры (setup)




	Define										инструкция препроцессора

	Variable 			32-bits 	64-bits

	path 				. 			.
	IncDir 				. 			.			files for the #include and #call instructions
	tempdir 			. 			.
	tempsortdir 		. 			.

	CommentChar 		$*$ 		$*$
	DotChar 			. 			.			when dotproducts are printed in Fortran output
	ContinuationLines 	15 			15			Format Fortran

	nwriteFinalStatistics OFF 		OFF
	nwriteStatistics 	OFF 		OFF
	nwriteThreadStatistics OFF 		OFF

	InsideFirst 		ON 			ON			files for the #include and #call instructions
	noSpacesInNumbers 	OFF 		OFF			пробелы вначчале строк при переносах длинных чисел
	oldorder 			OFF 		OFF
	sorttype 			lowfirst 	lowfirst

	BracketIndexSize	200000 		200000		раздел "скобки" и Output control statement "bracket"
	ConstIndex 			128 		128			максимальный индекс как число
	FunctionLevels 		30 			30			when functions have functions in their arguments
	MaxWildCards 		100 		100			количество шаблонов при одном сопоставлении паттерна
	filepatches 		256 		256
	largepatches 		256 		256

	CompressSize 		90000 		90000		compression buffer size
	HideSize 			50000000 	50000000
	termsinsmall 		100000 		100000
	smallsize 			10000000 	10000000
	smallextension 		20000000 	20000000
	largesize 			50000000 	50000000	размер большого буфера
	
	MaxNumberSize 		200 		200			максимум MaxTermSize/2
	MaxTermSize 		10000 		40000		
	workspace 			10000000 	40000000	размер кучи для алгебраического препроцессора, когда тот вычисляет дерево подстановок

	numstorecaches 		4 			4
	parentheses 		100 		100
	processbucketsize 	1000 		1000
	scratchsize 		50000000 	50000000
	sizestorecache 		32768 		32768
	sortiosize 			100000 		100000

	subfilepatches 		64 			64
	sublargepatches 	64 			64
	sublargesize 		4000000 	4000000
	subsmallextension 	800000 		800000
	subsmallsize 		500000 		500000
	subsortiosize 		32768 		32768
	subtermsinsmall 	10000 		10000

	threadbucketsize 	500 		500
	threadscratchoutsize 2500000 	2500000
	threadscratchsize 	100000 		100000

	JumpRatio									See the endswitch (7.49) statement
	threads 			0 			0
	threadLoadBalancing ON 			ON
	threadSortFileSynch OFF 		OFF





При запуске FORM-а в него встроен ряд настроек, которые были определены во время его установки. 
Если пользователь хочет изменить эти настройки, можно либо указать их желаемые значения в файле настройки, либо сделать это в начале файла программы. 
Существует два способа, с помощью которых FORM может найти установочный файл. 
Первый способ - создать файл с именем "form.set" в текущем каталоге. 
Если такой файл присутствует, FORM откроет его и интерпретирует его содержимое как параметры настройки. 
Если этот файл отсутствует, можно указать установочный файл с параметром -s в хвосте команды. 
Этот параметр должен предшествовать имени входного файла. 
После -s следует один или несколько пробелов или табуляций, а затем полное имя файла установки. 
FORM попытается прочитать параметры запуска из этого файла. 
Если файл "form.set" присутствует, FORM проигнорирует параметр -s и соответствующее имя файла. 
Этот порядок интерпретации позволяет пользователю определить псевдоним с помощью стандартного файла настройки, который может быть отменен локальным файлом настройки. 
Если в начале файла программы перед любыми другими инструкциями, за исключением #-инструкций и комментариев, есть строки, начинающиеся с #: 
	оставшееся содержимое этих строк интерпретируется точно так же, как строки в файле установки. 
Спецификации в файле программы имеют приоритет над всеми другими спецификациями. 
Если ни один из вышеперечисленных методов не используется, FORM будет использовать встроенный набор параметров. 
Их значения могут зависеть от установки и приведены ниже.


Ниже приведен список параметров, которые можно задать. 
Синтаксис довольно прост: должно быть указано полное слово (без учета регистра), за которым следует один или несколько пробелов или табуляций и желаемое число, строка или символ.
Все, что после этого, считается комментарием. 
В файле установки строки, которые не начинаются с буквенного символа, рассматриваются как комментарий. 
Размеры буферов указаны в байтах, если не указано иное. 
Слово составляет 2 байта для 32-разрядных машин и 4 байта для 64-разрядных машин.

В FORM-е версии 3.3 и более поздних версий также разрешено определять переменные препроцессора (см. также 3.1) в файле установки. 
Кроме того, в настройках можно использовать переменные препроцессора, если это не указано в имени параметра/ключевого слова.

--- системное ---
	Переменные, которые принимают путь для своего значения, ожидают последовательности каталогов, разделенных символами двоеточия, как в UNIX для определения таких объектов.
	InsideFirst							ON 	ON
		В данный момент это не имеет никакого эффекта.
	Define - Определять
		Синтаксис такой же, как в инструкции #define в препроцессоре (см. 3.1), с замечанием, что в файле установки не должно быть ведущего символа #, так как это превратило бы строку в комментарий. 
		Пример:
			define MODULUS "31991"
		который может быть использован на более позднем этапе программы для активации оператора modulus (см. 7.90).
	TempDir - ТемпДир						. 	.
		Эта переменная должна содержать имя каталога, то есть каталога, в котором FORM должен создавать свои временные файлы. 
		Если при запуске FORM-а используется параметр -t, переменная TempDir в файле установки игнорируется. 
		FORM может создавать несколько различных временных файлов.
	TempSortDir - ТемпСортДир					. 	.
		Эта переменная должна содержать имя каталога, который является каталогом, в котором FORM должен создавать свои временные файлы сортировки. 
		Если при запуске FORM-а используется параметр -ts, переменная TempSortDir в файле установки игнорируется. 
		Если TempSortDir не указан, то значение TEMPDIR используется также для сортировки файлов.
	IncDir								. 	.
		Каталог (или путь к каталогам), в котором FORM будет искать файлы, если их нет в текущем каталоге. 
		Это включает файлы для инструкций #include и #call. 
		Эта переменная имеет приоритет над переменной Path.
	Path - Путь							. 	.
		Каталог (или путь к каталогам), в котором FORM будет искать файлы, если их нет в текущем каталоге. 
		Это включает файлы для инструкций #include и #call. 
		ФОРМА проверит этот путь после потенциального пути, указанного как IncDir.
	ProcedureExtension - Продление процедуры
		Расширение, которое будет использоваться FORM-ом для поиска процедур, находящихся в отдельных файлах. 
		Ограничения на используемые строки приведены в инструкции препроцессора #proceduresextension в разделе 3.44.
	commentchar - Символ комментария				$*$ 	$*$
		За этим должен следовать один или несколько пробелов и один непустой символ. 
		Этот символ будет использоваться для обозначения комментария вместо обычного $*$ в столбце 1.
		$*$ 	$*$
	OldOrder - Старый Порядок					OFF 	OFF
		Специальный флаг (значения ВКЛ/ВЫКЛ), с помощью которого все еще можно выбрать старую опцию не проверять порядок инструкций внутри модуля. 
		Это следует использовать только в том случае, если практически невозможно перевести программу в новый режим, в котором важен порядок инструкций (объявлений и т.д.). 
		В будущем этот старый режим может и не существовать.
		OFF 	OFF
--- вывод ---
	DotChar - Дотчар						. 	.
		После этого имени должен быть один символ (и пробелы после него). 
		Этот символ будет использоваться вместо _, когда точечные продукты печатаются в выводе Fortran. 
		Этот параметр необходим, поскольку некоторые компиляторы Fortran не распознают подчеркивание как допустимый символ. 
		В былые времена здесь можно было использовать символ доллара, но в настоящее время многие компиляторы Fortran не распознают этот символ как принадлежащий имени переменной.
	SortType - Тип сортировки					lowfirst 	lowfirst
		Возможные значения: "lowfirst", "highfirst" и "highfirst". 
		"lowfirst" - это значение по умолчанию. 
		Определяет порядок, в котором термы размещаются во время сортировки. 
		В случае lowfirst, более низкие степени символов и точечных продуктов предшествуют более высоким степеням. 
		В случае с highfirst все наоборот. 
		В случае powerfirst рассматриваются объединенные степеней всех символов вместе, и на первом месте стоят высшие объединенные степени. 
		См. также заявление on в 7.107. (highfirst, lowfirst, powerfirst)
	NoSpacesInNumbers - В Числах Нет Пробелов			OFF 	OFF
		Длинные числа обычно распределяются по нескольким строкам, помещая символ пробела в конце каждой строки, а затем переходя к следующей строке. 
		В косметических целях FORM обычно помещает несколько пробелов в начале новой строки. Сам FORM может прочитать это, но некоторые программы не могут. 
		Следовательно, можно перевести FORM в режим, в котором эти пробелы опущены. 
		Значения переменной могут быть включены или выключены. 
		Существует также команда для изменения этого поведения во время выполнения. 
		Смотрите команды nospacesinnumbers включения и выключения в разделах 7.107 и 7.106.
	ContinuationLines - Линии продолжения				15 	15
		Количество строк продолжения, разрешенных локальным компилятором Fortran. 
		Это ограничивает количество строк продолжения, когда выбран параметр вывода "Format Fortran" (см. 7.60 (format)).
	ResetTimeOnClear - Сбросить Время при Очистке			ON	ON
		Значение ВКЛЮЧЕНО или ВЫКЛЮЧЕНО. Значение по умолчанию включено. 
		Это означает, что по умолчанию часы сбрасываются после каждой инструкции .очистить (см. главу 4 о модулях) в конце модуля.
	nwritefinalstatistics						OFF 	OFF
	NwriteStatistics - не Записывать статистику			OFF 	OFF
		При упоминании этого слова по умолчанию для статистики устанавливается, что статистика времени выполнения отображаться не будет. Обычно они будут показаны.
	NwriteThreadStatistics - не писать статистику потоков		OFF 	OFF
		Эта переменная имеет значения ВКЛЮЧЕНО или ВЫКЛЮЧЕНО. 
		Она определяет, будет ли печататься статистика отдельных потоков. Значение по умолчанию включено.
	WTimeStats - Статистика времени
		Включает режим времени настенных часов в статистике. 
		Смотрите отчет "On wtimestats" 7.107.
	TotalSize - Общий размер
		Переводит FORM в режим, в котором она пытается определить максимальное пространство, 
			занимаемое всеми выражениями в любой данный момент во время выполнения программы. 
		Это пространство представляет собой сумму файлов ввода/вывода/скрытия, файлов сортировки и файла .str. 
		Этот максимум выводится в конце программы. 
		То же самое можно получить с помощью инструкции "On totalSize" (см. 7.107) или параметра -T в хвосте команды при запуске F (см. 1).
--- параметры алгоритмов ---
	JumpRatio - соотношение прыжков					4	4
		См. инструкцию endswitch (7.49).
		Завершает конструкцию switch. 
		Он собирает различные обращения, упорядочивает их и решает, следует ли выполнять поиск обращений с помощью таблицы переходов или с помощью двоичного поиска. 
		Соотношение (разброс в случаях)/(количество случаев) определяет, будет ли построена таблица переходов. 
		Значение по умолчанию, ниже которого строится таблица переходов, равно 4. 
		Это значение можно изменить в настройках (см. раздел о настройках 17) с помощью переменной jumpratio.
	FunctionLevels - Уровни функций					30 	30
		Максимальное количество уровней, которые могут возникнуть, когда функции имеют функции в своих аргументах.
	Parentheses - Скобки						100 	100
		Максимальное количество вложенных скобок или функций включает функции. 
		Переменная может быть устранена в более поздней версии.
	MaxWildCards - Максимальное количество подстановочных знаков	100 	100
		Максимальное количество подстановочных знаков, которые могут быть активны при одном сопоставлении шаблона. 
		При нормальных обстоятельствах значения по умолчанию 100 должно быть более чем достаточно.
--- размеры элементов ---
	ConstIndex - Индекс Const					128 	128
		Это количество индексов, которые считаются постоянными индексами, как в компонентах фиксированного вектора (так называемые фиксированные индексы). 
		Размер этого параметра не связан с каким-либо пространством массива, но он не должен превышать 1000 на 32-разрядной машине. 
		На 64-битной машине это может пойти значительно дальше.
	bracketindexsize - размер индекса скобки			200K 	200K
		Максимальный размер в байтах любого отдельного индекса выражения, заключенного в квадратные скобки. 
		Каждое выражение будет иметь свой собственный индекс. 
		Индекс начинается с относительно небольшого размера и при необходимости будет расти. 
		Но он никогда не вырастет за пределы указанного размера. 
		Если требуется больше места, FORM начнет пропускать скобки и найдет их позже с помощью линейного поиска. См. также главу 9 (bracketindexsize) и раздел 7.11 (bracket).
	MaxNumberSize - Максимальный Размер Чисел			200 	200
		Позволяет установить максимальный размер чисел в FORM-е. 
		Число должен быть указан прописью. 
		Для 32-разрядных систем слово составляет два байта, а для 64-разрядных систем слово составляет 4 байта. 
		Размер числа всегда ограничен максимальным размером термов (см. MaxTermSize). 
		На самом деле он должен быть меньше половины максимального размера, потому что коэффициент содержит как числитель, так и знаменатель. 
		Не всегда рекомендуется иметь максимальное значение размера числа, особенно когда MaxTermSize большой. 
		В этом случае может пройти очень много времени, прежде чем беглый алгоритм столкнется с ограничениями по размеру 
			(арифметика для очень длинных дробей не очень быстрая из-за постоянной необходимости вычисления GCD)
	MaxTermSize - Максимальный размер терма				10K 	40K
		Это максимальный размер, который может занимать отдельный терм в словах. 
		Этот размер не влияет ни на какие распределения. 
		Однако следует понимать, что чем больше этот размер, тем больший спрос может быть на рабочую область, 
			потому что рабочая область действует как куча во время выполнения, и иногда распределение должно быть произведено заранее, 
			прежде чем FORM узнает, каков фактический размер терма будет. 
		Следовательно, дерево оценки не может быть очень глубоким, когда рабочее пространство/максимальный размер не очень велик. 
		MaxTermSize в основном контролирует, как скоро FORM начнет жаловаться на слишком сложные термы. 
		Его абсолютный максимум составляет 32568 в 32-разрядных системах и около 10^9 в 64-разрядных системах 
			(конечно, рабочее пространство должно быть значительно больше этого....).
	NumStoreCaches - Кэш-память Num Store				4 	4
		Это число определяет, сколько будет храниться кэшей (см. Описание параметра настройки SizeStoreCache ниже). 
		В случае параллельной обработки это будет количество кэшей на процессор.
	SizeStoreCache - Размер Кэша Хранилища				32K	32K
		Размер кэшей, которые используются для чтения термов, когда сохраненные выражения используются в r.h.s. инструкции. 
		Обычно таких кэшей несколько, и они значительно ускоряют чтение. 
		В случае параллельной обработки эти кэши становятся очень важными, 
			потому что без них разные процессы могут захотеть одновременно читать из файла .str, и скорость выполнения сильно пострадает. 
		Количество кэшей хранилища определяется параметром NumStoreCaches, который описан выше. 
		Размер этих кэшей не должен быть очень большим по сравнению с некоторыми другими буферами. 
		Рекомендуется, однако, чтобы они были по крайней мере такого же размера, как MaxTermSize (см. Выше).
--- размеры буферов ---
	CompressSize - Размер сжатия					90K 	90K
		При сжатии выходных термов FORM-у требуется буфер сжатия. 
		Этот буфер рекурсивно обрабатывает сжатие и распаковку термов, которые либо записываются, либо считываются. 
		Его размер будет по крайней мере максимальным, но при интенсивном использовании выражений в правой части определений или подстановки он должен быть значительно длиннее. 
		Есть надежда, что в будущем этот параметр можно будет устранить. 
		Размер сжатия должен быть указан в байтах.
	HideSize - Размер Скрытия					50M	50M
		Размер буфера скрытия. 
		Размер этого буфера обычно устанавливается равным scratchsize  (см. Ниже). 
		Если использовать настройку HideSize после настройки scratchsize, можно присвоить буферу скрытия его собственный размер. 
		Бывают случаи, когда это может ускорить работу программы.
	ScratchSize - Размер исходника					50M 	50M
		Размер входного и выходного буферов для обычной обработки алгебры. 
		Термы считываются фрагментами такого размера и записываются в выходной файл с использованием буферов такого размера. 
		Существует два или три таких буфера, в зависимости от того, используется ли средство скрытия (см. 7.67 (hide)). 
		Эти буферы должны иметь размер, по крайней мере, равный MaxTermSize. 
		Эти буферы действуют как кэш для файлов с расширением .sc1, .sc2 и.sc3. 
		Смотрите также параметр HideSize выше для независимой настройки размера буфера скрытия.
	WorkSpace - рабочее место					10M 	40M
		Размер кучи, используемой процессором алгебры при оценке дерева подстановок. 
		Он будет содержать термы, незаконченные термы и другую информацию. 
		Размер рабочей области может быть ограничением глубины дерева подстановок.
--- многопоточность ---		
	ProcessBucketSize - Размер технологического ковша		1000 	1000
		Для параллельной версии PARFORM. Это игнорируется в других версиях. 
		Указывает, сколько термов должно быть в корзинах, которые распределяются по вторичным процессорам. См. также 7.116. (processbucketsize)
	Threads	- Нити							0 	0
		Относится только к TFORM  (см. главу о параллельной версии). 
		Указывает количество используемых рабочих потоков по умолчанию. 
		Значения 0 и 1 будут указывать на то, что запуск будет выполняться только главным потоком (18).
	ThreadLoadBalancing - Балансировка нагрузки на поток		ON 	ON
		Актуально только для TFORM. 
		Возможные значения - ВКЛЮЧЕНО или выключено. 
		Для получения дополнительной информации см. главу о параллельной версии (18).
	ThreadBucketSize - Размер ковша с потока			500 	500
		Актуально только для TFORM. 
		Размер количества термов, отправляемых работникам одновременно. 
		Для получения дополнительной информации см. главу о параллельной версии (18) (The parallel version).
	ThreadScratchOutSize - 						2.5M 	2.5M
		Размер выходных исходных буферов для каждого из рабочих потоков. 
		Эти буферы будут использоваться, когда активен оператор InParallel 7.76. 
		Они используются для получения выходных данных выражений, обработанных отдельными рабочими, прежде чем они будут скопированы в выходной буфер/файл мастера. 
		Выходной исходный буфер/файл каждого рабочего никогда не будет содержать более одного выражения одновременно.
	ThreadScratchSize - 						100K	100K
		Размер входных исходных буферов для каждого из рабочих потоков. 
		Эти буферы используются только в том случае, если основных буферов очистки основного процесса недостаточно и были созданы файлы очистки. 
		Когда буферы ведущего устройства достаточно велики, рабочие используют только указатели на буфер ведущего устройства. 
		Как только появляются файлы с нуля, буфер используется для кэширования входных данных из этих файлов. 
		В этом случае у каждого работника есть свой собственный кэш. 
		Для целей чтения это может быть на самом деле контрпродуктивно, если эти буферы очень большие. 
		Этот параметр задает значение для входных и скрытых файлов. 
		Выходной размер  для рабочих задается с помощью параметра ThreadScratchOutSize.
--- сортировка и статистика ---
Вышеуказанные параметры концептуально относительно просты. 
Параметры, которые все еще остаются, более сложны и часто ограничены по размеру некоторыми отношениями. 
Следовательно, необходимо немного разобраться в сортировке внутри FORM-а, прежде чем использовать их. 
С другой стороны, эти параметры могут заметно повлиять на производительность. 
См. также главу 16 (Sorting and statistics) для получения более подробной информации.
------------
Система сортировки является жизненно важной частью ФОРМЫ и одной из главных причин, по которой скорость ФОРМЫ так выгодно отличается от других систем. 
Хорошее понимание того, что происходит во время сортировки выражений, необходимо, если вы хотите писать эффективные программы. 
По сути, сортировка выполняется сортировкой по дереву. 
Однако из-за природы математических выражений возникает сложность. 
Когда два члена идентичны, с возможным исключением их коэффициента, 
	мы добавим их коэффициенты, поместим этот новый коэффициент вместо коэффициента первого члена и отбросим второй член. 
Если новый коэффициент оказывается равным нулю, оба терма отбрасываются. 
Следовательно, количество термов во время сортировки не является фиксированным. 
Для сортировки деревом это не является серьезным осложнением. 
Что еще более раздражает, так это то, что новый коэффициент может занимать больше места в хранилище, чем любой из старых коэффициентов. 
Давайте теперь посмотрим, что происходит в программе ФОРМЫ. Многое можно увидеть из статистики.

    S	x1,...,x4;
    L	F = (x1+...+x4)^4;
    .end

Time =       0.01 sec    Generated terms =         35
                F        Terms in output =         35
                         Bytes used      =        628
			
В этом случае программа сгенерировала 35 термов. 
Всякий раз, когда создался терм и с ним выполняелась ФОРМА (больше никакие операторы не будут действовать на него), ФОРМА запишет его в буфер, который называется малым буфером. 
Кроме того, он хранит указатель на местоположение этого терма внутри малого буфера. 
Далее он продолжит генерировать термы. Этот процесс будет остановлен одним из трех условий:

    1. ФОРМА закончила генерировать термы.
    2. Последний сгенерированный терм не помещается в пространство, оставшееся в малом буфере.
    3. В массиве указателей нет места для указателя на последний сгенерированный терм.
   
В любом из этих трех случаев ФОРМА будет сортировать содержимое малого буфера. 
Эта сортировка выполняется "по указателям", и поэтому важно, чтобы весь небольшой буфер помещался в физическую память компьютера. 
Если бы это было не так, результатом могла бы стать очень неэффективная замена памяти. 
Во время этой сортировки ФОРМА может столкнуться с проблемой, заключающейся в том, 
	что коэффициент из двух объединенных терминов не помещается на место одного из двух старых коэффициентов. 
Это означает, что объединенному терму потребуется больше места, но поскольку старые термы могут быть окружены другими термами, это пространство может быть недоступно локально. 
Для этого у ФОРМЫ есть некоторое свободное пространство в малом буфере, который называется малым расширением. 
На самом деле термин SmallExtension используется для обозначения сочетания малого буфера и его дополнительного пространства. 
Дополнительное пространство по меньшей мере в 1/6 раза превышает размер малого буфера, но обычно оно составляет около 1/3 размера малого буфера. 
!!!!!! В некоторых исключительных случаях (при интенсивном использовании полиномиального коэффициента с помощью команды PolyFun) могут быть полезны большие размеры.


В случае, если новому объединенному терму требуется больше места, чем для каждого из старых термин, новый терм помещается в пространство расширения. 
Если во время сортировки пространство расширения будет исчерпано, ФОРМА выполнит сборку мусора всего расширенного малого буфера. 
Это всегда приведет к тому, что пространство расширения снова станет пустым, потому что обозначения термов в ФОРМЕ таковы, что новый объединенный терм будет занимать максимум пространство, равное сумме пространств исходных двух термов. 
В более старых версиях ФОРМЫ эта сборка мусора выполнялась с помощью временного файла на диске. 
В новой версии это делается внутри памяти путем временного выделения нового буфера. 
В любом случае, такие сборки мусора относительно редки.

В приведенном выше примере сортировка произошла из-за того, что генерация термов была завершена. 
Следовательно, отсортированная информация записывается таким образом, 
	чтобы ее можно было использовать в качестве входных данных для потенциального следующего модуля (или для печати). 
Следовательно, давайте изменим размер малого буфера:

    #: SmallSize 300
    S	x1,...,x4;
    L	F = (x1+...+x4)^4;
    .end

Time =       0.00 sec    Generated terms =         13
                F      1 Terms left      =         13
                         Bytes used      =        236

Time =       0.00 sec    Generated terms =         26
                F      1 Terms left      =         26
                         Bytes used      =        476

Time =       0.00 sec    Generated terms =         35
                F      1 Terms left      =         35
                         Bytes used      =        632

Time =       0.00 sec    Generated terms =         35
                F        Terms in output =         35
                         Bytes used      =        628
			 
Теперь размер малого буфера будет составлять всего 300 байт. 
В результате 13-й терм не подходит. 
Мы можем видеть это в статистике: 13-й терм сгенерирован, и ФОРМА сортирует малый буфер. 
Выходные данные 12 отсортированных термов записываются в другой буфер, называемый большим буфером. 
Внутри большого буфера термы слегка сжаты. 
Это сжатие связано с тем фактом, что в каждом "патче" термы уже отсортированы, и, следовательно, нам, возможно, не придется повторять одинаковые начала каждого терма. 
Следовательно, объем пространства, используемого после такой сортировки, меньше 300 байт малого буфера, хотя 13-й терм дал переполнение для этих 300 байт. 
Малый буфер снова заполняется на 26-м терме, и снова он сортируется, а результаты записываются в большой буфер. 
Наконец, по прошествии 35 термов, генерация завершена. 
Следовательно, остатки в малом буфере также сортируются и записываются в виде третьего "патча" в большой буфер. 
Затем сортируется большой буфер. 
Для этого используется другая техника сортировки. 
Предполагается, что большой буфер не всегда находится внутри физической памяти. 
Следовательно, его части могут быть временно заменены с диска. 
С размером памяти наших дней это может происходить не очень часто, если только размер буфера не будет сопоставим с размером памяти компьютера 
	и несколько программ не будут запущены одновременно. 
В любом случае, замена не сильно повлияет на большой буфер. 
ФОРМА объединит "исправления", последовательно пройдя через них с помощью метода, называемого "дерево неудачников" в книге Кнута (искусство компьютерного программирования, том 3). 
Поскольку он последовательно проходит через исправления, использует всю считываемую информацию и больше никогда в ней не нуждается, этот метод действительно довольно устойчив к замене.

Следующее осложнение, конечно, возникает, когда большой буфер заполнен. 
Это может быть либо потому, что его байтовое пространство заполнено, либо потому, что превышено максимальное количество исправлений. 
Поскольку метод сортировки использует довольно много переменных для каждого патча, для них выделяется место, и, следовательно, существует максимальное количество патчей. 
Если мы установим это значение равным 2 (только для демонстрационных целей), мы получим:

    #: SmallSize 200
    #: LargePatches 2
    S	x1,...,x4;
    L	F = (x1+...+x4)^4;
    .end

Time =       0.00 sec    Generated terms =          9
                F      1 Terms left      =          9
                         Bytes used      =        164

Time =       0.00 sec    Generated terms =         17
                F      1 Terms left      =         17
                         Bytes used      =        312

Time =       0.00 sec    Generated terms =         26
                F      1 Terms left      =         26
                         Bytes used      =        478

Time =       0.00 sec
                F        Terms active    =         26
                         Bytes used      =        474

Time =       0.00 sec    Generated terms =         35
                F      1 Terms left      =         35
                         Bytes used      =        630

Time =       0.00 sec
                F        Terms active    =         35
                         Bytes used      =        786

Time =       0.00 sec    Generated terms =         35
                F        Terms in output =         35
                         Bytes used      =        628
			 
Мы видим, что после третьей сортировки малого буфера третий патч не может быть записан в большой буфер. 
Следовательно, большой буфер сортируется (указывается специальной статистикой, включающей фразу "Активные термы"). 
Результат этого записывается в виде отсортированного патча в файл сортировки. 
Этот файл является одним из временных файлов, которые может создавать ФОРМА. Он имеет расширение.sor. 
Теперь третий патч можно записать в уже пустой большой буфер. 
В конце генерации термов последний малый буфер сортируется, его результаты записываются в большой буфер, затем он сортируется, а его результаты записываются в виде окончательного исправления в файл сортировки. 
Затем, наконец, исправления в файле сортировки объединяются методом, аналогичным способу сортировки большого буфера. 
Эта заключительная сортировка представляет собой сортировку с диска на диск. 
Следовательно, он может использовать диск довольно интенсивно, и использование процессора может временно снизиться, хотя это не так драматично, как когда компьютер вовлечен в тяжелую неэффективную замену с диска, как это может быть в случае со многими другими программами алгебры. 
Кроме того, обычно это составляет лишь небольшую часть времени выполнения программы. 
Исключением может быть случай, когда FORM запускает несколько процессов, и все они одновременно используют сортировку дисков. 
В этом случае некоторые файловые системы могут не очень хорошо справляться с возникающими пробками.

Кроме того, сортировка с диска на диск будет содержать максимальное количество исправлений, которые могут быть отсортированы одновременно. 
Если это число будет превышено, в сортировке будет один или несколько дополнительных этапов, все из которых будут сортироваться с диска на диск. 
Желательно настроить параметры настройки таким образом, чтобы можно было предотвратить это, поскольку обычно это связано с ненужным использованием ресурсов. 
Можно попытаться увеличить наборы файлов параметров, но проблема в том, что ФОРМА использует систему кэширования для буферизации входных данных из файла сортировки. 
Буферы кэша должны иметь размер, как минимум в два раза превышающий максимальный размер терма. 
Для каждого патча ему нужен буфер, и все буферы вместе должны вписываться в комбинацию большого буфера и малого расширенного буфера. 
Это накладывает верхний предел на количество исправлений файлов. 
Кроме того, этот буфер (сортировка) не должен быть очень маленьким, потому что в противном случае операции ввода-вывода на диске будут очень неэффективными. 
Следовательно, это часто помогает сначала увеличить размер малого буфера и большого буфера. 
Это дает меньше патчей. Кроме того, это, в свою очередь, может позволить использовать больше исправлений файлов, которые не слишком малы.

Одна вещь, которую можно увидеть сейчас, заключается в том, что если условия нужно отменить или добавить, то выгодно, если это произойдет уже на ранней стадии сортировки. 
Это означает, что наиболее эффективно, если эти термы одновременно окажутся в малом буфере. 
Это должно объяснить пример, приведенный в разделе, посвященном скобкам. 
Таким образом, в большой буфер и/или файл сортировки записывается меньше термов, что означает, что будет использоваться меньше места на диске.

Размеры задействованных буферов могут быть настроены на заданное оборудование. 
Как это делается, объясняется в главе, посвященной настройке 17.

Когда ФОРМА имеет дело с аргументами функций, и если аргумент является многотермовым подвыражением, также необходимо отсортировать такие подвыражения. 
В более старых версиях ФОРМЫ это делалось внутри оставшегося на тот момент пространства малого буфера и его расширения. 
Причина заключалась в том, что такие подвыражения были бы довольно короткими 
	(они должны были бы помещаться внутри аргумента функции и, следовательно, были ограничены максимальным размером терма), 
	а буферное пространство было трудно найти в компьютерах с небольшой памятью. 
В новой версии ФОРМЫ были добавлены другие виды подвыражений: сортировка в среде термов (см. 7.145 (term)) и сортировка $-выражений. 
Оба вида не имеют ограничения на максимальный размер терма. 
Они могут привести к выражениям произвольной длины (хотя это может не дать эффективных программ). 
Следовательно, сортировка подвыражений теперь имеет свои собственные буферы. 
И может потребоваться более одного такого набора, если, например, среда терма используется вложенным образом. 
Конечно, настройки для буферов этой "подсортировки" не так велики, как для основных буферов. 
И пользователь, конечно, может также влиять на их настройки, как описано в главе о настройке 17. 
В этой главе также приведены все значения по умолчанию.

Когда ФОРМА выполняется в параллельном режиме (либо TFORM , либо PARFORM), каждому работнику понадобятся свои собственные буферы. 
В PARFORM, в которой каждый процессор управляет своей собственной памятью, размер каждого из этих буферов такой же, как и для основного процесса. 
В TFORM с разделяемой памятью размеры, которые пользователь выбирает для буферов сортировки, и кэширование файлов с нуля относятся к буферам главного потока. 
Каждый из работников получает в основном буферы, размер которых в 1/N раз превышает размер буфера ведущего устройства. 
Они могут быть немного увеличены при возникновении потенциальных конфликтов с MaxTermSize.
-----------
Когда термы отправляются на "вывод" основным механизмом алгебры, они помещаются в буфер. 
Этот буфер называется "малым буфером". Его размер определяется переменной SmallSize. 
Когда этот буфер заполнен или когда количество термов в этом буфере превышает заданный максимум, указанный переменной TermsInSmall, содержимое буфера сортируется. 
Сортировка выполняется по указателям, поэтому важно, чтобы малый буфер находился внутри физической памяти. 
Во время сортировки может случиться так, что будут добавлены коэффициенты. 
Сумма двух рациональных чисел может занимать больше места, чем любое из отдельных чисел, поэтому возникнет проблема с пространством. 
Это было решено путем создания расширения для малого буфера. Переменное SmallExtension - это размер малого буфера вместе с этим расширением. 
Значение для SmallExtension  всегда будет как минимум в 7/6 раз больше значения SmallSize.
TermsInSmall
SmallSize
SmallExtension

Результат сортировки малого буфера записывается в "большой буфер" (с размером большего размера) в виде одного объекта, и заполнение малого буфера может возобновиться. 
Всякий раз, когда в большом буфере недостаточно места для результата сортировки малого буфера, 
	или когда в нем уже есть заданное количество этих отсортированных "исправлений" (управляемых переменной LargePatches), 
	буфер будет отсортирован путем объединения исправлений, чтобы освободить место для новых результатов. 
Выходные данные записываются в файл сортировки в виде одного патча. 
Затем результаты из малого буфера могут быть записаны в большой буфер. 
Эта игра может продолжаться до тех пор, пока будут сгенерированы новые термы. 
В конце концов, необходимо будет отсортировать результаты в промежуточном файле сортировки. 
Это может быть сделано одновременно с несколькими пакетами файлов. 
Поскольку операции с файлами, как известно, очень медленные, комбинация малого буфера, малого расширения и большого буфера используется для целей кэширования. 
Следовательно, это пространство может быть разделено на кэши "Пакетов файлов". 
Ограничение состоит в том, что каждый кэш должен быть способен содержать по крайней мере два члена максимального размера. 
Это означает, что сумма малых расширений и больших размеров должна быть не менее 2*maxtermsize* (байт в коротком целочисленном формате). 
Размер этих кэшей можно задать непосредственно с помощью переменной SortIOsize. 
Если переменная слишком велика, наборы файлов переменных могут быть скорректированы ФОРМОМ. 
Если в файле сортировки содержится больше исправлений, чем в пакетах файлов, для вывода каждого "суперпатча" необходим второй файл сортировки. 
После обработки первого файла сортировки второй файл сортировки можно обработать точно так же, как и его предшественник. 
Этот процесс в конце концов завершится. 
Когда в файле сортировки имеется не более FilePatches патчей для пакетов файлов, результат их слияния может быть записан непосредственно в обычный вывод. 
Для полноты картины мы приводим список всех этих переменных:

FilePatches			256 	256	sub filepatches 	64 	64
	Максимальное количество исправлений, которые могут быть объединены одновременно, когда задействован файл промежуточной сортировки.
LargePatches			256 	256	sub largepatches 	64 	64
	Максимальное количество исправлений, допустимое в большом буфере. 
	Большой буфер может находиться в виртуальной памяти из-за характера применяемой к нему сортировки.
TermsInSmall			100K 	100K	sub termsinsmall 	10K 	10K
	Максимальное количество термов, допустимое в малом буфере до его сортировки. 
	Отсортированный результат либо копируется в большой буфер, либо записывается в файл промежуточной сортировки (когда LargeSize слишком мал).
SmallSize			10M 	10M	sub smallsize 		500K 	500K
	Размер малого буфера в байтах.
SmallExtension			20M 	20M	sub smallextension 	800K 	800K
	Размер малого буфера плюс его расширение.
LargeSize			50M 	50M	sub largesize 		4M 	4M
	Размер большого буфера.
SortIOsize			100K 	100K	sub sortiosize 		32K 	32K
	Размер буфера, который используется для записи в промежуточный файл сортировки и для чтения из него. 
	Следует отметить, что если этот буфер не очень велик, сортировка больших файлов может стать довольно медленной, в зависимости от операционной системы. 
	Поэтому мы рекомендуем потенциальный четвертый этап сортировки, поскольку это число слишком мало, чтобы вместить больше исправлений файлов в объединенный малый и большой буфер. 
	Установка малых и больших буферов на приличный размер может избежать всех проблем, если: 
		а) освободить больше места для кэширования, 
		б) создать меньше исправлений файлов для начала.


Существует второй набор вышеуказанных параметров настройки для видов подвыражений, как в аргументах функции или в среде term (см. 7.145). 
Поскольку такие вещи могут происходить на более чем одном уровне, любые распределения, которые необходимо выполнить 
	(во время выполнения, когда это необходимо), возможно, придется выполнять несколько раз. 
Следовательно, здесь следует быть гораздо более консервативным, чем при глобальных распределениях. 
В любом случае, такие виды редко должны включать в себя что-то очень большое. 
С аргументами функции условие состоит в том, что конечный результат будет вписываться в один терм, но в среде term такого ограничения не существует. 
Соответствующими переменными здесь являются subfilepatches, sublargepatches, sublargesize, subsmallextension, subsmallsize, subsortiosize and subtermsinsmall. 
Их значения такие же, как и для переменных без sub впереди.

Когда ФОРМА выполняется в параллельном режиме (либо TFORM , либо PARFORM), каждому работнику понадобятся свои собственные буферы. 
В PARFORM, в которой каждый процессор управляет своей собственной памятью, размер каждого из этих буферов такой же, как и для основного процесса. 
В TFORM с общей памятью вышеуказанные размеры относятся к буферам главного потока. 
Каждый из работников получает в основном буферы, размер которых в 1/N раз превышает размер буфера ведущего устройства. 
Это может стать немного больше, когда возникнут потенциальные конфликты с MaxTermSize.




=========================================================================================
bracketindexsize		bracketindexsize 	200K 	200K
CommentChar                     commentchar 		$*$ 	$*$
CompressSize                    compresssize 		90K	90K
ConstIndex                      constindex 		128 	128
ContinuationLines               continuationlines 	15 	15
Define                          
DotChar                         dotchar 		. 	.
FunctionLevels                  functionlevels 		30 	30
HideSize                        hidesize 		50M 	50M
IncDir                          incdir 			. 	.
InsideFirst                     insidefirst 		ON 	ON
JumpRatio                       
MaxNumberSize                   maxnumbersize 		200 	200
MaxTermSize                     maxtermsize 		10K 	40K
MaxWildCards                    maxwildcards 		100 	100
NoSpacesInNumbers               nospacesinnumbers 	OFF 	OFF
NumStoreCaches                  numstorecaches 		4 	4
				nwritefinalstatistics 	OFF 	OFF
NwriteStatistics                nwritestatistics 	OFF 	OFF
NwriteThreadStatistics          nwritethreadstatistics 	OFF 	OFF
OldOrder                        oldorder 		OFF 	OFF
Parentheses                     parentheses 		100 	100
Path                            path 			. 	.
ProcedureExtension              
ProcessBucketSize               processbucketsize 	1K 	1K
ResetTimeOnClear                
ScratchSize                     scratchsize 		50M 	50M
SizeStoreCache                  sizestorecache 		32K 	32K
SortType                        sorttype 		lowfirst 	lowfirst
TempDir                         tempdir 		. 	.
TempSortDir                     tempsortdir 		. 	.
ThreadBucketSize                threadbucketsize 	500 	500
ThreadLoadBalancing             threadloadbalancing 	ON 	ON
Threads                         threads 		0 	0
ThreadScratchOutSize            threadscratchoutsize 	2.5M 	2.5M
ThreadScratchSize               threadscratchsize 	100K 	100K
TotalSize                       
WorkSpace                       workspace 		10M 	40M
WTimeStats                      
                                threadsortfilesynch 	OFF 	OFF
--------------------------------------
TermsInSmall			termsinsmall 		100K 	100K	subtermsinsmall 	10K 	10K
SmallSize			smallsize 		10M 	10M	subsmallsize 		500K 	500K
SmallExtension			smallextension 		20M 	20M	subsmallextension 	800K 	800K
LargePatches			largepatches 		256 	256	sublargepatches 	64 	64
LargeSize			largesize 		50M 	50M	sublargesize 		4M 	4M
FilePatches			filepatches 		256 	256	subfilepatches 		64 	64
SortIOsize			sortiosize 		100K 	100K	subsortiosize 		32K 	32K























