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

def getForecast(cycle):
	ts = gmtime(time() - 18000)
	return ts.tm_hour - (ts.tm_hour % 3)

def getFilename(dc, fc):
	return 'gfs.t{:02d}z.pgrb2full.0p50.f0{:02d}'.format(dc.cycle, fc)

def getMillibars(alt):
	if alt < 710 or alt > 54000: # 1000mb and 75mb
		return -9999;
	if alt >= 710 and alt < 1410:
		return 975;
	if alt >= 1410 and alt < 2135:
		return 950;
	if alt >= 2135 and alt < 2875:
		return 925;
	if alt >= 2875 and alt < 4000:
		return 900;
	if alt >= 4000 and alt < 5600:
		return 850;
	if alt >= 5600 and alt < 7235:
		return 800;
	if alt >= 7235 and alt < 8995:
		return 750;
	if alt >= 8995 and alt < 10820:
		return 700;
	if alt >= 10820 and alt < 12775:
		return 650;
	if alt >= 12775 and alt < 14865:
		return 600;
	if alt >= 14865 and alt < 17100:
		return 550;
	if alt >= 17100 and alt < 19530:
		return 500;
	if alt >= 19530 and alt < 22160:
		return 450;
	if alt >= 22160 and alt < 25065:
		return 400;
	if alt >= 25065 and alt < 27450:
		return 350;
	if alt >= 27450 and alt < 29170:
		return 325;
	if alt >= 29170 and alt < 31000:
		return 300;
	if alt >= 31000 and alt < 32965:
		return 275;
	if alt >= 32965 and alt < 35100:
		return 250;
	if alt >= 35100 and alt < 37400:
		return 225;
	if alt >= 37400 and alt < 39950:
		return 200;
	if alt >= 39950 and alt < 42800:
		return 175;
	if alt >= 42800 and alt < 46000:
		return 150;
	if alt >= 46000 and alt < 49750:
		return 125;
	if alt >= 49750 and alt < 54000:
		return 100;
	return -9999;
