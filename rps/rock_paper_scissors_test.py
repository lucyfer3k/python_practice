#!/usr/bin/env python3
from rock_paper_scissors import winner_rps
import unittest

class TestRPS(unittest.TestCase):
    def test_basic_player_1(self):
        testcase_player = 1
        testcase_pc = 0
        expected = "Player won"
        self.assertEqual(winner_rps(testcase_player, testcase_pc), expected)

    def test_basic_player_2(self):
        testcase_player = 2
        testcase_pc = 1
        expected = "Player won"
        self.assertEqual(winner_rps(testcase_player, testcase_pc), expected)

    def test_basic_player_3(self):
        testcase_player = 0
        testcase_pc = 2
        expected = "Player won"
        self.assertEqual(winner_rps(testcase_player, testcase_pc), expected)

    def test_basic_pc_1(self):
        testcase_player = 0
        testcase_pc = 1
        expected = "PC won"
        self.assertEqual(winner_rps(testcase_player, testcase_pc), expected)
    
    def test_basic_pc_2(self):
        testcase_player = 1
        testcase_pc = 2
        expected = "PC won"
        self.assertEqual(winner_rps(testcase_player, testcase_pc), expected)
                            
    def test_basic_pc_3(self):
        testcase_player = 2
        testcase_pc = 0
        expected = "PC won"
        self.assertEqual(winner_rps(testcase_player, testcase_pc), expected)

    def test_basic_draw_1(self):    
        testcase_player = 0
        testcase_pc = 0     
        expected = "Draw"    
        self.assertEqual(winner_rps(testcase_player, testcase_pc), expected)
    
    def test_basic_draw_2(self):    
        testcase_player = 1 
        testcase_pc = 1   
        expected = "Draw"    
        self.assertEqual(winner_rps(testcase_player, testcase_pc), expected)

    def test_basic_draw_3(self):    
        testcase_player = 2
        testcase_pc = 2
        expected = "Draw"    
        self.assertEqual(winner_rps(testcase_player, testcase_pc), expected)

    def test_empty(self):
        testcase_player = ""
        testcase_pc = ""
        expected = "Error"
        self.assertEqual(winner_rps(testcase_player, testcase_pc), expected)

    def test_out_of_bounds(self):
        testcase_player = 3
        testcase_pc = 0
        expected = "Error"
        self.assertEqual(winner_rps(testcase_player, testcase_pc), expected)

unittest.main()
