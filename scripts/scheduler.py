from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.daily import DailyTrigger  # You can choose other triggers like WeeklyTrigger
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor
from src.database import get_async_db
from src.services.categorize_customer import categorize_customers
import atexit

scheduler = BackgroundScheduler()
jobstore = {
    'default': SQLAlchemyJobStore(url='sqlite:///jobs.sqlite')  
}
executors = {
    'default': ThreadPoolExecutor(20),
    'processpool': ProcessPoolExecutor(5)
}
scheduler.configure(jobstores=jobstore, executors=executors)

# Define the function you want to schedule
def categorize_customers_job():
    with get_async_db() as db: 
        categorize_customers(db)  # Call  categorize_customers function

# Schedule the job to run daily at a specific time (e.g., midnight)
scheduler.add_job(
    categorize_customers_job,
    trigger=DailyTrigger(hour=0, minute=0, second=0),  # Adjust the time as needed
    id='categorize_customers',
    name='Categorize Customers Job',
    replace_existing=True,
)

# Register an exit handler to shut down the scheduler gracefully when the application exits
atexit.register(lambda: scheduler.shutdown())
