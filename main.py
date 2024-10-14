from tools.get_issues import get_open_issues
from tools.qq_mail_tell import send_email
import time
import datetime
if __name__ == '__main__':
# Test the function
    # send_email('1781591279@qq.com', '教育局教师培训第一期','This is a test email.')

    # 从命令行接受参数变量
    import sys
    to_email='1781591279@qq.com'
    
    today_utc_time= time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
    today_ctc_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()+28800))
    today_time=f'UTC: {today_utc_time} <br> CTC: {today_ctc_time} <br> timestamp: {time.time()}  <br> time_good {datetime.datetime.now()}'

    issues = get_open_issues()
    for index ,issue in enumerate(issues):
        title,url=issue[0],issue[1]
        send_email(to_email, f'今天 {len(issues)} / {index+1} _ '+title, url+'\n\n'+today_time)
        time.sleep(60)


    
