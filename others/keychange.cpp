#include <iostream>
#include <string>
using namespace std;

#define cmax 26 // character max��ĸ����

int main()
{
    string ori, key, sec; // ���ģ���Կ������
    // ��������
    cout << "���������ģ�";
    cin >> ori;
    int lenori = ori.length(); // ���ĳ���
    // ת��д
    for (int i = 0; i < lenori; i++)
        if ((int)ori[i] > 90)
            ori[i] -= (char)32;
    cout << "���ĳ���Ϊ��" << lenori << endl;
    // ����ؼ��ֲ�������Կ
    cout << "������ؼ���:";
    cin >> key;
    int lenkey = key.length(); // �ؼ��ֳ���
    // ת��д
    for (int i = 0; i < lenkey; i++)
        if ((int)key[i] > 90)
            key[i] -= (char)32;
    for (int i = lenkey; i < lenori; i++)
        key += key[(i - lenkey) % lenkey];
    cout << "��ԿΪ��" << key << endl;
    // ���ƫ��ֵ
    cout << "����ƫ��ֵ��";
    int num;
    cin >> num;
    cout << "ƫ��ֵΪ��" << num << endl;
    // ��������
    cout << "�����Ϊ��" << endl;
    for (int i = 0; i < cmax; i++)
    {
        for (int j = 0; j < cmax; j++)
            cout << (char)('A' + (i + j + num) % cmax) << ' ';
        cout << endl;
    }
    // �������Ĳ��������
    for (int i = 0; i < lenori; i++)
        sec += (char)('A' + ((int)ori[i] + (int)key[i] - 65 * 2 + num) % cmax);
    // ӳ�����������key[i]��ori[i]�Լ�ƫ��ֵ
    cout << "����Ϊ��" << sec << endl;
    // ����
    for (int i = 0; i < lenori; i++)
        // ����ӳ�����������key[i]�Լ�ƫ��ֵ����cmax��ֹ���ָ�����cppȡģ��������ѧ��ͬ��
        sec[i] = (char)('A' + (sec[i] - key[i] - num + cmax) % cmax);
    cout << "���ܺ�����Ϊ��" << sec << endl;

    int _ = 0;
    return (0 ^ _ ^ 0);
}
