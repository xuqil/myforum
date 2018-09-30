from string import ascii_letters, digits
import random
from random import randint


def generate_codef():
    """生成六位数随机验证码"""
    code = "".join(random.sample(ascii_letters + digits, 6))
    return code


def get_random_color():
    return (randint(0, 255), randint(0, 255), randint(0, 255))


def transform_list(comment_list):
    comment_dict = {}
    for d in comment_list:
        d['add_time']= str(d['add_time'])[:19]
        id = d.get('nid')
        d['children_contents']= []
        comment_dict[id] = d

    for k in comment_dict:
        parent_id = comment_dict[k]['parent_id_id']
        if parent_id:
            comment_dict[parent_id]['children_contents'].append(comment_dict[k])

    res_list = []
    for i in comment_dict:
        if not comment_dict[i]['parent_id_id']:
            res_list.append(comment_dict[i])
    return res_list


html = ''
comment_list = [
        {'nid': 1, 'content': '                         asdasd   ', 'user_id': 2, 'parent_id_id': None,
         'children_contents': [
             {'nid': 2, 'content': '你好', 'user_id': 2, 'parent_id_id': 1, 'children_contents': [
                 {'nid': 8, 'content': '阿萨德', 'user_id': 2, 'parent_id_id': 2, 'children_contents': []}]},
             {'nid': 7, 'content': '啊实打实', 'user_id': 2, 'parent_id_id': 1, 'children_contents': []}]},

        {'nid': 9, 'content': '啊实打实', 'user_id': 2, 'parent_id_id': None, 'children_contents': [
            {'nid': 10, 'content': '真的假的', 'user_id': 2, 'parent_id_id': 9, 'children_contents': []}]},
        {'nid': 32, 'content': '写的很好', 'user_id': 2, 'parent_id_id': None, 'children_contents': [
            {'nid': 39, 'content': '确实如此', 'user_id': 3, 'parent_id_id': 32, 'children_contents': []}]},

        {'nid': 38, 'content': '顶一个', 'user_id': 3, 'parent_id_id': None, 'children_contents': []},
        {'nid': 40, 'content': '不错', 'user_id': 2, 'parent_id_id': None, 'children_contents': []},
        {'nid': 42, 'content': '的深V就能看见谁像你', 'user_id': 3, 'parent_id_id': None, 'children_contents': []},
        {'nid': 43, 'content': 'asdasd', 'user_id': 1, 'parent_id_id': None, 'children_contents': []},
        {'nid': 44, 'content': 'a阿萨德', 'user_id': 2, 'parent_id_id': None, 'children_contents': []},
        {'nid': 45, 'content': '阿萨德sadas', 'user_id': 2, 'parent_id_id': None, 'children_contents': []},
        {'nid': 46, 'content': '阿萨德sadas', 'user_id': 2, 'parent_id_id': None, 'children_contents': []},
        {'nid': 47, 'content': '阿斯达四大', 'user_id': 2, 'parent_id_id': None, 'children_contents': []},
        {'nid': 48, 'content': '阿斯达四大啊实打实大声道按时的', 'user_id': 2, 'parent_id_id': None, 'children_contents': []},
        {'nid': 49, 'content': '撒大声地阿萨德阿萨德阿萨德按时打算打手电阿萨德按时的按时打算的阿萨德按时打算的阿萨德按时的',
         'user_id': 1, 'parent_id_id': None,'children_contents': []},
        {'nid': 50, 'content': '阿斯达四大', 'user_id': 1, 'parent_id_id': None, 'children_contents': []},
        {'nid': 51, 'content': '秋风的夙愿', 'user_id': 1, 'parent_id_id': None, 'children_contents': []},
        {'nid': 52, 'content': '小三', 'user_id': 1, 'parent_id_id': None, 'children_contents': []}
    ]


def produce_comment_html(comment_list = comment_list):
    global html
    tpl1 = """
           <div class="comment_item">
               <div class="comment-header">{0}{1}</div>
               <div class="comment-body">{2}</div>
           </div>
       """
    for item in comment_list:
        if item['children_contents']:
            html += tpl1.format(item['user_id'], item['content'].strip(), produce_comment_html(comment_list=item["children_contents"]))
        else:
            html += tpl1.format(item['user_id'], item['content'].strip(), '')

    return html

