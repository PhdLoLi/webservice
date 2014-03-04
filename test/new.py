import impala 
client = impala.ImpalaBeeswaxClient('master:21000') 
client.connect() 
results = client.execute(query)
