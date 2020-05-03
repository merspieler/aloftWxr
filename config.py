# Copyright (C) 2020 Merspieler, merspieler _at_ airmail.cc
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

import sys
import os

class config:
	def __init__(self):
		self.host = "localhost"
		self.port = 1711
		self.localPort = 1712
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
				print("  -h, --help         Shows this help and exit")
				print("  -f, --host         FlightGear host. Default 'localhost'")
				print("  -p, --port         FLightGear port. Default 1711")
				print("  -P, --localPort    aloftWxr port. Default 1712")
				print("  -t, --tmp          Directory for temporary files")
				sys.exit(0)
			elif sys.argv[i] == "-f" or sys.argv[i] == "--host":
				i += 1
				self.host = sys.argv[i]
			elif sys.argv[i] == "-p" or sys.argv[i] == "--port":
				i += 1
				self.port = sys.argv[i]
			elif sys.argv[i] == "-P" or sys.argv[i] == "--localPort":
				i += 1
				self.locaPort = sys.argv[i]
			elif sys.argv[i] == "-t" or sys.argv[i] == "--tmp":
				i += 1
				self.tmpPath = sys.argv[i]
			i += 1
