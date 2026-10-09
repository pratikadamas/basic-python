# import requests
#
#
# def find_municipality(latitude, longitude):
#     url = "https://nominatim.openstreetmap.org/reverse"
#
#     params = {
#         "lat": latitude,
#         "lon": longitude,
#         "format": "json",
#         "addressdetails": 1
#     }
#
#     headers = {
#         "User-Agent": "MunicipalityFinder/1.0"
#     }
#
#     response = requests.get(url, params=params, headers=headers, timeout=10)
#     response.raise_for_status()
#
#     data = response.json()
#     address = data.get("address", {})
#
#     municipality = (
#         address.get("municipality")
#         or address.get("city")
#         or address.get("town")
#         or address.get("city_district")
#         or address.get("village")
#     )
#
#     return {
#         "display_name": data.get("display_name"),
#         "municipality": municipality,
#         "city": address.get("city"),
#         "town": address.get("town"),
#         "district": address.get("state_district"),
#         "state": address.get("state"),
#         "country": address.get("country"),
#         "postcode": address.get("postcode")
#     }
#
#
# # Example
# latitude =  22.4639679947799
# longitude = 88.40838964041932
# # 22.4639679947799, 88.40838964041932
#
# result = find_municipality(latitude, longitude)
#
# for key, value in result.items():
#     print(f"{key}: {value}")

# -------------------------------------------------------


# import requests
#
#
# def reverse_geocode(latitude, longitude):
#
#     url = "https://nominatim.openstreetmap.org/reverse"
#
#     params = {
#         "lat": latitude,
#         "lon": longitude,
#         "format": "jsonv2",
#         "addressdetails": 1,
#         "zoom": 18
#     }
#
#     headers = {
#         "User-Agent": "GeoLocationApp/1.0"
#     }
#
#     response = requests.get(
#         url,
#         params=params,
#         headers=headers,
#         timeout=10
#     )
#
#     response.raise_for_status()
#
#     data = response.json()
#     address = data.get("address", {})
#
#     # -----------------------------
#     # Municipality
#     # -----------------------------
#     municipality = (
#         address.get("municipality")
#         or address.get("town")
#         or address.get("city")
#     )
#
#     # Nominatim sometimes returns
#     # "Kolkata Metropolitan Area" as municipality.
#     if municipality == "Kolkata Metropolitan Area":
#         municipality = address.get("town")
#
#     # -----------------------------
#     # Extract location
#     # -----------------------------
#     result = {
#         "latitude": latitude,
#         "longitude": longitude,
#
#         "display_name": data.get("display_name"),
#
#         "locality": (
#             address.get("village")
#             or address.get("suburb")
#             or address.get("neighbourhood")
#         ),
#
#         "municipality": municipality,
#
#         "town": address.get("town"),
#
#         "district": (
#             address.get("state_district")
#             or address.get("county")
#         ),
#
#         "state": address.get("state"),
#
#         "country": address.get("country"),
#
#         "postcode": address.get("postcode")
#     }
#
#     return result
#
#
# # --------------------------------
# # TEST
# # --------------------------------
#
# latitude = 22.4639679947799
# longitude = 88.40838964041932
#
# result = reverse_geocode(latitude, longitude)
#
# for key, value in result.items():
#     print(f"{key}: {value}")



# --------------------------------------------------
