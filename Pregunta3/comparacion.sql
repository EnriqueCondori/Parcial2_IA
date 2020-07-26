declare @nomb varchar(20),@cadena1 varchar(20),@prob float,
@cont integer,@v varchar(2)
declare listarest Cursor  for select nombre from alumno
open  listarest
fetch listarest into @nomb
set @cadena1=@nomb;

while @@fetch_status=0
begin
set @cont=1;
set @prob=0;

	while @cont<=LEN(@cadena1)
	begin
	Set @v=SUBSTRING(@cadena1,@cont,1)
		if @v=SUBSTRING(@nomb,@cont,1)
			begin
				 set @prob=@prob+1;
			end
		set @cont=@cont+1;
	end
	--print @prob
	set @prob =((@prob/len(@cadena1))*100);
	print @cadena1+space(5)+(@nomb)
	print 'El porcentaje de similitud es: '+str(@prob)+'%'
	print '--------------------'

fetch listarest into @nomb
end
close listarest
deallocate listarest