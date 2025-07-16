import unittest
import random
from game import Game

class TestGoldenBall(unittest.TestCase):
    def setUp(self):
        self.game = Game()
        # Set random seed for consistent testing
        random.seed(42)

    def test_golden_ball_generation(self):
        """Test that golden balls are generated with correct probability"""
        golden_balls = 0
        total_balls = 1000
        
        for _ in range(total_balls):
            # Simulate getting multi-ball powerup
            ball = self.game._create_new_ball()
            if hasattr(ball, 'is_golden') and ball.is_golden:
                golden_balls += 1
        
        # Should be approximately 10% golden balls
        self.assertAlmostEqual(golden_balls / total_balls, 0.1, delta=0.02)

    def test_golden_ball_speed(self):
        """Test that golden balls have correct speed multiplier"""
        # Create a golden ball
        ball = self.game._create_new_ball()
        ball.is_golden = True
        
        # Calculate speed
        speed = (ball.dx**2 + ball.dy**2)**0.5
        normal_speed = 5  # Base speed of normal balls
        
        # Golden ball should be roughly 1.5x faster
        self.assertAlmostEqual(speed / normal_speed, 1.5, delta=0.1)

    def test_golden_ball_brick_destruction(self):
        """Test that golden balls can destroy any brick type"""
        # Create a golden ball
        ball = self.game._create_new_ball()
        ball.is_golden = True
        
        # Test against different brick types
        brick_types = ['normal', 'metal', 'magnetic', 'teleport', 'explosive']
        for brick_type in brick_types:
            brick = self.game._create_brick(brick_type)
            self.assertTrue(self.game._can_ball_destroy_brick(ball, brick))

if __name__ == '__main__':
    unittest.main() 