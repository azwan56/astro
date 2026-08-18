"""
Swiss Ephemeris & High-Precision Astronomical Calculation Engine
Standard Human Design calculations matching official Jovian Archive / MMI.

Calculates:
1. Personality (Black) planetary longitudes at UTC Birth datetime.
2. Design (Red) planetary longitudes at the exact moment when Sun is 88.0° of solar arc backwards.
3. True Lunar Nodes (True Node) as standard in Human Design.
"""

import datetime
from typing import Dict, Tuple

try:
    import swisseph as swe
    HAVE_SWISSEPH = True
except ImportError:
    HAVE_SWISSEPH = False

try:
    import ephem
    HAVE_EPHEM = True
except ImportError:
    HAVE_EPHEM = False


PLANET_MAP_SWE = {
    "Sun": 0,          # swe.SUN
    "Moon": 1,         # swe.MOON
    "Mercury": 2,      # swe.MERCURY
    "Venus": 3,        # swe.VENUS
    "Mars": 4,         # swe.MARS
    "Jupiter": 5,      # swe.JUPITER
    "Saturn": 6,       # swe.SATURN
    "Uranus": 7,       # swe.URANUS
    "Neptune": 8,      # swe.NEPTUNE
    "Pluto": 9,        # swe.PLUTO
    "North_Node": 11   # swe.TRUE_NODE (Human Design standard)
}


def datetime_to_julian_day(dt: datetime.datetime) -> float:
    """Convert UTC datetime to Julian Day Number."""
    if HAVE_SWISSEPH:
        hour_dec = dt.hour + dt.minute / 60.0 + dt.second / 3600.0 + dt.microsecond / 3600000000.0
        return swe.julday(dt.year, dt.month, dt.day, hour_dec)
    
    # Mathematical fallback
    year = dt.year
    month = dt.month
    day = dt.day + (dt.hour + dt.minute / 60.0 + dt.second / 3600.0) / 24.0
    if month <= 2:
        year -= 1
        month += 12
    A = int(year / 100)
    B = 2 - A + int(A / 4)
    return int(365.25 * (year + 4716)) + int(30.6001 * (month + 1)) + day + B - 1524.5


def julian_day_to_datetime(jd: float) -> datetime.datetime:
    """Convert Julian Day Number to UTC datetime."""
    if HAVE_SWISSEPH:
        y, m, d, h_dec = swe.revjul(jd)
        hour = int(h_dec)
        min_dec = (h_dec - hour) * 60.0
        minute = int(min_dec)
        sec = int((min_dec - minute) * 60.0)
        return datetime.datetime(y, m, d, hour, minute, sec, tzinfo=datetime.timezone.utc)

    # Fallback
    jd_adjusted = jd + 0.5
    Z = int(jd_adjusted)
    F = jd_adjusted - Z
    if Z < 2299161:
        A = Z
    else:
        alpha = int((Z - 1867216.25) / 36524.25)
        A = Z + 1 + alpha - int(alpha / 4)
    B = A + 1524
    C = int((B - 122.1) / 365.25)
    D = int(365.25 * C)
    E = int((B - D) / 30.6001)
    day = B - D - int(30.6001 * E) + F
    month = E - 1 if E < 14 else E - 13
    year = C - 4716 if month > 2 else C - 4715
    day_int = int(day)
    h_total = (day - day_int) * 24.0
    hour = int(h_total)
    m_total = (h_total - hour) * 60.0
    minute = int(m_total)
    second = int((m_total - minute) * 60.0)
    return datetime.datetime(year, month, day_int, hour, minute, second, tzinfo=datetime.timezone.utc)


