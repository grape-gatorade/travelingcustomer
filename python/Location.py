import googlemaps
from datetime import datetime
class Location(object):

	def __init__(self, new_id):
		self.__id = new_id
		self.__closing_time = 0
		self.__24hours = False


	def __lt__(self, other):
		return self._closing_time < other._closing_time


	def setClosingTime(self):
	 	gmaps = googlemaps.Client(key='AIzaSyDA3tCPe5-nZ7i8swYDskytH2cmQq6lBiA')
	 	location_info = gmaps.place(self.__id, 'English')
	 	now = datetime.now()
	 	weekday = now.strftime("%w")
	 	print weekday

	 	try:
	 		print location_info['result']['opening_hours']['periods'][int(weekday)]['close']['time']

	 	except IndexError:
	 		if location_info['result']['opening_hours']['periods'][0]['open']['day'] == 0 and location_info['result']['opening_hours']['periods'][0]['open']['time'] == '0000':
	 			self.__24hours = True
	 		else:
	 			self.__closing_time = -1

	 	except KeyError:
	 		if location_info['result']['opening_hours']['periods'][0]['open']['day'] == 0 and location_info['result']['opening_hours']['periods'][0]['open']['time'] == '0000':
	 			self.__24hours = True
	 		else:
	 			self.__closing_time = -1



	 	print self.__24hours