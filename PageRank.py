import sys
from operator import add
import re
from pyspark import SparkContext

def line_parser(row):
    title_page = row[row.find("<title>")+7:row.find("</title>")]
    inner_text = row[row.find("<text"):row.find("</text>")]
    outlinks = re.findall("\\[\\[(.*?)\\]\\]", inner_text)
    ret_outlinks = []
    for item in outlinks:
        a,b = item.split("|")
        ret_outlinks.append(a)
    return title_page, ret_outlinks


if __name__ == "__main__":

    if len(sys.argv) != 4:
        print("Follow this sample: <Iteration> <Alpha> <Input Path> <Output Path>")
        sys.exit(-1)
    sc = SparkContext("local", "PageRank")
    iteration = int(sys.argv[1])
    alpha = float(sys.argv[2])
    input_path = sys.argv[3]
    output_path = sys.argv[4]

    input_data = sc.textFile(input_path).cache()
    total_node = input_data.count()
    rows = input_data.map(lambda row: line_parser(row))
    rows.collect()