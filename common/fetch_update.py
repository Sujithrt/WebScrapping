import psycopg2

# from news_constants import postgres_username, postgres_pwd, postgres_host, postgres_database


def insert_urls_to_news_urls(url, page_url, page_number):
    result = ''
    cursor = None
    connection = None
    try:
        connection = psycopg2.connect(user='news_engine', password='IP2021', host='localhost', port="5432",
                                      database='news_data_collection')
        cursor = connection.cursor()
        # sourceid = str(id)
        postgresquery = "insert into news_urls(url,page_url,page_number) values ("
        postgresquery = postgresquery + "'" + str(url) + "' ,"
        postgresquery = postgresquery + "'" + str(page_url) + "' ,"
        postgresquery = postgresquery + "'" + str(page_number) + "')"
        print("postgresquery---->  ", postgresquery)
        cursor.execute(postgresquery)
        connection.commit()
        del postgresquery
        result = 'COMPLETED'
        return result
    except (Exception, psycopg2.Error) as error:
        if connection is not None:
            print("Exception in insert_urls_to_news_urls --", error)
    finally:
        if cursor is not None:
            cursor.close()
        if connection is not None:
            connection.close()
    return result


def fetch_data_from_news_urls():
    cursor = None
    connection = None
    result_lst = []

    try:
        connection = psycopg2.connect(user='news_engine', password='IP2021', host='localhost', port="5432",
                                      database='news_data_collection')
        cursor = connection.cursor()
        postgresquery = "select id, url from news_urls where status = 'N' limit 10;"
        print("postgresquery---> ", postgresquery)
        cursor.execute(postgresquery)
        # result_set = cursor.fetch_one()
        result_set = cursor.fetchall()
        for result_obj in result_set:
            new_dict = {}
            new_dict["id"] = result_obj[0]
            new_dict["url"] = result_obj[1]
            result_lst.append(new_dict)
        connection.commit()
        del postgresquery
    except Exception as exp:
        if connection is not None:
            print("Exception in fetch_data_from_news_urls --", exp)
    finally:
        if cursor is not None:
            cursor.close()
        if connection is not None:
            connection.close()
    return result_lst


def insert_content_to_news_content(id, title, published_date, published_year):
    result = ''
    cursor = None
    connection = None
    try:
        connection = psycopg2.connect(user='news_engine', password='IP2021', host='localhost', port="5432",
                                      database='news_data_collection')
        cursor = connection.cursor()
        # sourceid = str(id)
        postgresquery = "insert into news_content(news_urls_id, title, published_date, published_year) values ("
        postgresquery = postgresquery + "'" + str(id) + "' ,"
        postgresquery = postgresquery + "'" + str(title).replace("'","").replace('"','') + "' ,"
        # postgresquery = postgresquery + "'" + str(description) + "' ,"
        postgresquery = postgresquery + "'" + str(published_date) + "' ,"
        # postgresquery = postgresquery + "'" + str(published_year) + "' ,"
        postgresquery = postgresquery + "'" + str(published_year) + "')"
        print("postgresquery---->  ", postgresquery)
        cursor.execute(postgresquery)
        update_news_urls_to_Y(id)
        connection.commit()
        del postgresquery
        result = 'COMPLETED'
        return result
    except (Exception, psycopg2.Error) as error:
        if connection is not None:
            print("Exception in insert_content_to_news_content --", error)
    finally:
        if cursor is not None:
            cursor.close()
        if connection is not None:
            connection.close()
    return result


def update_news_urls_to_Y(id):
    cursor = None
    connection = None
    result = 'COMPLETED'

    try:
        connection = psycopg2.connect(user='news_engine', password='IP2021', host='localhost', port="5432",
                                      database='news_data_collection')

        cursor = connection.cursor()

        postgresquery = "update news_urls set status='Y' where id = '" + str(id) + "'"
        cursor.execute(postgresquery)
        connection.commit()
        del postgresquery
    except (Exception, psycopg2.Error) as error:
        if connection is not None:
            print("Exception in update_news_urls --", error)
    finally:
        if cursor is not None:
            cursor.close()
        if connection is not None:
            connection.close()
    return result


def update_news_urls_to_P(id):
    cursor = None
    connection = None
    result = 'COMPLETED'

    try:
        connection = psycopg2.connect(user='news_engine', password='IP2021', host='localhost', port="5432",
                                      database='news_data_collection')

        cursor = connection.cursor()

        postgresquery = "update news_urls set status='P' where id = '" + str(id) + "'"
        cursor.execute(postgresquery)
        connection.commit()
        del postgresquery
    except (Exception, psycopg2.Error) as error:
        if connection is not None:
            print("Exception in update_news_urls --", error)
    finally:
        if cursor is not None:
            cursor.close()
        if connection is not None:
            connection.close()
    return result

# update_news_urls_to_P(12189)