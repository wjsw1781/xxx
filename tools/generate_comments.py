import requests

cookies = {
    '_octo': 'GH1.1.1262829699.1728367576',
    '_device_id': '1695e4c5a252184f22e3e6909449e322',
    'saved_user_sessions': '28215744%3AJYy3jFeQo19RlmGR45KnpKNSihJT2DS3XfCWUuDhsCObGb5a',
    'user_session': 'JYy3jFeQo19RlmGR45KnpKNSihJT2DS3XfCWUuDhsCObGb5a',
    '__Host-user_session_same_site': 'JYy3jFeQo19RlmGR45KnpKNSihJT2DS3XfCWUuDhsCObGb5a',
    'logged_in': 'yes',
    'dotcom_user': 'wjsw1781',
    'color_mode': '%7B%22color_mode%22%3A%22auto%22%2C%22light_theme%22%3A%7B%22name%22%3A%22light%22%2C%22color_mode%22%3A%22light%22%7D%2C%22dark_theme%22%3A%7B%22name%22%3A%22dark%22%2C%22color_mode%22%3A%22dark%22%7D%7D',
    'preferred_color_mode': 'light',
    'tz': 'Asia%2FShanghai',
    '_gh_sess': 'dWTz8Ob9hLJ1oPLtji6RDGtI%2F3yc7f8106kJTUIQYKx7hWVBeYeu64AVeYyexUED6rSNJuXLYkiWkSRFMiGdlJoPLoidLBIhmZfXWQzg0r9C%2BR84gng6yfo09SpDEeVOO8cUv07TBI3jj0hGtzieK0EPf8M7fvzm8ZyR64b%2F11cdY6h6duEbG4a7zEL%2BXxyQFYNoQ1L0wVWU2UXp6jqM31fPvvvPUfrpbTRyKJmwziQxTaNap6OxOQmcnWSTyKza7nYQ9E2ll0opChsNtfe2Na4XBmz9MlsWfseNrswJlA4CvR64YAlSWX7f2BFACTY067e2DlEvocScvgBPBaWS4Usv6ucZ2kiafktgTnCzqJAdrV4FN0opb8PLXyI8yL0k3BSeVVDkYjfkup322RRa7UgOrVtElmK9Xt8B9b62YSudU91DhKQsMO6oxnFkISC7X6Z1Kur7RyX8rDmmMDtMDO7%2Bgt72riyYGCsmMA%3D%3D--cIf9I%2BEFRWnknkg%2F--WGHUAe6gCWUye9I0hkcAxQ%3D%3D',
}

headers = {
    'accept': 'application/json',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'cache-control': 'no-cache',
    'content-type': 'multipart/form-data; boundary=----WebKitFormBoundarydBc8A9vBQ69rUIp6',
    # 'cookie': '_octo=GH1.1.1262829699.1728367576; _device_id=1695e4c5a252184f22e3e6909449e322; saved_user_sessions=28215744%3AJYy3jFeQo19RlmGR45KnpKNSihJT2DS3XfCWUuDhsCObGb5a; user_session=JYy3jFeQo19RlmGR45KnpKNSihJT2DS3XfCWUuDhsCObGb5a; __Host-user_session_same_site=JYy3jFeQo19RlmGR45KnpKNSihJT2DS3XfCWUuDhsCObGb5a; logged_in=yes; dotcom_user=wjsw1781; color_mode=%7B%22color_mode%22%3A%22auto%22%2C%22light_theme%22%3A%7B%22name%22%3A%22light%22%2C%22color_mode%22%3A%22light%22%7D%2C%22dark_theme%22%3A%7B%22name%22%3A%22dark%22%2C%22color_mode%22%3A%22dark%22%7D%7D; preferred_color_mode=light; tz=Asia%2FShanghai; _gh_sess=dWTz8Ob9hLJ1oPLtji6RDGtI%2F3yc7f8106kJTUIQYKx7hWVBeYeu64AVeYyexUED6rSNJuXLYkiWkSRFMiGdlJoPLoidLBIhmZfXWQzg0r9C%2BR84gng6yfo09SpDEeVOO8cUv07TBI3jj0hGtzieK0EPf8M7fvzm8ZyR64b%2F11cdY6h6duEbG4a7zEL%2BXxyQFYNoQ1L0wVWU2UXp6jqM31fPvvvPUfrpbTRyKJmwziQxTaNap6OxOQmcnWSTyKza7nYQ9E2ll0opChsNtfe2Na4XBmz9MlsWfseNrswJlA4CvR64YAlSWX7f2BFACTY067e2DlEvocScvgBPBaWS4Usv6ucZ2kiafktgTnCzqJAdrV4FN0opb8PLXyI8yL0k3BSeVVDkYjfkup322RRa7UgOrVtElmK9Xt8B9b62YSudU91DhKQsMO6oxnFkISC7X6Z1Kur7RyX8rDmmMDtMDO7%2Bgt72riyYGCsmMA%3D%3D--cIf9I%2BEFRWnknkg%2F--WGHUAe6gCWUye9I0hkcAxQ%3D%3D',
    'origin': 'https://github.com',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://github.com/wjsw1781/xxx/issues/5',
    'sec-ch-ua': '"Microsoft Edge";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0',
    'x-requested-with': 'XMLHttpRequest',
    'x-timeline-last-modified': '2024-10-14T07:52:19.000000000Z',
}

files = {
    'authenticity_token': (None, 'B7icAuMubZCuyGK40TbgkYELTJqNBnIh-mwt8XfVQwLzJCkk-x6xP2uNWXEqliKZF-TcU2v-NlHbHpnwnN213A'),
    'required_field_cc12': (None, ''),
    'timestamp': (None, '1728892276972'),
    'timestamp_secret': (None, '44d244871a213953d8d434d2e4cd6f046d2e10aca2a44c3f4b325bd5b98ac42b'),
    'issue': (None, '5'),
    'saved-reply-filter-field': (None, ''),
    'saved_reply_id': (None, ''),
    'comment[body]': (None, '\n测试评论是否存在body冲突3\n\n'),
    'path': (None, ''),
    'line': (None, ''),
    'start_line': (None, ''),
    'preview_side': (None, ''),
    'preview_start_side': (None, ''),
    'start_commit_oid': (None, ''),
    'end_commit_oid': (None, ''),
    'base_commit_oid': (None, ''),
    'comment_id': (None, ''),
    'state_reason': (None, 'completed'),
}
for i in range(5,1000):
    files['comment[body]'] = (None, f'\n测试评论是否存在body冲突{i}\n\n')
    response = requests.post('https://github.com/wjsw1781/xxx/issue_comments', cookies=cookies, headers=headers, files=files)

    print(response.status_code,i)

    