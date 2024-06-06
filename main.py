from numpy import mean
from common import TEST_LIST, TEST_LIST2


class RoadRange:

    def __init__(self, start_index: int, end_index: int, range_data: list[int]) -> None:
        self.start_index: int = start_index
        self.end_index: int = end_index
        self.range_data: list[int] = range_data

    def get_road_avg(self) -> int:
        return mean(self.range_data)

    def __str__(self) -> str:
        return (
            rf"range: {self.start_index} - {self.end_index}, avg: {self.get_road_avg()}"
        )


def func(road_range: int, source_data: list[int], min_score: int, error_count: int):
    """
    Function description.

    :param road_range: 计算范围.
    :param source_data: 源数据.
    :param min_score: 最小分数.
    :param error_count: 错误次数.

    return:

    """
    result_list = []
    # 右指针遍历,判断每一个元素是否大于 min_score,每有一个元素小于min_score,就计数一次,当计数大于error_count,左指针向右移动一位.如果当前右指针元素大于等min_score或者计数小于error_count,则将当前右指针元素添加到tmp_list中.
    for left_index in range(len(source_data) - road_range):
        # 创建一个空列表,用于暂存数据
        tmp_list = []
        # 计数小于min_score的次数
        count = 0
        for i in range(road_range):
            right_index = left_index + i
            current_data = source_data[right_index]
            # 如果当前数据小于min_score,且count在error_count以内,则计数加一,否则跳过改组数据
            if current_data < min_score:
                if count < error_count:
                    count += 1
                else:
                    continue
            else:
                tmp_list.append(current_data)
        left_index += 1
        # 判断tmp_list长度是否为road_range,为则创建一个RoadRange对象,并添加到result_list中
        if len(tmp_list) == road_range:
            result_list.append(RoadRange(left_index, right_index, tmp_list))
    return result_list


def main():
    result = func(60, TEST_LIST, 90, 5)
    for i in result:
        print(i)


if __name__ == "__main__":
    main()
