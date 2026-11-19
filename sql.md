```sql
CREATE TABLE table_name (
    column_1 INT PRIMARY KEY,
    column_2 VARCHAR(50) NOT NULL,
    column_3 VARCHAR(20) CHECK (column_3 IN ('value_1', 'value_2', 'value_3')),
    column_4 DECIMAL(10,2),
);

ALTER TABLE table_name ADD CONSTRAINT constraint_pk PRIMARY KEY (column_name);

CREATE TABLE junction_table (
    parent_1_id INTEGER NOT NULL,
    parent_2_id INTEGER NOT NULL,
    quantity_col INTEGER,
    CONSTRAINT pk_junction PRIMARY KEY (parent_1_id, parent_2_id),
    CONSTRAINT fk_parent_1 FOREIGN KEY (parent_1_id) REFERENCES parent_table_1(parent_1_id) ON DELETE CASCADE,
    CONSTRAINT fk_parent_2 FOREIGN KEY (parent_2_id) REFERENCES parent_table_2(parent_2_id)
);

ALTER TABLE table_name ADD new_column VARCHAR(20) DEFAULT 'default_value';
ALTER TABLE table_name ALTER COLUMN column_name SET DEFAULT 'new_default_value';

INSERT INTO table_name 
VALUES (val_1, 'string_val_2', 'string_val_3', 'string_val_4', 'string_val_5', 12345);

INSERT INTO table_name (column_1, column_2, column_3, column_6) 
VALUES (val_1, 'string_val_2', 'string_val_3', 100.50);

SELECT group_column, COUNT(id_column) AS total_count
FROM table_name
WHERE filter_column IN ('val_1', 'val_2', 'val_3')
GROUP BY group_column
HAVING COUNT(id_column) > threshold_val
ORDER BY total_count DESC;

SELECT table_a.pk_column, table_a.column_1, table_b.fk_column, table_b.column_2
FROM table_a, table_b
WHERE table_a.pk_column = table_b.fk_column
ORDER BY table_a.pk_column;

SELECT table_a.pk_column, table_a.column_1, table_b.fk_column, table_b.column_2
FROM table_a 
INNER JOIN table_b ON table_a.pk_column = table_b.fk_column
ORDER BY table_a.pk_column;
```
