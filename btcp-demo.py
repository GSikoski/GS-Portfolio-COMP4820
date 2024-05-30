# This code can't be run because it lacks the required proprietary modules.
# This code is primarily to see how data is generated on a user level.
# To see the data generation process, watch the btcp-demonstration video
# You can also refer to the attached diagram to help better grasp the code

def main():

    # Generate a class of the cyber challenge type
    cc = openAI_NT_Gen.CyberChallenge(log_path="BTCP_E2E.log",
                                    pcap_path="BTCP_E2E.pcap",
                                    malicious_ip= "237.234.234.196",
                                    time_start = datetime.datetime(2024,3,1,10,0,46), 
                                    time_end = datetime.datetime(2024,3,1,10,15,14)
                                    )
    
    # Set Challenge Values
    cc.set_ips(["247.161.168.45",
                "203.197.54.192",
                "203.167.31.239",
                "158.196.119.15",
                "220.32.157.154",
                "179.93.224.88",
                "164.112.184.203",
                "254.32.211.136",
                "68.82.123.101",
                "221.30.187.73",
                "57.254.150.118"
                "237.87.11.162"
                "91.62.89.161"
                "93.252.110.29"
                "242.146.146.128"
                "29.91.49.248"
                "106.164.123.62"
                "119.235.184.174"
                "105.221.166.79",
                "237.234.234.196"])
    
    cc.set_links([
        "https://www.test.com/"
        "https://www.test.com/about"
        "https://www.test.com/contact"
        "https://www.test.com/products"
        "https://www.test.com/services"
        "https://www.test.com/blog"
        "https://www.test.com/blog/post1"
        "https://www.test.com/blog/post2"
        "https://www.test.com/gallery"
        "https://www.test.com/gallery/photo1"
        "https://www.test.com/gallery/photo2"
        "https://www.test.com/news"
        "https://www.test.com/news/article1"
        "https://www.test.com/news/article2"
        "https://www.test.com/faq"
        ])

    # # Generate Regular Data
    for _ in range(15):
        cc.make_log_class()
        cc.make_pcap_class()

        try:
            new_logs = cc.gen_logs(8)
            log_insert(cc.log_path, new_logs)
        except Exception as e:
            print("Failed a log generation, error: ", e)

        count = 0
        while count < 3:
            try:
                new_pcap = cc.gen_pcap(8, False)
                pcap_insert(cc.pcap_path, new_pcap)
                break
            except Exception as e:
                print("Failed a pcap generation, error: ", e)
                count+=1

        
        

        cc.time_start = cc.time_start + datetime.timedelta(minutes=15)
        cc.time_end = cc.time_end + datetime.timedelta(minutes=15)

    
    # Generate Malicious Log Entries
    cc.time_start = cc.time_start = datetime.datetime(2024,3,1,12,0,20)
    cc.time_end = cc.time_end = datetime.datetime(2024,3,1,12,3,40)

    cc.make_log_class()
    
    try:
        mal_logs = cc.gen_logs(5, "ddos")
        log_insert(cc.log_path, mal_logs)
    except Exception as e:
        print("Failed malicious log entry generation: ", e)

    cc.time_start = cc.time_start + datetime.timedelta(minutes=46, seconds= 24)
    cc.time_end = cc.time_end + datetime.timedelta(minutes=46, seconds= 24)

    cc.make_log_class()

    try:
        mal_logs = cc.gen_logs(7, "ddos")
        log_insert(cc.log_path, mal_logs)
    except Exception as e:
        print("Failed malicious log entry generation: ", e)

    # Generate Malicious Pcap Entries
    cc.time_start = cc.time_start = datetime.datetime(2024,3,1,12,0,20)
    cc.time_end = cc.time_end = datetime.datetime(2024,3,1,12,3,40)

    cc.make_pcap_class()

    count = 0
    while count < 3:
        try:
            mal_pcap = cc.gen_pcap(5, True)
            pcap_insert_time(cc.pcap_path, mal_pcap)
            break
        except Exception as e:
            print("Failed malicious log entry generation: ", e)
            count += 1

    cc.time_start = cc.time_start + datetime.timedelta(minutes=46, seconds= 24)
    cc.time_end = cc.time_end + datetime.timedelta(minutes=46, seconds= 24)

    cc.make_pcap_class()

    count = 0
    while count < 3:
        try:
            mal_pcap = cc.gen_pcap(5, True)
            pcap_insert_time(cc.pcap_path, mal_pcap)
            break
        except Exception as e:
            print("Failed malicious log entry generation: ", e)
            count += 1
