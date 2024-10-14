import requests


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
    if response.status_code == 200:
        issues = response.json()
        if not issues:
            print("当前没有任何开放的 Issue。")
            return []
        else:
            print("以下是开放的 Issue:")
            all_issues_md=[]
            for issue in issues:
                # 打印标题和链接
                print(f"- [{issue['title']}]({issue['html_url']})")
                md_content=f'- [{issue["title"]}]({issue["html_url"]})\n\n'
                all_issues_md.append([issue['title'],md_content])
            return all_issues_md
    else:
        print(f"请求失败: {response.status_code}, {response.text}")
        return [['请求失败', '请求失败']]
