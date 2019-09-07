import sys

def load_poke(filename):
    '''从文件中加载poke_dict'''
    file = open(filename, 'r', encoding='utf-8')
    content = file.read()
    file.close()

    poke_dict = {}
    line_list = content.split('\n')
    for line in line_list:
        field_list = line.split('\t')
        if len(field_list) == 4:
            key = field_list[1]
            url = 'https://wiki.52poke.com/wiki/' + key
            poke_dict[key] = url + '\t' + line
    return poke_dict

def get_input_poke_name():
    '''获取输入的宝可梦名称'''
    if len(sys.argv) != 2:
        return None

    poke_name = sys.argv[1]
    return poke_name

def search(poke_name, poke_dict):
    '''查找宝可梦'''
    if poke_name in poke_dict:
        value = poke_dict[poke_name]
        field_list = value.split('\t')
        url, id, chinese_name, japan_name, english_name = field_list
        return {
            '网址': url,
            '编号': id,
            '中文': chinese_name,
            '日文名': japan_name,
            '英文名': english_name
        }

    return None

if __name__ == '__main__':
    # 1 加载宝可梦列表
    poke_dict = load_poke('poke.txt')

    # 2 获取输入的宝可梦
    poke_name = get_input_poke_name()
    if poke_name is None:
        print('缺少宝可梦名称')
        exit(0)

    # 3 查找宝可梦
    result = search(poke_name, poke_dict)
    if result is None:
        print('未找到宝可梦：', poke_name)
        exit(0)

    # 4 输出找到的宝可梦
    print('查找到宝可梦：', poke_name)
    print('----------')
    for key in result:
        value = result[key]
        print(key, ':', value)