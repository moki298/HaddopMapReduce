# project3 Hadoop MapReduce Analysis - Books Set

The data set used in this project is available at openlibrary.org.
The data will be analyzed using Hadoop.

Dump location: http://openlibrary.org/data/ol_dump_works_latest.txt.gz

## The instructions for using this code on hadoop server that supports HadoopStreamingAPI are given below

As it has huge data we are going to analyse it using hadoop streaming API

Go to home directory

Intially, clone the files in this repository.

Once the repository is cloned, execute the below command on hadoop cluster, by changing the output path in the command

hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.7.1.jar -input /data/openlibrary/ol_dump_works_latest-20161202.txt -output /users-cloud-16fs/ballima/project3-out/output2 -mapper ~/project3/mapper.py -reducer ~/project3/reducer.py -file ~/project3/{mapper,reducer}.py

##Output

Once the job execution is complete the output can be seen in hdfs using below commad

hdfs dfs -cat /users-cloud-16fs/ballima/project3-out/output2/part-00000
