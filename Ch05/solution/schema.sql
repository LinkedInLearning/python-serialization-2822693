-- UFO database schema
CREATE TABLE records (
    time TIMESTAMP,
    lat DOUBLE,
    lng DOUBLE,
    shape VARCHAR(128)
);
