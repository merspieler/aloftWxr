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

import socket

class aircraftPos:
	def __init__(self, lat, lon, alt):
		self.lat = lat
		self.lon = lon
		self.alt = alt

class connection:
	def __init__(self, conf):
		try:
			self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			self.sock.bind('0.0.0.0', conf.localPort)
		except:
			print("ERROR: Unable to open socket")
	def sendData(self, wp):
		wpt = '{:f},{:f}'.format(wp.lat, wp.lon)
		for w in wp:
			wpt += ',{:f},{:f}'.format(w.direction, w.speed)
		self.sock.sendto(wpt.encode(), (conf.host, conf.port))
	def receiveData(self):
		msg, addr = self.sock.recvfrom(1024);
		lat, lon, alt = msg.split(,)
		return aircraftPos(lat, lon, alt)
