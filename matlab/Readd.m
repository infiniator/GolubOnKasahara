function Readd(adrinp,fname,np,adrout)
s=[adrinp fname];
p=np;
fid=fopen(s,'r');
disp(s);
nj=fscanf(fid,'%d',[1 1]);
s1=[adrout '.txt'];
fid1=fopen(s1,'wt');
fprintf(fid1,'%d %d\n',[nj p]);
fscanf(fid,'%d',[1 3]);
He=zeros(1,nj);
for i=1:nj
    jn=fscanf(fid,'%d',[1 1]);
    fprintf(fid1,'%d ',jn);
    pt=fscanf(fid,'%d',[1 1]);

    np=fscanf(fid,'%d',[1 1]);
    pa=[];
    for j=1:np
        pa=[pa fscanf(fid,'%d',[1 1])];
    end;
    if(pa(1)~=0)
        He(i)=max(He(pa))+1;
        fprintf(fid1,'%d ',He(i));
        fprintf(fid1,'%d ',pt);
        fprintf(fid1,'%d ',[np pa]);
    else
        fprintf(fid1,'%d ',0);
        fprintf(fid1,'%d ',pt);
        fprintf(fid1,'%d ',0);
    end;
    fprintf(fid1,'\n',0);
end;
fclose(fid);
fclose(fid1);
end