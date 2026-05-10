from pyspark.sql import SparkSession
import sys

def read_json(schema_path,data_path,resultpath):
    #"D:\\Hadoop_iquiz\\jsonfiles\\batch30\\schema_batch44.json"
    #"D:\\Hadoop_iquiz\\jsonfiles\\batch30\\emp5.json"
    #D:\\Hadoop_iquiz\\jsonfiles\\btach44\\result
    spark=SparkSession.builder.appName("pyspark json data ").getOrCreate()

    read_schema = spark.read.json(schema_path).schema
    read_jon_df=spark.read.schema(read_schema).json(data_path)
    expr="""events.client,
    events.beaconType,
    events.beaconVersion,
    events.data.displayAd.instanceID,
    events.data.displayAd.inView,
    events.data.milestones.amazonA9Requested,
    events.data.milestones.indexExchangeReceived,
    events.data.milestones.adRequested,
    events.data.milestones.amazonA9BidsRequested""".split(",")

    flattendf=read_jon_df.selectExpr(expr)
    df=flattendf.where("client !='NULL'")
    df.createTempView("emp")
    df2=spark.sql("select client,beaconType,count(*) as count from emp group by client,beaconType ")
    df2.show()
    df2.coalesce(1).write.mode("overWrite").format("csv").option("header",True).save(resultpath)
if __name__ == '__main__':
    print("we are in main program")

    schema_path=sys.argv[1]
    data_path=sys.argv[2]
    resultpath=sys.argv[3]

    print("schema",schema_path)
    print("data", data_path)
    print("res", resultpath)

    read_json(schema_path,data_path,resultpath)

