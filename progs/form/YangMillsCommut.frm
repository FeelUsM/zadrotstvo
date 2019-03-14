sym g,x,y,z,smth,smth1,smth2;
nfun d,dd,S,SC,T,c,comm,A,D;
nfun psi,sym1(sym),sym2(sym),sym3(sym);
nfun X,Y,Z,aux;
cfun Avec,alp;
index mu,nu,i,j,k,l,m,n;

local res2 = i_/g*comm(D(mu),D(nu));
local res1 = i_/g*comm(D(mu),D(nu));

id comm(x?,y?) = x*y-y*x;
id D(mu?) = dd(mu)-i_*g*A(mu);

.sort
skip res1;
id A(mu?) = S*A(mu)*SC-i_/g*S(d(mu))*SC;
.sort
nskip res1;

id dd(mu?)*dd(nu?) = sym1(mu,nu); * искусственнно
repeat id dd(mu?)*X?(?smth) = X(?smth,d(mu))+X(?smth)*dd(mu);
id SC*S(d(mu?)) = - SC(d(mu))*S;
id S(d(mu?),d(nu?)) = sym2(mu,nu); * искусственно
id once A(mu?) = Avec(l,mu)*T(l);
id once A(mu?) = Avec(m,mu)*T(m);
id SC*S = 1;
id S*SC = 1;
id T(i?) = c(i)/2;
id once c(i?)*c(j?) = d_(i,j) + i_*e_(i,j,n)*c(n);
id c(i?) = T(i)*2;
id SC*S = 1;
id S*SC = 1;
id Avec(i?,mu?)*T(i?) = A(mu);

print +s;

.end