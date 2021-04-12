import schedule
import time
import threading

from news_data_creation.news_url_extraction import get_urls


def run_threaded(job_func, *args):
    job_thread = threading.Thread(target=job_func, args=args)
    job_thread.start()


def schedule_tasker():
    # schedule.every(2).seconds.do(fetch_template_keywords_from_csv)
    # schedule.every(2).seconds.do(fetch_queries_and_save_to_db)      # csv to gise_derived_query
    schedule.every(2).seconds.do(run_threaded, get_urls)
    print("--------------------- schedule_tasker ---------------------------------")
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    schedule_tasker()
