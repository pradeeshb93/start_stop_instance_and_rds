""" This script is used to start or stop the rds cluser we specify in the program
python start_stop_rds.py start     # To start rds
python start_stop_rds.py stop      # To stop rds
"""


import boto3
import sys
from pprint import pprint
aws_man_con = boto3.session.Session(profile_name ='root',region_name = "us-east-1")

rds = aws_man_con.client('rds')

def status_check():
	status = rds.describe_db_clusters(DBClusterIdentifier='rds clustername')
	return status['DBClusters'][0]['Status']

def start():
	status = status_check()
	if status == "available":
		print("The RDS is already up")
	else:
		try:
			rds.start_db_cluster(DBClusterIdentifier='rds clustername')		
			print("Starting RDS...")
		except:
			print("The cluser is modifying... please try start after sometime")
      
      
def stop():
	status = status_check()
	if status == "stopped":
		print("The RDS is already stopped")
	else:
		try:
			rds.stop_db_cluster(DBClusterIdentifier='rds clustername')
			print("Stopping RDS....")	
		except:
			print("The cluser is modifying.. please try stop after sometime.")
      
      
def main():
	if len(sys.argv) != 2:
		print("Incorrect !! Please run python start_stop_rds.py stop/start")
	elif sys.argv[1] == "start":
		start()
	elif sys.argv[1] == "stop":
		stop()
	else:
		print("please use stop/start keyword ")


if __name__ == "__main__":
	main()
