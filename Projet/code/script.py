import psycopg2
import csv
import os
import time
def main():
    connection = psycopg2.connect("host=localhost dbname=postgres user=postgres")
    cur = connection.cursor()
    #open kpis folder and read all csv Files
    requests_time = []
    for file in os.listdir("kpis"):
        if file.endswith(".csv"):
            with open("kpis/"+file
            ) as csvfile:
                reader = csv.reader(csvfile, delimiter=',')
                
                for row in reader:
                    print(row)
                    try:
                        row = row[0].split(';')
                        #workflow_id,workflow_name,workflow_started,workflow_finished,workflow_elapsed_time,workflow_status
                        started =time.time()
                        cur.execute("INSERT INTO workflowskpi(workflow_id,workflow_name,workflow_started,workflow_finished,workflow_elapsed_time,workflow_status) VALUES (%s,%s,%s,%s,%s,%s)",(row[0],row[1],row[2],row[3],row[4],row[5]))
                        requests_time.append(time.time()-started)
                    except Exception as e:
                        print(e)
                        pass
    connection.commit()
    print("Average time for insert: ",sum(requests_time)/len(requests_time))
    

start_time = time.time()
main()
print("--- %s seconds ---" % (time.time() - start_time))