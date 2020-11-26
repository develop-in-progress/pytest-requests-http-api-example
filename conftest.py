import logging
import allure
import pytest
from _pytest.python import Function
from _pytest.runner import CallInfo


# @pytest.hookimpl(hookwrapper=True, tryfirst=True)
# def pytest_exception_interact(node, call: CallInfo, report):
#     logger = logging.getLogger(__name__)
#     if report.failed:
#         logger.error(call.excinfo)


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()
    marker = item.get_closest_marker("ui")
    if marker:
        if rep.when == "call" and rep.failed:  # we only look at actual failing test calls, not setup/teardown
            try:
                allure.attach(item.instance.driver.get_screenshot_as_png(),
                              name=item.name,
                              attachment_type=allure.attachment_type.PNG)
            except Exception as e:
                print(e)
