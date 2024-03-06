import uuid
import datetime

class BaseModel:

	def __init__(self, *arg, **kwargs):
		if kwargs:
			for attr, value in kwargs.items():
				if attr != '__class__':
					if attr in ['created_at', 'updated_at']:
						date_string = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%f')
						parse_date = datetime.datetime.strptime(date_string, '%Y-%m-%dT%H:%M:%S.%f' )
						setattr(self,attr, parse_date)
					else:
						setattr(self, attr, value)
		else:
			self.id = str(uuid.uuid4())
			date = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f") 
			self.created_at =  datetime.datetime.strptime(date, '%Y-%m-%dT%H:%M:%S.%f')
			self.updated_at = self.created_at
			

	def save(self):
		self.updated_at = datetime.datetime.now()
	
	def to_dict(self):
		dict_class = self.__dict__
		dict_class['__class__'] = self.__class__.__name__
		return dict_class

	def __str__(self):
		return ("[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__ ))
	