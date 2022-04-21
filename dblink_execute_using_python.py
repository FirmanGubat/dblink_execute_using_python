#Package
import psycopg2

# connect to PostgreSQL Target
source_host = "host"
source_port = "port"
source_dbname = "database_name"
source_name_user = "username"
source_password = "pass"

#DBLink
def dblink():
    try:
        dblink_conn = psycopg2.connect(host=source_host, port=source_port, dbname=source_dbname, user=source_name_user, password=source_password)
        dblink_cursor = dblink_conn.cursor()
        # execute query
        dblink_cursor.execute(""" select dblink_connect('myconn',
						                                    'host=source_host
						                                    port=source_port
						                                    dbname=source_database_name
						                                    user=source_username
						                                    password=source_pass');

                                    create table schema.table_name as
                                    select * from
                                    dblink('myconn','select * from schema.table_name') as t1(
                                	DDL Table);""")
        dblink_conn.commit()
        print("Copy Table Succeeded")

    except Exception as e:
        print("Copy Table Error: " + str(e))
    finally:
        dblink_conn.close()

try:
    dblink()
except Exception as e:
    print("Error while Copy Table: " + str(e))
