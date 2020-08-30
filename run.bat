pytest -v -s testCases\test_login.py --browser chrome
pytest -s -v -m "sanity" --html=Reports\report.html testCases\test_addCustomer.py --browser chrome
rem pytest -s -v -m "sanity or regression" --html=Reports/report.html testCases/ --browser chrome