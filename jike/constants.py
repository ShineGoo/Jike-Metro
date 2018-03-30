# -*- coding: utf-8 -*-

"""
This module provides constants for Jike.
"""

from string import Template
import os.path as osp

JIKE_URI_SCHEME_FMT = 'jike://page.jk/web?url=https%3A%2F%2Fruguoapp.com%2Faccount%2Fscan%3Fuuid%3D{uuid}&displayHeader=false&displayFooter=false'

AUTH_TOKEN_STORE_PATH = osp.join(osp.dirname(__file__), 'metro.json')

STREAM_CAPACITY_LIMIT = 1000

RENDER2BROWSER_HTML_TEMPLATE = Template("""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Jike Metro</title>
    <style type="text/css">
        .container {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: space-around;
        }

        .header {
            font-size: 40px;
            margin: 50px auto;
        }

        .footer {
            font-size: 16px;
            margin: 100px auto;
        }

        .footer_line {
            margin: 10px auto;
        }
    </style>
</head>
<body>
<div class="container">
    <div class="header">Scan for Ⓙ 🚇 🎟️</div>
    ${qrcode_svg}
    <div class="footer container">
        <div class="footer_line">🚧 with 🐈 by 👷 <a href="https://web.okjike.com/user/WalleMax/" target="_blank">挖地道的</a></div>
        <div class="footer_line">GitHub: <a href="https://github.com/Sorosliu1029/Jike-Metro" target="_blank">Jike Metro</a></div>
        <div class="footer_line"><strong>Reviews</strong>, <strong>Feedbacks</strong> and <strong>Contributions</strong> are warmly welcome.</div>
    </div>
</div>
</body>
</html>
""")

HEADERS = {
    'Origin': 'http://web.okjike.com',
    'Referer': 'http://web.okjike.com',
    # TODO change User-Agent to 'Jike Metro' once published
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
    'Accept': 'application/json',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',

    'x-jike-app-auth-jwt': None,
    'App-Version': '4.1.0',
    'DNT': '1',
    'platform': 'web',
}

_f_ = {
    '_s_': 'https',
    '_d_': 'app.jike.ruguoapp.com',
    '_v_': '1.0'
}
ENDPOINTS = {
    'create_session': '{_s_}://{_d_}/sessions.create'.format(**_f_),
    'wait_login': '{_s_}://{_d_}/sessions.wait_for_login'.format(**_f_),
    'confirm_login': '{_s_}://{_d_}/sessions.wait_for_confirmation'.format(**_f_),

    'my_collections': '{_s_}://{_d_}/{_v_}/users/collections/list'.format(**_f_),

    'news_feed': '{_s_}://{_d_}/{_v_}/newsFeed/list'.format(**_f_),
    'news_feed_unread_count': '{_s_}://{_d_}//{_v_}/newsFeed/countUnreads'.format(**_f_),
    'following_update': '{_s_}://{_d_}/{_v_}/personalUpdate/followingUpdates'.format(**_f_),

    'user_profile': '{_s_}://{_d_}/{_v_}/users/profile'.format(**_f_),
    'user_post': '{_s_}://{_d_}/{_v_}/personalUpdate/single'.format(**_f_),
    'user_created_topic': '{_s_}://{_d_}/{_v_}/customTopics/custom/listCreated'.format(**_f_),
    'user_subscribed_topic': '{_s_}://{_d_}/{_v_}/users/topics/listSubscribed'.format(**_f_),
    'user_following': '{_s_}://{_d_}/{_v_}/userRelation/getFollowingList'.format(**_f_),
    'user_follower': '{_s_}://{_d_}/{_v_}/userRelation/getFollowerList'.format(**_f_),

    'comment': '{_s_}://{_d_}/{_v_}/comments/listPrimary'.format(**_f_),
    'topic_selected': '{_s_}://{_d_}/{_v_}/messages/history'.format(**_f_),
    'topic_square': '{_s_}://{_d_}/{_v_}/squarePosts/list'.format(**_f_),
}

PUBLIC_FIELDS = [
    # item meta info
    'id',
    'createdAt',
    'content',
    'pictures',
    'status',
    'topic',
    'linkInfo',
    'target',
    'targetType',
    'type',
    'user',
    'isCommentForbidden',
    'viewType',
    # item interaction info
    'likeCount',
    'likeIcon',
    'likeInfo',
    'commentCount',
    'repostCount',
    # item personal info
    'read',
    'liked',
    'collected',
    'collectedTime',
    'collectTime',  # seems to be Jike typo
]
