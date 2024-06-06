from common import TEST_LIST, TEST_LIST2, TEST_LIST3


class RoadRange:
    def __init__(self, start_index: int, end_index: int, range_data: list[int]) -> None:
        self.start_index: int = start_index
        self.end_index: int = end_index
        self.range_data: list[int] = range_data
        self.average = self.calculate_average()

    def calculate_average(self):
        return sum(self.range_data) / len(self.range_data) if self.range_data else 0

    def get_road_avg(self) -> int:
        return self.average

    def __str__(self) -> str:
        return (
            rf"range: {self.start_index} - {self.end_index}, avg: {self.get_road_avg()}"
        )


def func(
    road_range: int,
    source_data: list[int],
    min_score: int,
    max_score: int,
    error_count: int,
):
    result_list = []
    n = len(source_data)
    if n < road_range:
        return result_list  # 如果数据长度小于计算范围，直接返回空列表

    # 初始化滑动窗口和错误计数
    current_window = []
    count = 0

    # 先填充窗口
    for i in range(road_range):
        if source_data[i] < min_score or source_data[i] > max_score:
            count += 1
        current_window.append(source_data[i])
    # 如果初始窗口符合条件，加入结果列表
    if count <= error_count:
        result_list.append(RoadRange(0, road_range - 1, current_window.copy()))

    # 滑动窗口遍历剩余元素
    for i in range(road_range, n):
        # 移除窗口中的第一个元素，并更新错误计数
        pop_element = current_window.pop(0)
        if pop_element < min_score or pop_element > max_score:
            count -= 1

        # 添加新的元素到窗口
        new_element = source_data[i]
        current_window.append(new_element)
        if new_element < min_score or new_element > max_score:
            count += 1

        # 如果当前窗口符合条件，加入结果列表
        if count <= error_count:
            result_list.append(RoadRange(i - road_range + 1, i, current_window.copy()))

    return result_list


def main():
    result = func(60, TEST_LIST, 0, 100, 5)
    # get max avg from resule
    max_avg = max(result, key=lambda x: x.get_road_avg())
    print(max_avg)


if __name__ == "__main__":
    main()
