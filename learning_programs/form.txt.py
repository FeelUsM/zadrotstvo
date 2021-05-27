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
	fill
	cleartable
	
	fillexpression
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

	term
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
	sort
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
  	Print [<options>] "<format string>" [<objects>];
		+s каждый терм на новой строке
	print[]
	nprint

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
