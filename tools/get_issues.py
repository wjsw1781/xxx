import requests
import markdown
import datetime
# 这里优化的点逻辑 看看今天open的issue是否被comment过，如果被comment过，则不展示
def get_open_issues(owner="wjsw1781", repo="xxx", token=None):

    # 如果需要身份验证，可以用token替换None
    token = None  # 或者 'YOUR_PERSONAL_ACCESS_TOKEN'

    # 设置请求头
    headers = {
        "Authorization": f"token {token}" if token else None,
        "Accept": "application/vnd.github.v3+json",
    }

    # GitHub API URL
    url = f"https://api.github.com/repos/{owner}/{repo}/issues?state=open"

    # 发起 GET 请求
    response = requests.get(url, headers=headers)

    # 检查请求是否成功
    if response.status_code != 200:
        print("当前没有任何开放的 Issue。")
        return []
    issues = response.json()
    if not issues:
        print("当前没有任何开放的 Issue。")
        return []
    # 过滤掉今日已经被评论的issue 没有接口 这能全部获取 然后过滤掉
    all_open_issues_with_comments = []
    for issue in issues:
        comments_url = issue['comments_url']
        comments_response = requests.get(comments_url, headers=headers)
        comments = comments_response.json()
        try:
            lastest_comment = comments[-1]['created_at']                      #获取最后一条评论的时间 '2024-10-14T07:52:19Z'
        except Exception as e:
            continue
        today_time=datetime.datetime.now() #获取当前时间
        lastest_comment_time=datetime.datetime.strptime(lastest_comment,'%Y-%m-%dT%H:%M:%SZ')
        if lastest_comment_time.date() != today_time.date():
            all_open_issues_with_comments.append(issue)

    
    print("以下是开放的 Issue:")
    all_issues_md=[]
    for issue in issues:
        print(f"- [{issue['title']}]({issue['html_url']})")
        md_content=f'- [{issue["title"]}]({issue["html_url"]})\n\n'
        html_content = markdown.markdown(md_content)

        all_issues_md.append([issue['title'],html_content])
    return all_issues_md




if __name__ == '__main__':
    get_open_issues()