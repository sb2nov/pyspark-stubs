from mypy.test.data import DataDrivenTestCase, DataSuite
from mypy.test.testcheck import TypeCheckSuite


TypeCheckSuite.files = [
        "context.test",
        "ml-evaluation.test",
        "ml-param.test",
        "ml-readable.test",
        "resultiterable.test",
        "sql-column.test",
        "sql-readwriter.test",
        "sql-udf.test",
    ]
