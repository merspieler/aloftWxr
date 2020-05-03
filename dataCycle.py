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

from time import time, gmtime

class dataCycle:
	def __init__(self):
		timeStamp = gmtime(time() - 18000)
		self.hour = timeStamp.tm_hour
		self.day = timeStamp.tm_mday
		self.month = timeStamp.tm_mon
		self.year = timeStamp.tm_year
		self.cycle = self.hour - (self.hour % 6)
	def getString(self):
		return '{:04d}{:02d}{:02d}/{:02d}'.format(self.year, self.month, self.day, self.cycle)
