DROP TABLE IF EXISTS words_data;

CREATE TABLE words_data (
  job_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
  url TEXT, words_count INTEGER,
  submitted_on TEXT,
  status TEXT);
