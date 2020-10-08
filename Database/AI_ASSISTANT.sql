create database AI_ASSISTANT
use AI_ASSISTANT
go

create schema ASSISTANT
go 
create schema AI_USER
go

create table ASSISTANT.AI(
AI_NAME varchar(20) constraint ai_nm primary key, 
USER_CALL varchar(20))
go



create table AI_USER.INFO(
Userid int constraint u_id primary key identity(1,1),
Name varchar(30) not null,
Passcode nvarchar(max) not null,
Email varchar(30),
EmailPassword nvarchar(max))
go

create table AI_USER.DATA(
Memory varchar(max),
ModifiedAt date default getdate())
go

--limit the number of rows to just one
create trigger LimitTable 
on ASSISTANT.AI
after insert
as
    declare @tableCount int
    select @tableCount = Count(*) from ASSISTANT.AI

    if @tableCount > 1
    begin
        rollback
    end
go

create trigger LimTable 
on AI_USER.INFO
after insert
as
    declare @tableCount int
    select @tableCount = Count(*) from AI_USER.INFO

    if @tableCount > 1
    begin
        rollback
    end
go


--delete data in all tables
create procedure dbreset
as
begin
delete from ASSISTANT.AI
delete from AI_USER.INFO
delete from AI_USER.DATA
end
go

--setup app
create procedure setup
@Aname varchar(20),
@Uname varchar(20),
@Password varchar(70)
as 
begin
insert into ASSISTANT.AI values(@Aname, @Uname)
insert into AI_USER.INFO(Name, Passcode) values(@Uname, @Password)
end
go

--setup email service
create procedure mail
@email varchar(30),
@password nvarchar(100),
@name varchar(20)
as 
begin
update AI_USER.INFO 
set Email = @email, EmailPassword = @password 
where Name = @name
end
go
--create procedures for retrieving memory data by date
--create trigger for password encryption
create trigger PassEncrypt
on AI_USER.INFO
Instead of insert
as
begin
declare @name varchar(30)
declare @pswd nvarchar(max)
declare @salt varbinary(4) = crypt_gen_random(4)
declare @hash varbinary(max)
set @name = (select Name from inserted)
set @pswd = (select Passcode from inserted)
set @hash = 0x0200 + @salt + HASHBYTES('SHA2_512', CAST(@pswd as varbinary(max)) + @salt);
insert into AI_USER.INFO(Name, Passcode) values(@name, @hash)
end
go

--password validation
create procedure pwcompare
@pwd varchar(max)
as
begin
declare @hash nvarchar(max)
set @hash = (select Passcode from AI_USER.INFO) 
select PWDCOMPARE(@pwd, @hash) as IsPasswordHash;
end
go







