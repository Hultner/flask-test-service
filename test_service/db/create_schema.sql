-- Creates needed schema and tables
BEGIN;
CREATE SCHEMA IF NOT EXISTS flask_test;
CREATE TABLE IF NOT EXISTS flask_test.note (
    id      serial PRIMARY KEY,
    title   text NOT NULL,
    body    text
);
COMMIT;
