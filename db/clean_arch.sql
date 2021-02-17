DROP TABLE IF EXISTS todolist_tickets;
DROP TABLE IF EXISTS todolist_boards;

CREATE TABLE todolist_boards (
    id SERIAL,
    title VARCHAR(128) NOT NULL,
    creation_date TIMESTAMP NOT NULL,
    CONSTRAINT pk_todolist_boards PRIMARY KEY (id)
);

CREATE TABLE todolist_tickets (
    id SERIAL,
    board_id INT NOT NULL,
    title VARCHAR(128) NOT NULL,
    description TEXT DEFAULT NULL,
    labels TEXT DEFAULT NULL,
    creation_date TIMESTAMP NOT NULL,
    CONSTRAINT pk_todolist_tickets PRIMARY KEY (id),
    CONSTRAINT fk_todolist_tickets_todolist_boards FOREIGN KEY (board_id) REFERENCES todolist_boards(id)
);