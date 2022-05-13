import csv
import sqlite3
import pandas as pd

columns = ['id','MSIND','engagement','experience','satisfaction']

class SavingToSQL:
	def __init__(self, df:pd.DataFrame):
		# initializing model
		self.df = df
		self.connection = sqlite3.connect('telco.db')
		self.cursor = self.connection.cursor()
		print('Automation in Action...!!!')

	def create_table(self):
		create_table = '''CREATE TABLE user_experience(id INTEGER PRIMARY KEY AUTOINCREMENT,
							MSIND NUMBER NOT NULL,
							engagement NUMBER NOT NULL,
							experience NUMBER NOT NULL,
							satisfaction NUMBER NOT NULL,
							
						)
						'''
		print('Table creaton in action...!!!')
		try:
			self.cursor.execute(create_table)
		except sqlite3.OperationalError:
			print('Table already exists...')

	def csv_to_sql(self):
		contents = pd.read_csv(self.df)
		self.connection.commit()
		contents.to_sql('user_experience', self.connection, if_exists='replace', index=True)
		self.connection.commit()

	def sql_fetchall(self):
		self.cursor.execute('''SELECT * FROM user_experience''')
		display = pd.DataFrame(self.cursor.fetchall())
		display.columns = columns
		print(display)
		self.connection.commit()

	def sql_close(self):
		self.connection.close()

def fetchall():
	connection = sqlite3.connect('telco.db')
	cursor = connection.cursor()
	cursor.execute('''SELECT * FROM user_experience''')
	display = pd.DataFrame(cursor.fetchall())
	display.columns = columns
	print(display)
	connection.commit()
	connection.close()
	return display

if __name__ == '__main__':
	file = '../data/experience_data.csv'
	obj = SavingToSQL(file)
	obj.create_table()
	obj.csv_to_sql()
	obj.sql_fetchall()
	fetchall()
	obj.sql_close()