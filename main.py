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
    current_goode_time=datetime.datetime.now()
    current_hour=current_goode_time.hour
    current_hour_sh=current_hour+8
    pre_hour=current_hour-8
    if current_hour_sh<10 or current_hour_sh>22:
        print(f'current_hour_sh {current_hour_sh} current_hour {current_hour} 不在发送时间  太早或者太晚  都会打扰我  所以不发送')
        sys.exit(0)

    today_time=f'UTC: {today_utc_time} <br> CTC: {today_ctc_time} <br> timestamp: {time.time()}  <br> time_good {current_goode_time}'
    issues = get_open_issues()
    for index ,issue in enumerate(issues):
        title,url=issue[0],issue[1]
        send_email(to_email, f'今天 {len(issues)} / {index+1} _ '+title, url+'\n\n'+today_time)
        time.sleep(60)
    


    
