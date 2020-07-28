from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand

from __init__ import app, db

manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command('runserver', Server(

	use_debugger = True,
	use_reloader = True,
	host = '0.0.0.0',
	port = 8080
	))

manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
	manager.run()