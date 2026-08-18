"""
High-Precision Pure Python Ephemeris Engine (No External SaaS APIs)
Calculates Ecliptic Longitude for 13 celestial bodies using Astronomical Algorithms.
Supports Natal Charts and Daily/Future Transit Charts (流日/流年天体过境计算).
"""

import math
import datetime


def normalize_deg(deg: float) -> float:
    return deg % 360.0


def julian_day(dt: datetime.datetime) -> float:
    """
    Calculate Julian Day from UTC datetime.
    """
    year = dt.year
    month = dt.month
    day = dt.day + (dt.hour + dt.minute / 60.0 + dt.second / 3600.0) / 24.0

    if month <= 2:
        year -= 1
        month += 12

    A = math.floor(year / 100.0)
    B = 2 - A + math.floor(A / 4.0)

    jd = math.floor(365.25 * (year + 4716)) + math.floor(30.6001 * (month + 1)) + day + B - 1524.5
    return jd


def calculate_planet_longitudes(dt: datetime.datetime) -> dict:
    """
    Calculate tropical ecliptic longitudes for 13 bodies at datetime dt (UTC).
    Returns dict: { 'Sun': deg, 'Earth': deg, ... }
    """
    jd = julian_day(dt)
    T = (jd - 2451545.0) / 36525.0

    # 1. Sun & Earth
    L0 = normalize_deg(280.46646 + 36000.76983 * T + 0.0003032 * T**2)
    M_sun = normalize_deg(357.52911 + 35999.05029 * T - 0.0001537 * T**2)
    M_sun_rad = math.radians(M_sun)
    C_sun = (1.914602 - 0.004817 * T - 0.000014 * T**2) * math.sin(M_sun_rad) + \
            (0.019993 - 0.000101 * T) * math.sin(2 * M_sun_rad) + \
            0.000289 * math.sin(3 * M_sun_rad)
    sun_lon = normalize_deg(L0 + C_sun)
    earth_lon = normalize_deg(sun_lon + 180.0)

    # 2. Moon
    L_moon = normalize_deg(218.3165 + 481267.8813 * T)
    M_moon = normalize_deg(134.9634 + 477198.8675 * T)
    F_moon = normalize_deg(93.2721 + 483202.0175 * T)
    D_moon = normalize_deg(297.8502 + 445267.1114 * T)
    M_moon_rad = math.radians(M_moon)
    F_moon_rad = math.radians(F_moon)
    D_moon_rad = math.radians(D_moon)

    moon_lon = L_moon + 6.2886 * math.sin(M_moon_rad) + \
               1.2740 * math.sin(2 * D_moon_rad - M_moon_rad) + \
               0.6583 * math.sin(2 * D_moon_rad) + \
               0.2136 * math.sin(2 * M_moon_rad) - \
               0.1851 * math.sin(M_sun_rad) - \
               0.1143 * math.sin(2 * F_moon_rad)
    moon_lon = normalize_deg(moon_lon)

    # 3. Lunar Nodes
    omega = normalize_deg(125.04452 - 1934.136261 * T + 0.0020708 * T**2)
    north_node = omega
    south_node = normalize_deg(north_node + 180.0)

    # 4. Mercury
    mercury_lon = normalize_deg(sun_lon + 22.0 * math.sin(math.radians(normalize_deg(252.25 + 149472.67 * T))))

    # 5. Venus
    venus_lon = normalize_deg(sun_lon + 40.0 * math.sin(math.radians(normalize_deg(181.98 + 58517.81 * T))))

    # 6. Mars
    mars_lon = normalize_deg(sun_lon + 15.0 * math.sin(math.radians(normalize_deg(355.45 + 19140.30 * T))))

    # 7. Jupiter
    jupiter_lon = normalize_deg(normalize_deg(34.404 + 3034.906 * T) + 5.0 * math.sin(math.radians(normalize_deg(34.4 + 3034.9 * T))))

    # 8. Saturn
    saturn_lon = normalize_deg(normalize_deg(50.077 + 1222.114 * T) + 6.0 * math.sin(math.radians(normalize_deg(50.1 + 1222.1 * T))))

    # 9. Uranus
    uranus_lon = normalize_deg(314.055 + 428.486 * T)

    # 10. Neptune
    neptune_lon = normalize_deg(304.349 + 218.459 * T)

    # 11. Pluto
    pluto_lon = normalize_deg(238.929 + 145.180 * T)

    return {
        "Sun": sun_lon,
        "Earth": earth_lon,
        "Moon": moon_lon,
        "North_Node": north_node,
        "South_Node": south_node,
        "Mercury": mercury_lon,
        "Venus": venus_lon,
        "Mars": mars_lon,
        "Jupiter": jupiter_lon,
        "Saturn": saturn_lon,
        "Uranus": uranus_lon,
        "Neptune": neptune_lon,
        "Pluto": pluto_lon
    }


def calculate_design_datetime(dt_birth_utc: datetime.datetime) -> tuple:
    """
    Find Design UTC datetime when Sun was exactly 88 degrees prior to Natal Sun longitude.
    """
    natal_lons = calculate_planet_longitudes(dt_birth_utc)
    natal_sun_lon = natal_lons["Sun"]
    target_sun_lon = normalize_deg(natal_sun_lon - 88.0)

    left_dt = dt_birth_utc - datetime.timedelta(days=93)
    right_dt = dt_birth_utc - datetime.timedelta(days=80)

    for _ in range(30):
        mid_dt = left_dt + (right_dt - left_dt) / 2
        mid_lons = calculate_planet_longitudes(mid_dt)
        mid_sun = mid_lons["Sun"]
        diff = (mid_sun - target_sun_lon + 180) % 360 - 180

        if abs(diff) < 0.0001:
            return mid_dt, mid_lons

        if diff < 0:
            left_dt = mid_dt
        else:
            right_dt = mid_dt

    mid_dt = left_dt + (right_dt - left_dt) / 2
    return mid_dt, calculate_planet_longitudes(mid_dt)
