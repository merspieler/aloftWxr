import sys
import os

class config:
	def __init__(self):
		self.host = "localhost"
		self.port = 1711
		if os.name == 'nt': # If on windows
			# TODO give windows path
			pass
		else:
			self.tmpPath = "/tmp"

		argc = len(sys.argv)
		i = 1
		while i < argc:
			if sys.argv[i] == "-h" or sys.argv[i] == "--help":
				print("Usage: aloftWxr.py [OPTIONS]")
				print("Fetch live weather from NOAA servers and loads it into FlightGear")
				print("OPTIONS")
				print("  -h, --help     Shows this help and exit")
				print("  -f, --host     FlightGear host. Default 'localhost'")
				print("  -p, --port     FLightGear port. Default 1711")
				print("  -t, --tmp      Directory for temporary files")
				sys.exit(0)
			elif sys.argv[i] == "-f" or sys.argv[i] == "--host":
				i += 1
				self.host = sys.argv[i]
			elif sys.argv[i] == "-p" or sys.argv[i] == "--port":
				i += 1
				self.port = sys.argv[i]
			elif sys.argv[i] == "-t" or sys.argv[i] == "--tmp":
				i += 1
				self.tmpPath = sys.argv[i]
			i += 1
