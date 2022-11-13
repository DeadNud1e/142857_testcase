-- Creation of product table
CREATE TABLE IF NOT EXISTS product (
  product_id INT NOT NULL,
  name varchar(250) NOT NULL,
  PRIMARY KEY (product_id)
);

-- Creation of category table
CREATE TABLE IF NOT EXISTS category (
  category_id INT NOT NULL,
  name varchar(250) NOT NULL,
  PRIMARY KEY (category_id)
);

-- Creation of productCategory table
CREATE TABLE IF NOT EXISTS productCategory (
  product_id INT NOT NULL,
  category_id INT NOT NULL,
  CONSTRAINT PK_productCategory PRIMARY KEY ( product_id, category_id ),
  CONSTRAINT fk_product
      FOREIGN KEY(product_id) 
	  REFERENCES product(product_id),
  CONSTRAINT fk_category
      FOREIGN KEY(category_id) 
	  REFERENCES category(category_id)
);

-- Filling db
set session my.number_of_products = '5';
set session my.number_of_categories = '5';

INSERT INTO product
select product_id, concat('Product ', product_id) 
FROM GENERATE_SERIES(1, current_setting('my.number_of_products')::int) as product_id;

INSERT INTO category
select category_id, concat('Category ', category_id) 
FROM GENERATE_SERIES(1, current_setting('my.number_of_categories')::int) as category_id;

INSERT INTO productCategory (product_id, category_id) VALUES(1, 1);
INSERT INTO productCategory (product_id, category_id) VALUES(1, 3);
INSERT INTO productCategory (product_id, category_id) VALUES(2, 3);
INSERT INTO productCategory (product_id, category_id) VALUES(4, 4);
INSERT INTO productCategory (product_id, category_id) VALUES(4, 2);
INSERT INTO productCategory (product_id, category_id) VALUES(5, 1);
