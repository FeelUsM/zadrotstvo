#-
nfun c,cc,aux,aux1,aux2;
nfun comm;
Cfun J(sym),h,auxC,ccc,eq(sym),d(sym);
dim 3;
index al,be,ga1,...,ga20,mu1,...,mu100,nu1,...,nu10;
set muset:mu1,...,mu100;

sym n,A,B,smth,smth1,smth2;
dim n;
index i,j,k1,...,k20;
set outindex: k1,...,k20;
Nfun antiD(sym);
Cfun mye; * опять костыли приходится клепать


#+
#define debug "1"
*=== Гамильтонианы ===
#define H "J(i,j)*d(al,be)*c(i,al)*c(j,be)/2 + h(i,al)*c(i,al)";
#define Hh "h(i,al)*c(i,al)";
#define HJ "J(i,j)*d(al,be)*c(i,al)*c(j,be)/2";

*local Ch = comm(`Hh',c(k1,ga1));
*local ChToCCh = comm(`Hh',d_(ga1,ga2)+i_*e_(ga1,ga2,nu1)*c(k1,nu1));
local CJ = comm(`HJ',c(k1,ga1));
*local CJToCCJ = comm(`HJ',d_(ga1,ga2)+i_*e_(ga1,ga2,nu1)*c(k1,nu1));
*local C  = comm(`H' ,c(k1,ga1));
*---
*local CCh = comm(`Hh',c(k1,ga1)*c(k2,ga2));
*local CCJ = comm(`HJ',c(k1,ga1)*c(k2,ga2));
*local CC  = comm(`H' ,c(k1,ga1)*c(k2,ga2));
*---
*local C2h = comm(`Hh',c(k1,nu1)*c(k2,nu1));
*local C2J = comm(`HJ',c(k1,nu1)*c(k2,nu1));
*local C2  = comm(`H' ,c(k1,nu1)*c(k2,nu1));
*---
*local C3h = comm(`Hh',c(k1,nu1)*c(k2,nu2)*c(k3,nu3)*e_(nu1,nu2,nu3));
*local C3J = comm(`HJ',c(k1,nu1)*c(k2,nu2)*c(k3,nu3)*e_(nu1,nu2,nu3));
*local C3  = comm(`H' ,c(k1,nu1)*c(k2,nu2)*c(k3,nu3)*e_(nu1,nu2,nu3));
#-
id comm(A?,B?) = A*B-B*A;

bracket eq;
print +s;
.sort :commutator expanded;

* === затравочная функция ===
id once c(?smth) = cc(?smth);

#define cyi "0"
#do cyflag=1,1
	#define cyi "{`cyi'+1}"
	#write "=== cycle #`cyi' ==="

* 	=== процесс разделения на совпадающие и различные индексы ===
	id cc(?smth1)*c(?smth2) = cc(?smth1)*cc(?smth2) + cc(?smth1)*aux(?smth2);

	if(match(cc(i?,?smth1)*aux(j?outindex,?smth2)));
		$flag = 1; * j - внешний
	else;
		$flag = 0; * j - внутренний
	endif;
	while(match(cc(i?$i,?smth1)*aux(j?$j,?smth2)));
*		* если оба индекса внешние - домножаем на маркер eq(i,j)
		if(match(cc(i?outindex,?smth1)*aux(j?outindex,?smth2)));
			id cc(i?,?smth1)*aux(j?,?smth2) = 
				cc(i,?smth1,?smth2)*auxC*eq(c(i),c(j))+
				aux(j,?smth2)*cc(i,?smth1); * - основная замена цикла
*			* i,j засовываем в c() чтобы внутри argument они не изменились
		else;
			id cc(i?,?smth1)*aux(j?,?smth2) = 
				cc(i,?smth1,?smth2)*auxC+
				aux(j,?smth2)*cc(i,?smth1); * - основная замена цикла
		endif;
		

		if(match(auxC)); * - i и j надо сделать одинаковыми
			argument;
*				* внешние индексы имеют приоритет над внутренними
*				* т.е. внутренний индекс будет заменен на внешний, а не наоборот
				if($flag);
					id $i = $j;
				else;
					id $j = $i;
				endif;	
			endargument;
			id auxC = 1;
		endif;
	endwhile;
	id aux(?smth) = 0;

*	=== упрощение индексов ===
	#call EqSimplify()

*	=== новая затравочная функция ===
	if(0==match(cc(?smth)))
		id once c(?smth) = cc(?smth);
		
* 	=== условие продолжения цикла ===
	if(match(c(?smth))) redefine cyflag "0";

	#if 0
*	* 1 - включена промежуточная сортировка
		#write "(промежуточная сортировка"
*	=== Оборачиваем в симметричную функцию === в этом месте aux - костыль
		id once cc(?smth) = aux(cc(?smth));
		repeat id aux(?smth1)*cc(?smth2) = aux(?smth1,cc(?smth2));
		id aux(?smth) = antiD(?smth);

		bracket eq;
		print +s;
		.sort :cycle-split sort;

*	=== разворачиваем симметричную функцию ===
		id antiD(cc(?smth1)) = aux(cc(?smth1));
		#define j "1"
		#do jf = 1,1
			#define j "{`j'+1}"
*			#write "=== cycle-j #`j' ==="
			id antiD(<cc(?smth1)>,...,<cc(?smth`j')>) = aux(<cc(?smth1)>,...,<cc(?smth`j')>);
			if(match(antiD(<cc(?smth1)>,...,<cc(?smth{`j'+1})>))) redefine jf "0"; * условие продолжения цикла
			.sort :kostyl;
		#enddo
		repeat id aux(cc(?smth1),?smth2) = cc(?smth1)*aux(?smth2);
		id aux = 1;
		#write "промежуточная сортировка)"
	#else
		bracket eq;
		print +s;
		.sort :cycle-split;
	#endif

#enddo
#write "=== end cycle ==="

* === заменяем на коммутирующие ===
id cc(?smth) = ccc(?smth);

* === тождество Паули
#define cyi "0"
#do cyflag=1,1
	#define cyi "{`cyi'+1}"
	id once ccc(i?,al?,be?,?smth) = d_(al,be)*ccc(i,?smth) + i_*e_(al,be,mu`cyi')*ccc(i,mu`cyi',?smth);
	id ccc(i?) = 1;
	contract;
	
* 	=== условие продолжения цикла ===
	if(match(ccc(i?,al?,be?,?smth))) redefine cyflag "0";
	
*	bracket eq;
*	print +s;
	.sort :cycle-pauli;
#enddo

bracket eq;
print +s;
.sort:before end;

#call EqSimplify()

sum nu1,...,nu10,al,be,mu1,...,mu100;
id e_(mu1?,mu2?,mu3?) = mye(mu1,mu2,mu3);
argument;
#do N = 1,100
	id N`N'_? = mu`N';
#enddo
endargument;
id mye(mu1?,mu2?,mu3?) = e_(mu1,mu2,mu3);

sum i,j;
id e_(mu1?,mu2?,mu3?) = mye(mu1,mu2,mu3);
argument;
	id N1_? = i;
	id N2_? = j;
endargument;
id mye(mu1?,mu2?,mu3?) = e_(mu1,mu2,mu3);

id J(i?,i?) = 0;

bracket eq;
print +s;
.sort:end;

Cfun c2(sym), c3(antisym), c2v;

id ccc(k1?,mu1?)*ccc(k2?, mu1?) = c2(k1,k2); * скалярное произведение
id ccc(k1?,mu1?)*ccc(k2?,mu2?)*ccc(k3?,mu3?)*e_(mu1?,mu2?,mu3?) = c3(k1,k2,k3); * смешанное произведение
id ccc(k1?,mu1?)*ccc(k2?,mu2?)*e_(mu1?,mu2?,mu3?) = c2v(k1,k2,mu3); * векторное произведение

bracket eq;
print +s;
.end:pricheson;
