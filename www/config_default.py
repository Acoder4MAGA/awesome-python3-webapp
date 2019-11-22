'''
Default configuration.开发环境数据库配置.
'''

configs = {
	'debug': True,
	'db': {
		'host': '127.0.0.1',
		'port': 3306,
		'user': 'master',
		'password': 'master',
		'db': 'pythonweb'
	},
	'session': {
		'secret': 'Awesome'
	}
}