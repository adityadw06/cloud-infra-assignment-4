# cloud-infra-assignment-4

* mapper.py code - temperature_mapper.py
* reducer.py code - temperature_reducer.py
* Screenshots of the execution of Hadoop MapReduce Job in the terminal - map_reduce_execution_1 to map_reduce_execution_4 (contains final completed successfully result)
* Merged Output file - Temperature_Merged_Result

## Commands Used
* gsutil cp -r gs://dataproc-staging-us-central1-<my-bucket-id>-tpkv5trg/HW-4/ .

* hadoop fs -put data/ /tempData

* hadoop jar /usr/lib/hadoop/hadoop-streaming.jar \
-files temperature_mapper.py,temperature_reducer.py \
-input /tempData/* \
-output /TemperatureOutputFolder \
-mapper 'python temperature_mapper.py' \
-combiner 'python temperature_reducer.py' \
-reducer 'python temperature_reducer.py'

* hadoop fs -getmerge /TemperatureOutputFolder Temperature_Merged_Result

* gsutil cp Temperature_Merged_Result gs://dataproc-staging-us-central1-<my-bucket-id>-tpkv5trg/

## Additional things
* misc_screenshots - Contains screenshots of each of the steps performed
* references - mapper code picked up from lecture materials and then modified, reducer code used as it is from lecture materials