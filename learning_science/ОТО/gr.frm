dim 4;
index la,mu,nu,ci,si,ro,al,be,ga,al1,...,al500;
Cfun g(sym),Ga,R,x(sym);
Nfun d;

Local F = R(mu,ro,mu,la);

#do ipr = 1,50
  id once R(mu?,ro?,si?,la?) = d(la,Ga(mu,si,ro)) + Ga(mu,la,al`ipr')*Ga(al`ipr',si,ro) - 
        d(si,Ga(mu,la,ro)) + Ga(mu,si,al`ipr')*Ga(al`ipr',la,ro);
#enddo

#do ipr = 51,100
  id once Ga(la?,mu?,nu?) = 1/2*g(la,al`ipr')*(d(nu,g(mu,al`ipr')) + d(mu,g(nu,al`ipr')) - d(al`ipr',g(mu,nu)));
#enddo
#do ipr = 101,150
  id once d(ro?,Ga(la?,mu?,nu?)) = 1/2*(
    d(ro,g(la,al`ipr'))*d(nu,g(mu,al`ipr')) + g(la,al`ipr')*d(x(ro,nu),g(mu,al`ipr')) + 
    d(ro,g(la,al`ipr'))*d(mu,g(nu,al`ipr')) + g(la,al`ipr')*d(x(ro,mu),g(nu,al`ipr')) - 
    d(ro,g(la,al`ipr'))*d(al`ipr',g(mu,nu)) - g(la,al`ipr')*d(x(ro,al`ipr'),g(mu,nu))
    );
#enddo

sum mu,al1,...,al150;

print +s;

.sort
