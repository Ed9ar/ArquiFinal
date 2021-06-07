create database users_twitters;
use users_twitters;

create table users (id int not null primary key auto_increment, username varchar(255) NOT NULL);

insert into users (username) values ("@elonmusk");
insert into users (username) values ("@BillGates");
insert into users (username) values ("@tim_cook");
insert into users (username) values ("@Wendys");
insert into users (username) values ("@Spotify");
insert into users (username) values ("@awscloud");
insert into users (username) values ("@Cinepolis");
insert into users (username) values ("@PrimeVideo");
insert into users (username) values ("@InvincibleHQ");
insert into users (username) values ("@kfc");
