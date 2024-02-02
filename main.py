import sqlite3
import uuid
import logging
from src.config.app_config import AppConfig
from src.business.admin_business import AdminBusiness
from src.business.rider_business import RiderBusiness
from src.controllers.admin_controller import AdminController
from src.controllers.rider_controller import RiderController
from src.views.admin_view import Admin
from src.views.home_view import HomePage
from src.views.login_view import Login
from src.views.register_view import Register
from src.views.publisher_view import Publisher
from src.controllers.auth_controller import AuthController
from src.controllers.publisher_controller import PublisherController
from src.business.auth_business import AuthBusiness
from src.database.database import Database
from src.business.publisher_business import PublisherBusiness
from src.views.rider_view import Rider

logging.basicConfig(
    format='%(asctime)s %(levelname)-8s [%(filename)s %(funcName)s:%(lineno)d] %(message)s',
    level=logging.DEBUG,
    filename=AppConfig.LOG_PATH
)
logger = logging.getLogger(__name__)

if __name__ == '__main__':
    id=str(uuid.uuid1())
    print(id)

    # path= r"C:\Users\rnarang\PycharmProjects\CarPooling\src\database\CarPooling.db"
    # connection=sqlite3.connect(path)
    # cursor= connection.cursor()
    # cursor.execute("CREATE('e15bcbad-be67-11ee-bee4-d41b810ba6e8','AB Colony,Rohtak','CD Colony,Noida','2024-09-01','23')")
    # connection.commit()
    # connection.close()

    database=Database()

    admin_business = AdminBusiness()
    admin_controller = AdminController(admin_business)
    admin_view = Admin(admin_controller)

    publisher_business=PublisherBusiness(database)
    publisher_controller=PublisherController(publisher_business)
    publisher_view=Publisher(publisher_controller)

    rider_business = RiderBusiness(database)
    rider_controller = RiderController(rider_business)
    rider_view = Rider(rider_controller, publisher_controller)

    auth_business=AuthBusiness(database)
    auth_controller=AuthController(auth_business)
    login = Login(publisher_view,auth_controller,rider_view)
    register=Register(auth_controller)

    home_page=HomePage(login,register)
    home_page.start()

    #choose vehicle
    #add vehicle constraint
    #book ride constraint

