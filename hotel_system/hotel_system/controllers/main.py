"""
    main.py
    This is the main application file for the Hotel Reservation system 
"""
from .tester import Tester
      
"""
Main working platform
"""
def start_app():
    test_app = Tester()
    test_app.fill_test()

start_app()
