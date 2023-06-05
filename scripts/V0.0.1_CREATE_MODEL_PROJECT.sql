CREATE TABLE project (
    id INT NOT NULL AUTO_INCREMENT,
    company_id INT NOT NULL,
    name_project VARCHAR(100) NOT NULL,
    enabled VARCHAR(3) NOT NULL,
    CONSTRAINT pk_project primary key(id)
);