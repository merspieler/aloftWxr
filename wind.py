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

class wind:
	direction = 0
	speed = 0

class windpoint:
	def __init__(self):
		self.lat = 0
		self.lon = 0
		self.winds = []
		i = 0
		while i < 9:
			self.winds.append(wind())
			i += 1
