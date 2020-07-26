create database academico
create table alumnou
(
ci varchar(10),
nombre varchar(20),
apellidoP varchar(20),
apellidoM varchar(20)
)

INSERT INTO alumno (ci, nombre, apellidoP, apellidoM) VALUES ('24', 'Alvaro', 'Vallejos', 'Perez');
INSERT INTO alumno (ci, nombre, apellidoP, apellidoM) VALUES ('25', 'Aramiz', 'Acarapi', 'Quiroga');



declare @cadena1 varchar(30),
		@cadena2 varchar(30),
		@cont integer,
		@prob float,
		@v varchar(2);
set @cadena1='brayan';
set @cadena2='brian';
set @cont=1;
set	@prob=0;
while @cont<=LEN(@cadena1)
begin
Set @v=SUBSTRING(@cadena1,@cont,1)
	if @v=SUBSTRING(@cadena2,@cont,1)
		begin
			 set @prob=@prob+1;
		end
--print (@v);
--print(@cont)
set @cont=@cont+1;
end
print((@prob/len(@cadena1))*100);