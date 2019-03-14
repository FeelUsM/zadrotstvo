Cfun c(sym),A(sym),B(sym);
sym i,j,k,l;

Local t = 
-c(i,j)*c(j-1,k)
-c(i,j)*c(j+1,k)
+c(i,k)*c(k-1,j)
+c(i,k)*c(k+1,j)
-c(j,k)*c(k-1,i)
-c(j,k)*c(k+1,i)
+c(j,i)*c(i-1,k)
+c(j,i)*c(i+1,k)
-c(k,i)*c(i-1,j)
-c(k,i)*c(i+1,j)
+c(k,j)*c(j-1,i)
+c(k,j)*c(j+1,i);


id c(i?,j?)*c(k?,l?) = (4*A(i,j)*A(k,l)-A(i,k)*A(j,l)-A(i,l)*A(j,k))/30;

id A(i,j)*A(j-1,k) = 1/3*B(i,k)*B(j-1,j);
id A(i,j)*A(j+1,k) = 1/3*B(i,k)*B(j+1,j);
id A(k,j)*A(j-1,i) = 1/3*B(i,k)*B(j-1,j);
id A(k,j)*A(j+1,i) = 1/3*B(i,k)*B(j+1,j);

id A(j,k)*A(k-1,i) = 1/3*B(i,j)*B(k-1,k);
id A(j,k)*A(k+1,i) = 1/3*B(i,j)*B(k-1,k);
id A(i,k)*A(k-1,j) = 1/3*B(i,j)*B(k-1,k);
id A(i,k)*A(k+1,j) = 1/3*B(i,j)*B(k-1,k);

id A(k,i)*A(i-1,j) = 1/3*B(k,j)*B(i-1,i);
id A(k,i)*A(i+1,j) = 1/3*B(k,j)*B(i+1,i);
id A(j,i)*A(i-1,k) = 1/3*B(k,j)*B(i-1,i);
id A(j,i)*A(i+1,k) = 1/3*B(k,j)*B(i+1,i);

print +s;
.end;

