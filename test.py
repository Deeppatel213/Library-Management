import psycopg2
import csv

try:
    connection = psycopg2.connect(user="postgres",password="1234",host="127.0.0.1",port="5432",database="test")
    cursor = connection.cursor()
    with open('C:\\Users\\RAKESH\\Desktop\\archive\\books1.csv') as f:
        read_row = csv.read(f)
        for row in read_row:
            x = tuple(row)
            print(x)
            postgres_insert_query = """ INSERT INTO user_booksdata (title,authors,published_year,average_rating,num_pages,rating_count,bookshelf_number,level) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
            record_to_insert = x
            cursor.execute(postgres_insert_query, record_to_insert)
            connection.commit()
            count = cursor.rowcount
            print(count, "Record inserted successfully into mobile table")

except (Exception, psycopg2.Error) as error:
    print("Failed to insert record into mobile table", error)

finally:
    # closing database connection.
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")