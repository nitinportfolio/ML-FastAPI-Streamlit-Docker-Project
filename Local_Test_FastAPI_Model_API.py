import requests
data = {
  "sl_no": 112,
  "ssc_p": 84.0,
  "hsc_p": 90.9,
  "degree_p": 64.5,
  "etest_p": 86.04,
  "mba_p": 59.42,
  "gender": "M",
  "ssc_b": "Others",
  "hsc_b": "Others",
  "hsc_s": "Science",
  "degree_t": "Sci&Tech",
  "workex": "No",
  "specialisation": "Mkt&Fin"
}
response = requests.post("http://127.0.0.1:8000/predict", json=data)
print(response.text)