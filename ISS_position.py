import ephem, datetime

iss = ephem.readtle("ISS", 
            "1 25544U 98067A   21343.41105832  .00001026  00000-0  26844-4 0  9994",
            "2 25544  51.6429 196.3067 0004267 290.0753 127.4657 15.48949375315754")

print((iss.name))

observer = ephem.Observer()
observer.lat, observer.lon, observer.elev = "35.9", "51.0", 1100
observer.date = str(datetime.datetime.now() - datetime.timedelta(hours=3.5))


iss.compute(observer)

print(iss.sublat, iss.sublong)


from sgp4.api import Satrec
from sgp4.api import jday

s = '1 25544U 98067A   19343.69339541  .00001764  00000-0  38792-4 0  9991'
t = '2 25544  51.6439 211.2001 0007417  17.6667  85.6398 15.50103472202482'
satellite = Satrec.twoline2rv(s, t)

print(list((datetime.datetime.now() - datetime.timedelta(hours=3.5)).timetuple())[:6])
jd, fr = jday(list((datetime.datetime.now() - datetime.timedelta(hours=3.5)).timetuple())[:6])
e, r, v = satellite.sgp4(jd, fr)


print(r)  # True Equator Mean Equinox position (km)
print(v)  # True Equator Mean Equinox velocity (km/s)


