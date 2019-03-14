g1=[0 1 0; 1 0 0; 0 0 0]
g2=[0 -1i 0; 1i 0 0; 0 0 0]
g3=[1 0 0; 0 -1 0; 0 0 0]
g4=[0 0 1; 0 0 0; 1 0 0]
g5=[0 0 -1i; 0 0 0; 1i 0 0]
g6=[0 0 0; 0 0 1; 0 1 0]
g7=[0 0 0; 0 0 -1i; 0 1i 0]
g8=[1 0 0; 0 1 0; 0 0 -2]/sqrt(3)
g(1,:,:)=g1;
g(2,:,:)=g2;
g(3,:,:)=g3;
g(4,:,:)=g4;
g(5,:,:)=g5;
g(6,:,:)=g6;
g(7,:,:)=g7;
g(8,:,:)=g8;
%t;
tt=[];
ti=[];

im=1i;
for i=1:8
    for j=1:8
        gg=g(i,:,:)*g(j,:,:);
        if i==j 
            if trace(gg)~=2
                fprintf('trace g(%d)*g(%d)=\n',i,j);
                trace(gg)
            end;
            gg(1,1)=0;
            gg(2,2)=0;
            gg(3,3)=0;
            gg(4,4)=0;
            if gg~=zeros(4,4)
                fprintf('g(%d)*g(%d)=\n',i,j);
                g(i,:,:)*g(j,:,:)
            end
        else
            if trace(gg)~=0
                fprintf('trace g(%d)*g(%d)=\n',i,j);
                trace(gg)
            end;
        end
    end
end
disp 'checks finished'
for i=1:8
    for j=1:8
        for k=1:8
            gi=g(i,:,:);
            gj=g(j,:,:);
            gk=g(k,:,:);
            t_=trace(gi*gj*gk-gj*gi*gk)/2/im;
            t(i,j,k)=t_;
            found=0;
            for l=1:length(tt)
                if t_==tt(l)
                    ti=[ti [i;j;k]];
                    found=1;
                    break;
                end
            end
            if ~found
                tt=[tt t_];
                ti=[ti [i;j;k]];
                fprintf('for t=%d , ijk=%d%d%d\n',t_,i,j,k)
            end
        end
    end
end
