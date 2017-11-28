cd '50';
ls = transpose(dir('*.stg'));
cd ..
for file = ls
    t = strsplit(file.name,'.');
    s=['C:\Users\admin\Downloads\_Thesis\Matlab\txt\' t{1,1}];
    Readd('C:\Users\admin\Downloads\_Thesis\Matlab\50\',file.name,20,s);
end