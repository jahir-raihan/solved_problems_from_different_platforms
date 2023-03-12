import json
s = '{"browsers": {"firefox": {"name": "Firefox","pref_url": "about:config","releases": {"1": {"release_date": "2004-11-09","status": "retired","engine": "Gecko","engine_version": "1.7"}}}}}--{"browsers":{"firefox":{"name":"Firefox","pref_url":"about:config","releases":{"1":{"engine":"Gecko","engine_version":"1.7","release_date":"2004-11-09","status":"retired"}}}}}'
lst = s.split('--')
json1 = json.loads(lst[0])
json2 = json.loads(lst[1])
print('same' if json1 == json2 else 'different')






