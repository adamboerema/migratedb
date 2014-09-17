from subprocess import call
from datetime import datetime
import time


#dump and back up a database to the tmp folder
def mysql_dump(user, password, host, db_name, timestamp):
    call("mysqldump "
         "--user=" + user +
         " --password=" + password +
         " --host=" + host +
         " " + db_name +
         "> /tmp/" + db_name + "_" + timestamp + ".sql", shell=True)


#import a database dump into another database
def mysql_import(user, password, host, db_name, migrate_db_name, timestamp):
    call("mysql "
         "--user=" + user +
         " --password=" + password +
         " --host=" + host +
         " " + migrate_db_name +
         "< /tmp/" + db_name + "_" + timestamp + ".sql", shell=True)

#config
db_user = ""
db_password = ""
db_host = ""
db_name = ""
db_migrate_name = ""

date = datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d')


#Backup database
mysql_dump(db_user, db_password, db_host, db_name, date)
mysql_import(db_user, db_password, db_host, db_name, db_migrate_name, date)

