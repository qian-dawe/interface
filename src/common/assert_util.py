# 封装断言
from requests import Response
from src.common.logs import log


def assert_result(response: Response, expected: str) -> None:
    """
    断言方法
    :param response: 实际响应对象
    :param expected: 预期响应内容，从excel中或者yaml读取、或者手动传入
    return None
    """
    if expected is None:
        log.info("当前用例无断言！")
        return

    if isinstance(expected, str):
        expect_dict = eval(expected)
    else:
        expect_dict = expected
    index = 0
    for k, v in expect_dict.items():
        # 获取需要断言的实际结果部分
        for _k, _v in v.items():
            if _k == "http_code":
                actual = response.status_code
            else:
                if response_type(response) == "json":
                    actual = json_extractor(response.json(), _k)
                else:
                    actual = re_extract(response.text, _k)
            index += 1
            log.info(f'第{index}个断言数据,实际结果:{actual} | 预期结果:{_v} 断言方式：{k}')
            allure_step(f'第{index}个断言数据', f'实际结果:{actual} = 预期结果:{v}')
            try:
                if k == "eq":  # 相等
                    assert actual == _v
                elif k == "in":  # 包含关系
                    assert _v in actual
                elif k == "gt":  # 判断大于，值应该为数值型
                    assert actual > _v
                elif k == "lt":  # 判断小于，值应该为数值型
                    assert actual < _v
                elif k == "not":  # 不等于，非
                    assert actual != _v
                else:
                    log.exception(f"判断关键字: {k} 错误！")
            except AssertionError:
                raise AssertionError(f'第{index}个断言失败 -|- 断言方式：{k} 实际结果:{actual} || 预期结果: {_v}')
