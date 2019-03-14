dim 3;
sym n;
*Ntensors
Nfunction c,cp,t,d;
Index i1,...,i100,j1,...,j200,k1,...,k100,l1,...,l100;
Cfunctions C;
sym a,a1,...,a23,b1,...,b20,e,p;

Local cse3 = 
(1+a12*(d(1,2)+d(2,3))+a13*d(1,3))*
((d(1,2)+d(2,3))*t(1,2,3)-t(1,2,3)*(d(1,2)+d(2,3)));

* === расписываем наши функции в сигма-матрицы ===
#do i = 1,50
  id once d(i1?,i2?) = c(i1,j`i')*c(i2,j`i');
#enddo
#do i = 50,199,3
  id once t(i1?,i2?,i3?) = c(i1,j`i')*c(i2,j{`i'+1})*c(i3,j{`i'+2})*e_(j`i',j{`i'+1},j{`i'+2});
#enddo

print +s;
.sort:expand;

* === сортировка ===
repeat;
  id 	c(i1?!{,j1},k1?)*
	c(j1?!{i1,i2},k3?)*
	c(i1?!{,j1},k2?)
	= c(i1,k1)*c(i1,k2)*c(j1,k3);
#do N=2,3
  id 	c(i1?!{j1,...,j`N'},k1?)*
	<c(j1?!{i1,i2},l1?)>*...*<c(j`N'?!{i1,i2},l`N'?)>*
	c(i1?!{j1,...,j`N'},k2?)
	= c(i1,k1)*c(i1,k2)*<c(j1,l1)>*...*<c(j`N',l`N')>;
#enddo
endrepeat;

print +s;
.sort:sort;

* === раскрытие ===
#do i = 1,100
	id once c(i1?,j1?)*c(i1?,j2?) = d_(j1,j2)+i_*c(i1,k`i')*e_(k`i',j1,j2);
#enddo

* === и свертка ===
contract;
contract;

print +s;
.sort:pauli;

* === заменяем на коммутирующие ===
id c(?name) = C(?name);

* === возвращаем к красивому виду ===
id C(i1?,j1?)*C(i2?,j1?) = d(i1,i2);
id C(i1?,j1?)*C(i2?,j2?)*C(i3?,j3?)*e_(j1?,j2?,j3?) = t(i1,i2,i3);

bracket t,d;
print;

.end:end;
