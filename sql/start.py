import sqlite3

# in memory db
# conn = sqlite3.connect(":memory:")


def main():
    """
    DATATYPES
    NULL, INTEGER, REAL (float), TEXT, BLOB (file like mp3 etc.)
    """
    conn = sqlite3.connect("customer.db")
    c = conn.cursor()
    c.execute(
        """CREATE TABLE customers (
        first_name text,
        last_name text,
        email text
        
        )



    """
    )
    # save
    conn.commit()
    conn.close()


if __name__ == "__main__":
    main()