def calculate_planet_longitudes(dt: datetime.datetime) -> Dict[str, float]:
    """
    Calculate high-precision tropical ecliptic longitudes for 13 celestial bodies at UTC datetime.
    Returns: { "Sun": deg, "Earth": deg, "Moon": deg, "North_Node": deg, "South_Node": deg, ... }
    """
    if HAVE_SWISSEPH:
        tjd_ut = datetime_to_julian_day(dt)
        flag = swe.FLG_SWIEPH | swe.FLG_SPEED

        longitudes = {}
        for name, planet_id in PLANET_MAP_SWE.items():
            res, _ = swe.calc_ut(tjd_ut, planet_id, flag)
            longitudes[name] = res[0] % 360.0

        # Earth is exactly opposite the Sun
        longitudes["Earth"] = (longitudes["Sun"] + 180.0) % 360.0
        # South Node is exactly opposite the North Node
        longitudes["South_Node"] = (longitudes["North_Node"] + 180.0) % 360.0
        return longitudes

    elif HAVE_EPHEM:
        d = ephem.Date(dt)
        def get_ecl(cls):
            b = cls(d)
            e = ephem.Ecliptic(b)
            return (e.lon * 180.0 / 3.141592653589793) % 360.0

        sun = get_ecl(ephem.Sun)
        # Approximate True Node
        T = (float(d) + 2415020.0 - 2451545.0) / 36525.0
        nn = (125.04452 - 1934.136261 * T + 0.0020708 * T**2) % 360.0

        return {
            "Sun": sun,
            "Earth": (sun + 180.0) % 360.0,
            "Moon": get_ecl(ephem.Moon),
            "North_Node": nn,
            "South_Node": (nn + 180.0) % 360.0,
            "Mercury": get_ecl(ephem.Mercury),
            "Venus": get_ecl(ephem.Venus),
            "Mars": get_ecl(ephem.Mars),
            "Jupiter": get_ecl(ephem.Jupiter),
            "Saturn": get_ecl(ephem.Saturn),
            "Uranus": get_ecl(ephem.Uranus),
            "Neptune": get_ecl(ephem.Neptune),
            "Pluto": get_ecl(ephem.Pluto)
        }
    else:
        raise RuntimeError("Neither pyswisseph nor ephem is installed.")


def calculate_design_datetime(dt_utc: datetime.datetime) -> Tuple[datetime.datetime, Dict[str, float]]:
    """
    Calculates the exact Design datetime and Design planetary positions (88° Solar Arc earlier).
    """
    pers_longitudes = calculate_planet_longitudes(dt_utc)
    pers_sun_lon = pers_longitudes["Sun"]
    target_sun_lon = (pers_sun_lon - 88.0) % 360.0

    if HAVE_SWISSEPH:
        tjd_pers = datetime_to_julian_day(dt_utc)
        flag = swe.FLG_SWIEPH | swe.FLG_SPEED

        # Initial estimate: ~89.2 days before birth
        tjd_des = tjd_pers - 88.0 * (365.2422 / 360.0)

        # High-precision Newton-Raphson convergence
        for _ in range(15):
            res, _ = swe.calc_ut(tjd_des, swe.SUN, flag)
            curr_lon = res[0]
            speed = res[3] # deg/day
            diff = (curr_lon - target_sun_lon + 180.0) % 360.0 - 180.0
            if abs(diff) < 1e-7:
                break
            tjd_des -= diff / speed

        dt_des_utc = julian_day_to_datetime(tjd_des)
        des_longitudes = calculate_planet_longitudes(dt_des_utc)
        return dt_des_utc, des_longitudes

    elif HAVE_EPHEM:
        d_pers = ephem.Date(dt_utc)
        t_est = ephem.Date(d_pers - 88.0 * (365.2422 / 360.0))
        for _ in range(12):
            sun = ephem.Sun(t_est)
            e = ephem.Ecliptic(sun)
            curr_lon = (e.lon * 180.0 / 3.141592653589793) % 360.0
            diff = (curr_lon - target_sun_lon + 180.0) % 360.0 - 180.0
            if abs(diff) < 1e-6:
                break
            t_est = ephem.Date(t_est - diff / 0.9856)

        dt_des_utc = t_est.datetime().replace(tzinfo=datetime.timezone.utc)
        des_longitudes = calculate_planet_longitudes(dt_des_utc)
        return dt_des_utc, des_longitudes
    else:
        raise RuntimeError("Neither pyswisseph nor ephem is installed.")
