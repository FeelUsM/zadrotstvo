{=== ядро, интерфейс ===
блокнот
	запуск: mathematica или ярлыком
	Wolfram CDF Player
командная строка
	запуск: math или пуск-> mathematica kernel
	незаконченное выражение можно продолжить на следующей строке
	C-C, C-G, Esc - отмена или отказ ввода
	C-D, C-Z - прекращение работы ядра
	Quit[]
MathLink
}
{=== блокнот ===
S-Enter или num-Enter- ввод-вычисление
M-, - прекратить вычисление(?)
C-L - вставить последнее выражение
S-C-L - вставить результат последнего выражения

C-spc - выход из ...
С-^ или C-6 - степень
C-_ - индекс
C-/ - дробь
C-2 - корень
C-, - добавить столбец
C-enter - добавить строку

группы можно скрывать

Edit->Preferences->Appearence->Syntax Coloring
Input: известные имена - черный
Input: новые имена - синий

можно выделить вначале ячейку
M-1	Format -> Style -> Title
M-2	Format -> Style -> Chapter
M-3	Format -> Style -> Subchapter
M-4	Format -> Style -> Section
M-5	Format -> Style -> Subsection
M-6	Format -> Style -> Subsubsection
M-7	Format -> Style -> Text
M-8	Format -> Style -> Code
M-9	Format -> Style -> Input

M-9	Format -> Style -> Input
M-7	Format -> Style -> Text
		Window -> Show Toolbar
		Window -> Show Ruler
		C-9 - начать ввод формулы
		C-0 - закончить ввод формулы
	Format -> Stylesheet - внешний вид стиля
	Format -> Edit Stylesheet

In[n]:=
Out[n]=
}
{=== символы ===
http://reference.wolfram.com/language/tutorial/Operators.html
Palletes -> Special Characters

esc..esc\[..]
a		Alpha
b		Beta
...
A		CapitalAlpha
B		CapitalBeta
...
int		Integral
dd		DifferencialD
\TeX
\infty
->		Rule
not		Not
elem	Element
!elem	NotElement
fa		ForAll
ex		Exists
		Ellipsis	...


}
{=== документация, помощь ===
Help -> Documentation Center
?имя_или_оператор
??имя_или_оператор - с дополнительной информацией
?aaa* - список объектов, начинающихся с aaa
?aaa`* - список объектов, содержащихся в пакете aaa
}
{=== операторы ===
http://reference.wolfram.com/language/tutorial/OperatorInputForms.html
(**) - комментарий
() - группировка
F[x,y] - функция
f@g === g//f === f[g]
x~f~y === f[x,y]

70	x//f === Postfix[f[x]]
Postfix[]
Precedence[] - старшинство (для операторов?)
}
{=== Встроенные функции - с большй буквы ===
	{ввод-вывод
		In[]
			% === Out[] - последний результат
		Out[]
		
		Quiet[выражение]	вычисляет выражение без вывода каких-либо сообщений
		Off[Функция::тег]	выключение (подавление) сообщения
		On[Функция::тег]	включение сообщения
		750	f::tag === MessageName[f,"tag"]
		MessageName[f,"tag"] - имя(тег), которому можно присвоить сообщение, которое может использовать аргументы, типа `1` `2` ... 
			f::usage - справка функции
		Message[f::tag,args] - вывод соответствующего сообщения
		General - символ, к которому присоединяются основные системные сообщения
			General::newsym - печатает сообение, когда создается новый символ
		SyntaxInformation[f] - подсказка для подсветки синтаксиса
			SyntaxInformation[f] = {"ArgumentsPattern" -> {_, _}}
			SyntaxInformation[f] = {"ArgumentsPattern" -> {_, _, OptionsPattern[]}}

		MatrixForm[] - список в матрицу
		TableForm[]
		StandardForm[] - человеческая форма
		FullForm[] - машинная форма
		InputForm[] - форма, которую снова можно скормить математике
		
		Print[smth] - печатает сообщение во все потоки, содержащиеся в $Output
		$Output - список потоков, куда поступает вывод от Print[]
		Write[stream,expr] - печатает в сообщение в заданный поток
		OpenWite[filename] - открывает файл и создает поток
		Close[stream] - закрывает поток

		Directory[] - выдает текущую директорию
		NotebookDirectory[] - выдает директорию текущего блокнота
		SetDirectory[dir] - устанавливает текущую директорию
		30	val>>file === Put[val,file]
		Put[val,file] - записывает значение в файл (при помощи FullForm (?))
		720	<<file === Get[file]
		Get[file] - возвращает значение, прочитанное из файла
			Get[PackageName`] - загрузить пакет
		Needs[PackageName`] - читает пакет, только если он отсутствует в $Packages
		Import[file,format]
		Export[file,expr,format]
		$ImportFormats - список доступных форматов
		
		Monitor[выполняющийся код, (выр-е от переменных, меняющихся в процессе кода, которое выводится и заменяется ниже)]
		ProgressIndicator[0<val<1] - возвращает и выводит прогресс бар
		
		RawBox[]
		MakeBoxes[]
	}
	{производительность и дебаг
		http://reference.wolfram.com/language/guide/EvaluationControl.html
		
		Pause[s]
		
		MemoryConstrained[expr,bytes]
		Timing[expr]
		
		ParallelSubmit[]
		WaitAll[]
		WaitNext[]
	}
	{переменные, функции, опции, атрибуты, контексты
		{переменные
			Hold[] - квотирование
			40	x=y === Set[x,y]
			Inactivate[expr[,fun]]
			Activate[expr[,fun]]
			
			Set[x,y] - вычислить y и в последсвии заменять x на этот вычисленный сейчас y
			40	x:=y === SetDelayed[x,y]
			SetDelayed[x,y] - не вычислять сейчас y и в последсвии заменять x на этот y, такой, какой он есть, а потом вычислять
			670	x=. === Unset[x] (?)
			Unset[]
			Clear[] - сбрасывает определение, "Global`*" - все текущие переменные
			ClearAll[] - сбрасывает значения и атрибуты и ...
			Remove[x] - удаляет x (и он становится сининьким)
				With[{var=...},(Remove[var];#)&[code]]
		}
		{атрибуты
			SetAttributes[f,attr] - устанавливает атрибут
			Attributes[f] - возвращает список атрибутов
			ClearAttributes[f] - удаляет аттрибуты
			HoldAll - не вычислять аргументы
			Listable - атрибут, т.ч. f[{a,b,c}] -> {f[a],f[b],f[c]}
				Thread[f[{a,b,c}]] -> {f[a],f[b],f[c]}
			Orderless - атрибут, т.ч. f[a,b] == f[b,a]
			Flat - атрибут т.ч. f[a,f[b]] == f[a,b]
			OneIdentity - атрибут т.ч. f[x] == x
			Protected - атрибут, запрещает менять определение функции
				Protect[fun] - устанавливает атрибут Protected
				Unprotect[fun] - снимает атрибут Protected
		}
		{опции - могут передаваться в конце аргументов например в Plot[]
			Options[f] - список опций_по_умолчанию функции f
			SetOptions[s,name->val,...]
		}			
		{контексты
				contextName`f - доступ к функции внутри контекста
			Context[shortname] - контекст переменной
			Context[] - текущий контекст
			Contexts[] - список всех возможных контекстов
			$Context - текущий контекст
			$ContextPath - context search path
				context`name or c_1`c_2 ... `name	    a symbol in an explicitly specified context
				`name                                   a symbol in the current context
				`context`name or `c_1 `c_2 ... `name    a symbol in a specific context relative to the current context
				name                                    a symbol in the current context, or found on the context search path
			Begin["contextName`"] - устанавливает текущий контекст
				Begin["c`"]; Print[Context[x]]; End[] - здесь Begin[] не сработает, т.к. это выр-е сначала прочитается (всё), а потом будет выполняться
			End[] - возвращает текущий контекст и восстанавливает старый
			BeginPackage["contextName`",{need1,need2,...}] - делает активными пакетами только contextName` и System`
				а также вызывает Needs[] для каждого need1, need2 ...
			EndPackage[] - восстанавливает $Context и $ContextPath, и добавляет текущий контекст в $ContextPath
		}
	}
	{структура выражений
		Symbol["name"] - ссылается на символ с определенным именем
		Unique["name"] - создает уникальный символ с именем, начинающимся с name 
			Unique[ConstantArray["x", 10]] -> x1,x2,x3,...,x10
		SymboName[s] - возвращает имя символа
		Names["pattern"] - возвращает список имен символов, подходящих под паттерн
		
		Head[x] - возвращает голову объекта (обычно имя функции или Symbol, Integer, ...)
		Level[obj,level] - все объекты на соответствующем уровне: n - 1..n, {n} - only n, {n,m} - n..m, -1 - листья, 0 - все выражение
		Scan[f,expr] - применит f ко всем элементам списка expr
	}
	{строки
			"abc" === String["abc"] - строка ???
		String[]
		ToString[x]
		600	s1<>s2<>s3 === StringJoin[s1,s2,s3]
		StringJoin[s1,s2,...]
		
		RegularExpression["str"]
		StringMatchQ[str,regex]
	}
	{логика
		290 a===b  === SameQ[a,b]
		290 a=!=b  === UnsameQ[a,b]
		290	a==b   === Equal[a,b]
		290	a==b   === Unequal[a,b]
		290	a<b    === Less[a,b]
		290	a<=b   === LessEqual[a,b]
		290	a>b    === Grater[a,b]
		290	a>=b   === GraterEqual[a,b]
		
		230	!x     === Not[x]
		215	a||b   === Or[a,b]
		215	a&&b   === And[a,b]
		TrueQ[arg] === If[arg===True,True,False]
	}
	{блоки, циклы и ветвления
		10	expr1;expr2;expr3 === CompoundExpression[expr1,expr2,expr3]
		CompoundExpression[a,b,c] === a;b;c
		                        m = i^2
		Block[listVars,body]    Block[{i = a}, i + m] --> a+a^2 // dynamic scoping
		Module[listVars,body]   Module[{i = a}, i + m] --> a+i^2// lexical scoping
		With[listVars,body]
		
		If[cond,then,else]
		Which[cond,then, cond,then, ...]
		Switch[expr, patt1,then, patt2,then, ...]
		While[cond,body]
		For[start,cond,inr,body]
		Do[...?]
		
		Label[name]
		Goto[name]
		Break[]
		Continue[]
		Return[expr]
		Catch[expr] - возвращает значение выражения или кинутое исключение
		Throw[val]
		
		Reap[body] - возвращает список из двух элементов: 1й - результат body и 2й - {{все, что вернул каждый вызов Sow[] внутри body}}
		Sow[expr]
	}
	{списки
	https://mathematica.stackexchange.com/questions/3069/elegant-operations-on-matrix-rows-and-columns
		{генерация
			670	{a,b,c} === List[a,b,c] - список
			List[a,b,c] -> {a,b,c}
			Range[n] -> {1,...,n}
			Table[f[xxx],{xxx,xl,xh}] -> {f[xl], f[xl+1], ... , f[xh]}
			Array[f,n] -> {f[1],...,f[n]}
			ConstantArray[c,n] -> {c,c,c,c,c,c,...,c} n times
			Tuples[list1,list2,...] - генерирует все списки где на 1м месте элемент из 1го списка, на 2м - из 2го ....
			Permutations[list] - генерирует список перестановок
			Signature[]
			Order[a,b] -> -1,0,+1
			OrderedQ[f[a,b,c]] - Упорядочены ли аргументы
		}
		{индексация
			670	x[[n,m,...]] === Part[x,n,m,...] - n-й элемент списка
			Part[l,n,m,...]
			в качесте индекса можно использовать число или отрицательное число(индекс с конца) или список или
			All - выбрать все элементы, или
			305	a;;b;;c === Span[a,b,c] - диапозон ((a или b) и c можно опускать)
			Span[left,right,step]
			
			Position[list,pattern,levelspec] - возвращает список путей, элементов, удовлетворяющих паттерну (головы тоже просматривает)
			
			Length[list]
			First[list]
			Last[list]
		}
		{добавление/удаление
			Prepend[]
			Append[list,el] - не меняет список
			Drop[list,n] - вернуть кроме первых n элементов
			AppendTo[list,el] - меняет список
			Insert[]
			Delete[list,i]
		}
		{как множества
			http://reference.wolfram.com/language/guide/OperationsOnSets.html
			Union
			Intersection
			Complement
			MemberQ
		}
		{преобразования списков
			Partition[l,n] - разбивает список l на список подсписков длиной n
			Split[] - повторяющиеся элементы объединяет
			Flatten[] - убирает внутренние скобки
			FlattenAt[list,pos] - убирает внутренние скобки (вклеивает) на позиции pos
			Riffle[] - расставить между элементами другой элемент

			Sort[v] или ассоциацию
			SortBy[v,f]
			Union[v] - Sort и удалить повторы
			Reverse[]
			RotateLeft[]
			RotateRight[]
			PadLeft[]
			PadRight[]
			Join[]
			Select[список,предикат] - оставляет только элементы, удовлетворяющие предикату
			Pick[list,selector,pattern] - оставляет только элементы list, для которых элементы selector удовлетворяют pattern-у
		}
	}
	{map, hash
			<|a->1,b->2|> === Association[{a->1,b->2}]
		Association[rules] (:> позволяет сохранять код и вызывать его)
		Normal[] - Association -> List[rules]
			ass[key] -> val // lvalue
			ass[[Key[smth]]]
			ass[["string"]]
		Key[]
			
		Select[ассоц,предикат]
		Position[assoc,n] -> Key[...] на nой позиции
		Append[assoc,rule]
		Keys[assoc] -> {keys}
	}
	{функ.прог., Map-Reduce
		90	body& === Function[body]
		Function[body] - лямбда-функция
			#n === Slot[n]
		Slot[n] - n-й аргумент лямбда-функции
		
		620	f@@g[] === Apply[f,g[]]
			f@@@g[] === Apply[f,g[],{1}] --- на первом уровне
		Apply[f,g[x,...,z]] -> f[x,...,z]
			Apply[f,1] -> 1 (а не в f[1])
		Nest[f,x,3] -> f[f[f[x]]]
		NestList[]
		
		620	f/@list === Map[f,list]
		Map[f,{a,...,c}] -> {f[a],...,f[c]} или со значениями ассоциации
		Scan[f,expr,lavelspec] - применяет f к каждому элементу
		MapThread[f,{l1,l2,...}] -> {f[l1[[1]],l2[[1]],...],...}
		MapThread[f,{l1,l2,...},levelspec]
		
		Total[list] - сумма (и с ассоц.)
		Accumulate[{a,b,c}] -> {a,a+b,a+b+c} 
	}
	{шаблоны и замены
		<Blank> - шаблонный объект, который может соответствовать любому выражению в языке Wolfram. Выражение <Blank>[] может компактно обозначаться символом подчеркивания _. 
		Более специальный паттерн <Blank>[h] (компактно обозначаемый _h) соответствует любому выражению с головой h. 
		<Blank> - очень мощьная и полезная конструкция для программирования, основанного на паттернах, а также является основанием, на которм строится шаблонная функциональность. 
		Наиболее общая функция, работающая с <Blank> и соответствующими паттернами как с аргументами - это <SetDelayed>. 
		Другими такими функциями являются <MatchQ>, <Cases>, <DeleteCases>, <Count>, и <RuleDelayed>.
		
		Последовательность одного или более бланков представляеетя шаблонным объектом <BlankSequence> (двойное подчеркивание: __). 
		Последовательность нуля или более бланков представляется с использованием шаблонного объекта <BlankNullSequence> (тройное подчеркивание: ___). 
		Вообще, паттерны, использующие много конструкций <Blank>, работают быстрее по сравнению с теми, которые используют <BlankSequence> и <BlankNullSequence>, так как в двух последних случаях необходимо протестировать гораздо больше возможностей для возможного совпадения.
		
		<Blank> может использоваться вместе с <Optional> для задания шаблонного объекта для выражения, которое, если пропущено, будет заменяться значением по умолчанию. 
		Шаблонный объект <Alternatives> позволяет задавать несколько возможных паттернов, включая <Blank>. 
		<Blank> может быть скомбинирован с <PatternTest> (записанный коротко как p?test). 
		Например код <<Cases[Range[100], _?(IntegerQ[Sqrt[#]] &)]>> (который использует лямбда-функцию со спецификацией <Slot>) выделяет и возвращает список всех чисел-квадратов, которые меньше или равны 100.


		730	_ === Blank[] - любое выражение
		730	_h === Blank[h] - любое выражение с головой h (например _Integer)
			__ === BlankSequence[]
			___ === BlankNullSequence[]
		Blank[] - любое выражение
		BlankSequence[]
		BlankNullSequence[]
		
		150	x_ === Pattern[x,Balnk[]]
		150	a:b === Pattern[a,b]
		Pattern[a,b] - a должно соответствовать b
		Except[b] - не должно соответствовать b
		140	a:b:c === Optional[Pattern[a, b], c]
			y_: с === Optional[Pattern[y, Blank[]], с]
			y_. === Optional[Pattern[y, Blank[]]]
		Optional[a,b] - если паттерн a пропущен, то он примет занчение b
		Default[f,i] - lvalue для значения по умолчанию iго аргумента функции f, если он задан как y_.
		
		680	pattern?test === PatternTest[pattern,test]
		PatternTest[pattern,test] - pattern распарсится удачно, только если после того как оно распарсилось будет верно еще и условие
		(условие - предикат, который применяется к распарсенному паттерну)
		130	pattern/;cond === Condition[pattern,cond]
		Condition[pattern,cond] - pattern распарсится удачно, только если после того как оно распарсилось будет верно еще и условие
		(в условии можно использовать элементы паттерна, условие не является лямбда-функцией)
		https://mathematica.stackexchange.com/questions/1835/using-a-patterntest-versus-a-condition-for-pattern-matching
		160 a|b|c === Alternatives[a,b,c]
		Alternatives[] - должен распарсится лбой из паттернов
	
	
		120	x->y === Rule[x,y]
		Rule[]
		120	x:>y === RuleDelayed[x,y]
		RuleDelayed[] - правая часть квотирована (Hold)
		
		
		MatchQ[expr,pattern] - проверяет, соответствует ли все выражение шаблону
		Replace[expr,pattern] - заменяет всё выражение по шаблону
		
		FirstPosition[expr,pattern] - возвращает путь к первому найденному подвыражению в виде списка позиций (или Missing["NotFound"])
		Position[expr,pattern] - возвращает список путей в виде спиков позиций (головы тоже просматривает)
		ReplacePart[expr,path->expr2] - в выражении заменяет элемент, находящийся по заданному адресу, выражением2
		
		MemberQ[{exprs},pattern] - проверяет, есть ли в списке элементы, соответствующие шаблону
		FreeQ[{exprs},pattern] = !MemberQ[expr,pattern]
		Cases[{exprs},pattern] - возвращает список подвыражений, соответствующих или замененных по шаблону
		FirstCase[{exprs},pattern] - возвращает первое подвыражение, соответствующее или замененное по шаблону (или Missing["NotFound"])
		Count[{exprs},pattern] - подсчитывает, сколько раз в выражении встречается подвыражение, соответствующее шаблону
		
		110	expr/.rules === ReplaceAll[expr,rules]
		ReplaceAll[expr,rules] - в выражении заменяет все подвыражения по шаблону
		110	expr//.rules === ReplaceRepeated[expr,rules]
		ReplaceRepeated[expr,rules] - применяет ReplaceAll пока в нем что-то заменяется
	}
	{кванторы, домены, Assumptions
		240 \[Exists]_a b === Exists[a,b]
		Exists[x,expr]
		240 \[ForAll]_a b === ForAll[a,b]
		ForAll[x,expr]
		FullSimplify[smth] - вычисляет true или false для кванторов
		Resolve[expr] - удаляет кванторы
		
	?	Домены:, Booleans, Primes, Integers, Rationals, Algebrics, Reals, Complexes
		250 a\[Element]b === Element[a,b]
		Element[a,домен, регион] - a может быть символом, списком сиволов или паттерном
		250 a\[NotElement]b === NotElement[a,b]
		NotElement[a,домен, регион]
		
		$Assumptions - глобальные предположения
		Assuming[assume, expr] - локльные предположения, котрые применяются только в 
			Refine, Simplify, FullSimplify, FunctionExpand, Integrate...
		Refine[] - уточняет выражение в соответствии с предположениями
		Simplify[]
		FullSimplify[]
		FunctionExpand[]
	}
	{арифметика
		310	a+b+c === Plus[a,b,c]
			a-b === a+(-b)
			-b === b*(-1)
		Plus[...]
			a/b === a*b^-1
		400	a*b*c === Times[a,b,c] ; пробел===*
		Times[...]
		590	a^b === Power[a,b]
			a.^b === a*10^b
		
		Power[a,b]
		Sqrt[a]
		Exp[a]
		Log[]
		Sin[x]
		Cos[]
		Tan[]
		ArcSin[]
		ArcCos[]
		ArcTan[]
		Re[]
		Im[]

		N[x] - перевести в число с плавающей точкой или посчитать численно
		Abs[]
		Round[]
		Floor[]
		Mod[a,b] - остаток
		Quotient[a,b] - целочисленное деление
		
		RandomReal[]
		RndomInteger[]
		Max[a,b,c...]
		Min[a,b,c...]
		
		610	x! === Factorial[x]
		Factorial[x]
			x!! === Factorial2[x]
		Factorial2[x]

		Pi
		E
		Degree - Pi/180
		I
		Infinity
	}
	{теория чисел
		FactorInteger[x] - разложить x на простые множители
		PrimeQ[x] - простое ли число
		Prime[n] - n-е простое число
	}
	{многочлены
		Variables[poly] - возвращает список переменных многочлена
		Coefficient[expr,form] - возвращает коэффициент при form
		Numerator[expr] - приводит к общему знаменателю и возвращает числитель
		
		Factor[expr] - разложить многочлен на множители
		Expand[expr] - раскрыть скобки только для Plus и Times
		Distribute[expr] - раскрыть скобки
		Collect[expr,pattern,[action]] - вынести паттерн за скобки и выполнить action с каждым множителем pattern-а
			Reap[Collect[expr,pattern,Sow];][[2]]
	}
	{алгебраические ур-я
		Solve[lhs==rhs,{x...}] - решить алгебраическое ур-е (или систему) отн x
		SolveAlways[lhs==rhs,{x...}] - подразумевая x-ы произвольными решить алгебраическое ур-е (или систему) отн. всех остальных переменных.
			params/.Solve[equations,params]
		Reduce[]
		NSolve[lhs==rhs,x] - численно решить алгебраическое ур-е
		FindRoot[lhs==rhs,{x,x0}] - численно найти корень алгебраического ур-я около x0
		
		PolynomialQutientRemainder[moly1(x),poly2(x),x] - {q(x),r(x)}
	}
	{Лин-Ал
		490	x.y.z === Dot[x,y,z]
		Dot[] - умножение матриц
		Inner[] - обобщение умножения матриц (параметризуемое сложением и умножением как функциями)
		Outer[] - тензорное умножение, параметризуемое умножением
		TensorProduct[...] = Outer[Times,...]
		KroneckerProduct[] - тензорное умножение, но матрицу в матрицу, вектор в вектор, ...

		Det[m]
		Tr[m]

		Inverse[m]
		RowReduce[m] - верхнетреугольная, преобразованиями строк

		PositiveDefiniteMatrixQ[m]
		PositiveSemidefiniteMatrixQ[m]

		Eigenvalues[] - СЗ
		EigenSystem[]
		
		MatrixExp[]
		
		CoefficientArrays[expr,vars, "Symmetric"->True] - Полином/квадратичный функционал -> Массив/матрицу
	}
	{матан
		Limit[f,x->x0] - найти предел
		D[expr[x],x] - продифференцировать по x
		Integrate[expr[x],x] - проинтегрировать по x
		NIntegrate[expr[x],x] - численно проинтегрировать по x
		Series[f,{x,x0,order}] - разложить в степенной ряд в точке x0 
		Minimize[f,x] - минимизация
		NMinimize[f,x] - численная минимизация
		FindMinimum[f,{x,x0}] - численный минимум около x0
		Sum[f,{i,imin,imax}] - просуммировать или посчитать ряд
		NSum[f,{i,imin,imax}] - просуммировать или численно посчитать ряд
		Mean[] - среднее арифметическое
	}
	{дифуры
		NDSolve[]
		DSolve[]
	}
	{графика и интерфейс
		Grid[]

		Plot[expr[x],{x,minx,maxx}]
		ParametricPlot[{fx[t],fy[t]},{t,mint,maxt}]
		Plot3D[expr[x,y],{x,minx,maxx},{y,miny,maxy}]
		ListLinePlot[] - график по точкам
		
		ArrayPlot[]
		MatrixPlot[]

		Manipulate[] - выводит динамическое содержимое (?)
		Import[]
		Export[]

		Button[название,MessageDialog[строка]] - ...
		MessageDialog[строка] - ...
	}
}


http://kobriniq.ru/mathematica
https://habrahabr.ru/company/wolfram/blog/257733/
Основной язык
	краткий курс
		+работа с переменными и функциями
		+работа со списками
		работа с правилами
		применение синтаксиса mathemetica
	основные принципы построения вычислений
	списки
	работа со списками
	выражения
	шаблоны
	правила преобразования и определения
	функции и программы
	функциональные операции
	модульность и использование имен элементов
	текстовые фрагменты и исмволы
	вычисление выражений
	форматы данных WilgramAlpha
	приложения: структура языка
математика и алгоритмы
визуализация и графика
работа с данными
динамическая интерактивностть
блокноты и документы
система и развертывание




http://reference.wolfram.com/language/tutorial/LinearAlgebraMatrixComputations.html
http://reference.wolfram.com/language/guide/EvaluationControl.html
http://reference.wolfram.com/language/guide/GroupTheory.html
http://reference.wolfram.com/language/guide/NamedGroups.html
http://reference.wolfram.com/language/ref/GroupElements.html
http://reference.wolfram.com/language/guide/Permutations.html

https://reference.wolfram.com/language/ref/OptionsPattern.html	необязательные аргументы функций