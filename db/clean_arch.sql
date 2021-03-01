DROP TABLE IF EXISTS todolist_tickets;
DROP TABLE IF EXISTS todolist_board_columns;
DROP TABLE IF EXISTS todolist_boards;

CREATE TABLE todolist_boards (
    id SERIAL,
    title VARCHAR(128) NOT NULL,
    created_at TIMESTAMP NOT NULL,
    updated_at TIMESTAMP NOT NULL,
    CONSTRAINT pk_todolist_boards PRIMARY KEY (id)
);

CREATE TABLE todolist_board_columns (
    id SERIAL,
    board_id INT NOT NULL,
    name VARCHAR(32) NOT NULL,
    created_at TIMESTAMP NOT NULL,
    updated_at TIMESTAMP NOT NULL,
    CONSTRAINT pk_todolist_board_columns PRIMARY KEY (id),
    CONSTRAINT fk_todolist_board_columsn_todolist_boards FOREIGN KEY (board_id) REFERENCES todolist_boards(id)
);

CREATE TABLE todolist_tickets (
    id SERIAL,
    board_column_id INT DEFAULT NULL,
    title VARCHAR(128) NOT NULL,
    description TEXT DEFAULT NULL,
    priority INT DEFAULT 0,
    labels TEXT DEFAULT NULL,
    created_at TIMESTAMP NOT NULL,
    updated_at TIMESTAMP NOT NULL,
    CONSTRAINT pk_todolist_tickets PRIMARY KEY (id),
    CONSTRAINT fk_todolist_tickets_todolist_board_columns FOREIGN KEY (board_column_id) REFERENCES todolist_board_columns(id)
);