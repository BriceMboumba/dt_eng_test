drop table if exists db_dteng;

create table people (
  id int not null auto_increment,
  given_name varchar(50) default null,
  family_name varchar(50) default null,
  date_of_birth varchar(50) default null,
  place_of_birth varchar(50) default null,
  primary key (id)
);

create table places (
  id int not null auto_increment,
  city varchar(50) default null,
  county varchar(50) default null,
  country varchar(50) default null,
  primary key (id)
);

create table keys (
  id int not null auto_increment,
  people_id int,
  places_id int,
  primary key (id),
  foreign key (people_id) references people(id),
  foreign key (places_id) references places(id),
);

