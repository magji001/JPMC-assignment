import unittest

import UpdatingService
import seatInitializer
from unittest import mock
from unittest.mock import patch
import io
from contextlib import redirect_stdout
import io


class MyTestCase(unittest.TestCase):

    ##Test for successful booking, seats should be updated and SUCCESS gets written to STDOUT
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_book_seat_success(self, mock_stdout):
        dummy_UpdatingService = UpdatingService
        dummy_UpdatingService.seats = {'A':
                     { 0:'E' , 1: 'E', 2: 'E'}
                 }
        dummy_UpdatingService.updateSeats('BOOK', 'A1', 2)
        self.assertEqual(dummy_UpdatingService.seats, {'A':
                                                           { 0:'E' , 1: 'B', 2: 'B'}
                                                       }
                         )
        assert mock_stdout.getvalue() == 'SUCCESS\n'
        seatInitializer.resetSeats()

    ##Test for booking failure, FAIL gets written to STDOUT
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_book_seat_failure(self, mock_stdout):
        dummy_UpdatingService = UpdatingService
        dummy_UpdatingService.seats = {'A':
                                           { 0:'B' , 1: 'B', 2: 'B'}
                                       }
        dummy_UpdatingService.updateSeats('BOOK', 'A1', 2)
        self.assertEqual(dummy_UpdatingService.seats, {'A':
                                                           { 0:'B' , 1: 'B', 2: 'B'}
                                                       }
                         )

        assert mock_stdout.getvalue() == 'FAIL\n'

        seatInitializer.resetSeats()

    ##Test for successful cancellation, seats should be updated and SUCCESS gets written to STDOUT
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_cancel_seat_success(self, mock_stdout):
        dummy_UpdatingService = UpdatingService
        dummy_UpdatingService.seats = {'A':
                                           { 0:'E' , 1: 'B', 2: 'B'}
                                       }
        dummy_UpdatingService.updateSeats('CANCEL', 'A1', 2)
        self.assertEqual(dummy_UpdatingService.seats, {'A':
                                                           { 0:'E' , 1: 'E', 2: 'E'}
                                                       }
                         )
        assert mock_stdout.getvalue() == 'SUCCESS\n'
        seatInitializer.resetSeats()

    ##Test for cancellation failure, FAIL gets written to STDOUT
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_cancel_seat_failure(self, mock_stdout):
        dummy_UpdatingService = UpdatingService
        dummy_UpdatingService.seats = {'A':
                                           { 0:'E' , 1: 'E', 2: 'E'}
                                       }
        dummy_UpdatingService.updateSeats('CANCEL', 'A1', 2)
        self.assertEqual(dummy_UpdatingService.seats, {'A':
                                                           { 0:'E' , 1: 'E', 2: 'E'}
                                                       }
                         )
        assert mock_stdout.getvalue() == 'FAIL\n'
        seatInitializer.resetSeats()


if __name__ == '__main__':
    unittest.main()
