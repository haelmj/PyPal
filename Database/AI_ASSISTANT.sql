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
Name varchar(20) not null,
Passcode varchar(70) not null,
Email varchar(30),
EmailPassword nvarchar(100))
go

create table AI_USER.DATA(
Memory varchar(max),
CreatedAt date default getdate())
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


--procedure to delete data in all tables
create procedure dbreset
as
begin
delete from ASSISTANT.AI
delete from AI_USER.INFO
delete from AI_USER.DATA
end
go

--procedure to create setup app
create procedure setup
@Aname varchar(20),
@Uname varchar(20),
@Password varchar(70)
as 
begin
insert into ASSISTANT.AI values(@Aname, @Uname)
insert into AI_USER.INFO values(@Uname, @Password)
end
go

--create procedures for retrieving memory data by date
--create trigger for password encryption
exec dbreset