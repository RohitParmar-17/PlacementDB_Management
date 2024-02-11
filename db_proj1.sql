create database db_proj1;
use db_proj1;
drop database db_proj1;
create table Company
(
Cpregno int primary key,
Cpname varchar(20),
CpDomain varchar(20)
);

create table College
(
Cregid int primary key,
Cname varchar(20),
Clocation varchar(20)
);

create table Job
(
Japplication int primary key,
Jdescription varchar(20),
Jrole varchar(20),
Cpregno int ,
foreign key(Cpregno) references Company(Cpregno) on delete set null on update cascade
);

create table Interviewer
(
Iid int primary key,
Iname varchar(20),
Iexp int,
Cpregno int ,
foreign key(Cpregno) references Company(Cpregno) on delete set null on update cascade
);
drop table Student;
create table Student
(
Sid int primary key,
Sname varchar(20),
Sage int,
Iid int ,
foreign key(Iid) references Interviewer(Iid) on delete set null on update cascade,
Cregid int ,
foreign key(Cregid) references College(Cregid) on delete set null on update cascade
);

select * from Company;
select * from College;
select * from Job;
select * from Interviewer;
select * from Student;