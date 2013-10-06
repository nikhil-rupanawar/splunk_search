"""
An example to create a search query to splunk and print result set
Requirements: splunk SDK for python
"""
import splunklib.client as client  
import splunklib.results as results
HOST = "localhost"
PORT = 8089
USERNAME = "admin"
PASSWORD = "changeme"

# Create a Service instance and log in
service = client.connect(
    host=HOST,
    port=PORT,
    username=USERNAME,
    password=PASSWORD)

# Print installed apps to the console to verify login
for app in service.apps:
    print app.name
#search events, logs
kwargs_normalsearch = {"exec_mode": "normal"} #specify mode 'normal, blocking etc
#search for 500 Internal server error, with source type and specific url
searchquery_normal = 'search sourcetype=access_combined_wcookie "/flower_store/category.screen"  host="nik-PC" 500' 
job = service.jobs.create(searchquery_normal, **kwargs_normalsearch)
print "Search job properties"
print "Search job ID:        ", job["sid"]
print "The number of events: ", job["eventCount"]
print "The number of results:", job["resultCount"]
print "Search duration:      ", job["runDuration"], "seconds"
print "This job expires in:  ", job["ttl"], "seconds"
for result in results.ResultsReader(job.results()):
    print result
