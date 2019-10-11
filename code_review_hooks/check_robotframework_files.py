import os

from robot.model import SuiteVisitor


class BaseChecker(SuiteVisitor):
    id = 0
    severity = 'I'
    name = 'base'

    def __init__(self, findings):
        super().__init__()
        self.findings = findings

    def add_finding(self, category, node, msg):
        self.findings.add((category, node, msg))


class NamingChecker(BaseChecker):
    def start_suite(self, suite):
        if '.' in os.path.basename(suite.source):
            print('suite name should not contain "."')

    def start_test(self, test):
        if '.' in test.name:
            print('test name should not contain ".')

    def check_suite_variable_name(self, variable):
        pass


class StructureChecker(BaseChecker):
    def start_suite(self, suite):
        pass

    def start_test(self, test):
        pass

    def check_setup_teardown_in_suite(self, suite):
        pass


class TagsCheck(BaseChecker):
    def start_test(self, test):
        pass

    def get_tags(self, test):
        pass


class KeywordInvalidUsageChecker(BaseChecker):
    def start_keyword(self, keyword):
        pass


class CaseDuplicateChecker(BaseChecker):
    def start_test(self, test):
        pass


def main():
    raise SystemExit(
        'check-robotframework is un-implemented.'
    )


if __name__ == '__main__':
    exit(main())
