#-*coding:utf-8*-
from collections import defaultdict

def etree_to_dict(t):       # tΪxml��ʽ�ַ�
    d = {t.tag: {} if t.attrib else None}       # dΪ������Ŀ���ֵ�
                                                # t.tag������Ϊ�ֵ��һ��
    children = list(t)      # ���¿�ʼ�ݹ������������ֱ��Ҷ�ӽڵ�
    if children:        # �жϽڵ��Ƿ�Ϊ�գ��ݹ�߽�����
        dd = defaultdict(list)
        for dc in map(etree_to_dict, children):     # �ݹ��������
            for k, v in dc.iteritems():
                dd[k].append(v)     # ���ֵ��м������¶��ϵĽ��
        d = {t.tag: {k:v[0] if len(v) == 1 else v for k, v in dd.iteritems()}}      # ��Ҷ�ӽڵ�Ĵ������
    if t.attrib:        # ��������,������ڴ��������е� ȫ����ǰ׺@
        d[t.tag].update(('@' + k, v) for k, v in t.attrib.iteritems())
    if t.text:      # ����textֵ
        text = t.text.strip()       # ɾ���ո�
        if children or t.attrib:        #
                d[t.tag]['#text'] = text
        else:
            d[t.tag] = text     # txetֱֵ�ӷ�װΪt.tag
    return d        # return
