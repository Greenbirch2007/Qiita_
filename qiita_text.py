#! -*- utf-8 -*-
import copy
import re
import json
import time
from lxml import etree
from selenium import webdriver
import csv
driver = webdriver.Chrome()




def use_selenium_headless_getdt(url):
    driver.get(url)
    time.sleep(1)
    html = driver.page_source
    return html





def list_null(list_content):
    if list_content !=[]:
        result = list_content
    else:
        result = ["null"]
    return result



def writeinto_jsonfile(filename,list_data):
    with open(filename, 'w', encoding='utf-8') as fw:
        json.dump(list_data, fw, indent=4, ensure_ascii=False)


def writeintoTSV_file(filename,data):
    with open(filename,'a', newline='\n', encoding="utf-8") as f_output:
        tsv_output = csv.writer(f_output, delimiter='\t')
        tsv_output.writerow(data)

if __name__=="__main__":
    page_MAx = 101
    keyword_list = ["Python","C","Java","C#","JavaScript","Ruby","SQL","PHP","Go","Golang","VBA","shell","html","css","外部設計","内部設計","試験","手順書","リリース","運用","保守","システム","マネージメント","mysql","mariadb","oracle","redis","Django","Flask","unittest","requests","selenium","gin","正規表現","GORM","echo","pandas","scrapy","sqlchemy","threading","multiprocessing","docker","linux","centos","windows","AWS","cloud","k8s","JSON","pycharm","git","API","apache","restful","要件定義書","基本設計書","詳細設計書","テスト仕様書","仕様書","設計書","単体テスト","結合テスト","要件定義","基本設計","詳細設計","テスト","単体テスト","結合テスト","VNF","tableau"]
    for item_page in range(page_MAx):
        for item_keyword in keyword_list:
            try:


                url = "https://qiita.com/search?page={0}&q={1}".format(item_page,item_keyword)
                html = use_selenium_headless_getdt(url)
                pattern = re.compile('class="searchResult_itemTitle">(.*?)</a>',re.S)
                title = re.findall(pattern,html)
                selector = etree.HTML(html)
                title_url = selector.xpath('//*[@id="main"]/div/div[1]/div/div[2]/h1/a/@href')
                # time.sleep(40)

                for i1,i2 in zip(title,title_url):
                    f_title ="".join(i1.split("<em>")[1].split("</em>"))
                    f_title_url = "https://qiita.com"+i2
                    print(f_title,f_title_url)
                    writeintoTSV_file("{0}.tsv".format(item_keyword), [f_title,f_title_url])
            except:
                pass















