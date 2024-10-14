from tools.get_issues import get_open_issues
from tools.qq_mail_tell import send_email
import time

if __name__ == '__main__':
# Test the function
    # send_email('1781591279@qq.com', '教育局教师培训第一期','This is a test email.')

    # 从命令行接受参数变量
    import sys
    if len(sys.argv) != 4:
        print("Usage: python qqmail_tell.py <to_email> <title> <content>")
        sys.exit(1)
    to_email = sys.argv[1]
    title = sys.argv[2]
    content = sys.argv[3]
    if '算法学习方面' not in title:
        sys.exit(0)


    issues = get_open_issues()
    for index ,issue in enumerate(issues):
        title,url=issue[0],issue[1]
        send_email(to_email, f'今天 {len(issues)} / {index+1} _ '+title, url)
        time.sleep(60)


    
