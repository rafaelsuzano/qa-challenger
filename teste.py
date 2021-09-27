# -*- coding: utf-8 -*-
import qa_challenger
import os
import unittest
import HtmlTestRunner




FP =  unittest.defaultTestLoader.loadTestsFromTestCase(qa_challenger.Test_qa_challenger)
suite = unittest.TestSuite([FP])

suite = unittest.TestSuite([suite])
html_runner = HtmlTestRunner.HTMLTestRunner(report_title='QA-challenger', descriptions=u"Cenarios de teste",
                                         combine_reports=True, output="C:\\Users\\user\AppData\\Local\Jenkins\\.jenkins\workspace\qa-challenger\\",
                                         add_timestamp=False,
                                         report_name="QA-challenger",
                                         failfast = False,
                                         buffer = True)


html_runner.run(suite)

if __name__ == '__main__':
    unittest.main(verbosity=2)

