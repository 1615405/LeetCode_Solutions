class Solution:
    def maximum69Number(self, num: int) -> int:
        num_str = str(num)  # 将数字转换为字符串以便遍历
        num_list = list(num_str)  # 将字符串转换为字符列表以便修改

        # 遍历字符列表
        for i in range(len(num_list)):
            # 如果找到 '6'，将其翻转为 '9'，然后停止遍历
            if num_list[i] == '6':
                num_list[i] = '9'
                break

        # 将字符列表重新组合成字符串，并转换为整数
        return int("".join(num_list))
