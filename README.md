# -DATA_ENGINEERING-PROJECT2-Dection-of-Possible-Distressed-Company


```sql

DROP TABLE IF EXISTS security;
DROP TABLE IF EXISTS company;


CREATE TABLE exchange(
exchange_id INT UNSIGNED NOT NULL AUTO_INCREMENT,
name VARCHAR(30) NOT NULL UNIQUE,
PRIMARY KEY(exchange_id)) 
AUTO_INCREMENT=1
ENGINE=InnoDB;



CREATE TABLE company(
company_id INT UNSIGNED NOT NULL AUTO_INCREMENT,
company_name VARCHAR(255) NOT NULL,
sector VARCHAR(45) NOT NULL,
industry VARCHAR(255) NOT NULL,
PRIMARY KEY(company_symbol))
AUTO_INCREMENT=1
ENGINE=InnoDB;



CREATE TABLE security(
company_id INT UNSIGNED NOT NULL AUTO_INCREMENT,
exchange_id INT UNSIGNED NOT NULL,
code VARCHAR(20) NOT NULL UNIQUE,
status VARCHAR(10) NOT NULL,
security_created DATETIME DEFAULT CURRENT_TIMESTAMP,
security_modified DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
PRIMARY KEY(company_id),
FOREIGN KEY(company_id) REFERENCES company(company_id) ON DELETE CASCADE,
FOREIGN KEY(exchange_id) REFERENCES exchange(exchange_id) ON DELETE NO ACTION)
AUTO_INCREMENT=1
ENGINE=InnoDB;


CREATE TABLE price(
price_id INT UNSIGNED NOT NULL AUTO_INCREMENT,
company_id INT UNSIGNED NOT NULL,
date VARCHAR(10) NOT NULL,
open DOUBLE NOT NULL,
high DOUBLE NOT NULL,
low DOUBLE NOT NULL,
close DOUBLE NOT NULL,
volume INT UNSIGNED NOT NULL,
adjusted DOUBLE NOT NULL,
dividend DOUBLE NOT NULL,
PRIMARY KEY(price_id),
FOREIGN KEY(company_id) REFERENCES security(company_id)) 
AUTO_INCREMENT=1
ENGINE=InnoDB;


CREATE TABLE statement_type(
type_id INT UNSIGNED NOT NULL AUTO_INCREMENT,
type_name VARCHAR(50) NOT NULL,
PRIMARY KEY(type_id))
AUTO_INCREMENT=1
ENGINE=InnoDB;

CREATE TABLE statement_line(
line_id INT UNSIGNED NOT NULL AUTO_INCREMENT,
type_id INT UNSIGNED NOT NULL,
line_name VARCHAR(100) NOT NULL,
PRIMARY KEY(line_id),
FOREIGN KEY(type_id) REFERENCES statement_type(type_id) ON DELETE SET CASCADE)
AUTO_INCREMENT=1
ENGINE=InnoDB;

CREATE TABLE statement_fact(
fact_id INT UNSIGNED NOT NULL AUTO_INCREMENT,
line_id INT UNSIGNED NOT NULL,
fiscal_year INT(4) NOT NULL,
fiscal_month INT(2) NOT NULL,
currency VARCHAR(5) NOT NULL,
unit VARCHAR(10) NOT NULL,
value DOUBLE NOT NULL,
PRIMARY KEY(fact_id),
FOREIGN KEY(line_id) REFERENCES statement_line(line_id) ON DELETE SET NULL)
AUTO_INCREMENT=1
ENGINE=InnoDB;



CREATE TABLE security_has_statement(
shs_id INT UNSIGNED NOT NULL AUTO_INCREMENT,
company_id INT UNSIGNED NOT NULL,
fact_id INT UNSIGNED NOT NULL,
PRIMARY KEY(shs_id),
FOREIGN KEY(company_id) REFERENCES security(company_id) ON DELETE CASCADE,
FOREIGN KEY(fact_id) REFERENCES statement_fact(fact_id) ON DELETE CASCADE)
AUTO_INCREMENT=1
ENGINE=InnoDB;














```
