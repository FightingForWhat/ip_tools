# -*- coding: utf-8 -*-
# !/usr/bin/ python
# @Time    : 2021-03-23
# @Author  : 
# @FileName: ip_tools.py

import requests
import random
import re



def headers_use(headers_use):
    user_agent = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3100.0 Safari/537.36',
        'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
        'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
        'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0',
        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)',
        'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)',
        'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
        'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
        'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11',
        'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
        'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)',
        'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)',
        'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
        'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)',
        'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)',
        'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)',
        'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser)',
        'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
    ]
    user_agent_use = user_agent[random.randint(0, len(user_agent)-1)]
    headers_use={
        'User-Agent': user_agent_use
    }

    return headers_use


def ip_check():

    look_up_ip_input = input('输入要查询的ip: ')
    if '://' in look_up_ip_input:
        look_up_ip_check = look_up_ip_input.split('://')[1]
    elif ':' in look_up_ip_check:
        look_up_ip_check = look_up_ip_check.split(':')[0]
    elif '/' in look_up_ip_check:
        look_up_ip_check = look_up_ip_check.split('/')[0]
    else:
        print('ip格式出现错误，请更正')

    look_up_ip = look_up_ip_check
    # print(look_up_ip)
    return look_up_ip

def look_up():

    look_up_ip = ip_check()

    data_post = 'ip=' + look_up_ip
    # url = 'http://ip.tool.chinaz.com/' + str(look_up_ip)
    headers = headers_use(headers_use)
    ip_look_up = requests.post('http://ip.tool.chinaz.com/' + look_up_ip, headers=headers, data=data_post)
    respon_look_up = ip_look_up.text

    # print(ip_look_up.status_code)
    # print(ip_look_up.apparent_encoding)

    reg = 'w30-0.lh24.tl.ml80.*<p>(.{1,30})</p>.*<em>(.{1,30})</em><a.class=.*>(.{1,30})提供</a>'
    find_words = re.search(reg, respon_look_up, re.S)
    print()
    if ip_look_up.status_code == 200:
        result_ip_look_up = find_words.group(1) + ' ' + find_words.group(2) + ' ' + find_words.group(3) + '提供'
        print(result_ip_look_up + '\n')
    else:
        print('查询出错' + '\n')
    return

def ips_check():

    ips_path = input('请输入源文件路径和文件名（默认为当前路径下urls.txt文件）：') or './urls.txt'
    ips_source = open(ips_path, 'r')
    ips_list = ips_source.readlines()
    ips_count = len(ips_list)
    ips_source.close()
    # print(ips_count)

    print()

    i = 1
    doc_result_write = open('ip_check_result.txt', 'a+')
    for look_up_ip_input in ips_list:
        look_up_ip_input = look_up_ip_input.strip('\n').strip(' ')
        if '://' in look_up_ip_input:
            look_up_ip_check = look_up_ip_input.split('://')[1]
        elif ':' in look_up_ip_check:
            look_up_ip_check = look_up_ip_check.split(':')[0]
        elif '/' in look_up_ip_check:
            look_up_ip_check = look_up_ip_check.split('/')[0]
        else:
            print('ip格式出现错误，请更正')
            continue
        look_up_ip = look_up_ip_check
        data_post = 'ip=' + look_up_ip
        # url = 'http://ip.tool.chinaz.com/' + str(look_up_ip)
        headers = headers_use(headers_use)
        ip_look_up = requests.post('http://ip.tool.chinaz.com/' + look_up_ip, headers=headers, data=data_post)
        respon_look_up = ip_look_up.text

        # print(ip_look_up.status_code)
        # print(ip_look_up.apparent_encoding)

        reg = 'w30-0.lh24.tl.ml80.*<p>(.{1,30})</p>.*<em>(.{1,30})</em><a.class=.*>(.{1,30})提供</a>'
        find_words = re.search(reg, respon_look_up, re.S)

        look_up_progress = '       ---[' + str(i) + '/' + str(ips_count) + ']'
        ip_info = '[*] 查询 ' + look_up_ip_input

        if ip_look_up.status_code == 200:
            try:
                result_ip_look_up = '[+] ' + find_words.group(1) + ' ' + find_words.group(2) + ' ' + find_words.group(3) + '提供' + look_up_progress
                print(ip_info + '\n' + result_ip_look_up)
            except Exception as error:
                result_ip_look_up = '[!] 爬取数据发生错误 ' + str(error.args).replace('(\"', '[').replace('\",)', ']') + look_up_progress
                print(ip_info + '\n' + result_ip_look_up)
                i += 1
                continue
        else:
            result_ip_look_up = '[!] 返回状态异常，查询出错!!!' + look_up_progress
            print(ip_info + '\n' + result_ip_look_up)
            i += 1
            continue
        doc_result_write.write(ip_info + '\n' + result_ip_look_up + '\n')

        i += 1

    doc_result_write.close()
    print()
    return




def logo():

    print('''
        .__                              _____.__        
        |__|_____     ____  ____   _____/ ____\__| ____  
        |  \____ \  _/ ___\/  _ \ /    \   __\|  |/ ___\ 
        |  |  |_> > \  \__(  <_> )   |  \  |  |  / /_/  >
        |__|   __/   \___  >____/|___|  /__|  |__\___  / 
           |__|          \/           \/        /_____/  
       
    ''')

def main():

    print('''
    [*] 选择要使用的功能(输入相应的编号)：
    
    1. 查找单个ip或域名信息
    2. 批量查找ip或域名信息
    3. 退出
    ''')

    choice_option = input('    >>>')
    if choice_option == '1':
        logo()
        look_up()

    elif choice_option == '2':
        logo()
        ips_check()

    elif choice_option == '3':
        print()
        exit()
    else:
        print()
        exit()

    return

if __name__ == '__main__':
    logo()
    main()
