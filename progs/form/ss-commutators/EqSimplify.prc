#procedure EqSimplify()

* === внешние индексы ===
id eq(c(k1?),c(k2?))       *eq(c(k2?),c(k3?)) = eq(c(k1),c(k2),c(k3));
id eq(c(k1?),c(k2?),c(k3?))*eq(c(k3?),c(k4?)) = eq(c(k1),c(k2),c(k3),c(k4));
*...
id eq(c(k1?),c(k1?),c(k2?),c(k3?)) = eq(c(k1),c(k2),c(k3));
id eq(c(k1?),c(k1?),c(k2?))        = eq(c(k1),c(k2));
id eq(c(k1?),c(k1?))               = 1;
*...
id e_(mu1?,mu2?,mu3?) = mye(mu1,mu2,mu3);
if(match(eq(c(k1),c(k2))));
	argument;
		id k2 = k1;
	endargument;
endif;
if(match(eq(c(k1),c(k3))));
	argument;
		id k3 = k1;
	endargument;
endif;
if(match(eq(c(k2),c(k3))));
	argument;
		id k3 = k2;
	endargument;
endif;
if(match(eq(c(k1),c(k2),c(k3))));
	argument;
		id k2 = k1;
		id k3 = k1;
	endargument;
endif;
*...
id mye(mu1?,mu2?,mu3?) = e_(mu1,mu2,mu3);

#endprocedure
