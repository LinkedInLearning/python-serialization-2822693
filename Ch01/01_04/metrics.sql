-- Metric data in SQL
CREATE TABLE metrics (
    id INTEGER,
    time TIMESTAMP,
    name VARCHAR(32),
    value FLOAT
);


CREATE TABLE lables (
    metric INTEGER,
    key VARCHAR(32),
    value VARCHAR(32),

    FOREIGN KEY(metric) REFERENCES metrics(id)
);
