import random
import math

class Game:
    def _create_new_ball(self):
        """Create a new ball with random direction and speed"""
        # Calculate random angle between -60 and 60 degrees
        angle = (random.random() - 0.5) * math.pi / 1.5  # -60 to 60 degrees
        base_speed = 5  # Base speed for normal balls
        
        # 10% chance to create a golden ball
        is_golden = random.random() < 0.1
        if is_golden:
            base_speed *= 1.5  # Golden balls are 1.5x faster
        
        ball = {
            'x': self.paddle['x'] + self.paddle['width'] / 2,
            'y': self.paddle['y'] - 10,
            'radius': 10,
            'dx': math.sin(angle) * base_speed,
            'dy': -math.cos(angle) * base_speed,
            'is_golden': is_golden
        }
        return ball

    def _can_ball_destroy_brick(self, ball, brick):
        """Check if a ball can destroy a brick"""
        # Golden balls can destroy any brick
        if ball.get('is_golden', False):
            return True
        
        # Normal balls can't destroy metal bricks
        if brick.get('type') == 'metal':
            return False
        
        return True

    def _handle_brick_collision(self, ball, brick):
        """Handle collision between ball and brick"""
        if not self._can_ball_destroy_brick(ball, brick):
            return False
        
        # Golden balls destroy bricks in one hit
        if ball.get('is_golden', False):
            brick['visible'] = False
            self.bricks_broken += 1
            self.score += brick['hits'] * 10
            self._create_particles_from_brick(brick)
            return True
        
        # Normal ball collision logic
        if brick['hits'] == 2:
            if not brick['hit']:
                brick['hit'] = True
            else:
                brick['visible'] = False
                self.bricks_broken += 1
                self._create_particles_from_brick(brick)
        else:
            brick['visible'] = False
            self.bricks_broken += 1
            self._create_particles_from_brick(brick)
        
        self.score += brick['hits'] * 10
        return True

    def _draw_ball(self, ball):
        """Draw a ball with appropriate color and effects"""
        ctx = self.ctx
        
        # Create gradient for 3D effect
        ball_gradient = ctx.createRadialGradient(
            ball['x'] - ball['radius'] * 0.3, ball['y'] - ball['radius'] * 0.3, ball['radius'] * 0.1,
            ball['x'], ball['y'], ball['radius']
        )
        
        if ball.get('is_golden', False):
            # Golden ball gradient
            ball_gradient.addColorStop(0, '#ffff00')  # Bright yellow at highlight
            ball_gradient.addColorStop(0.5, '#ffcc00')  # Gold in middle
            ball_gradient.addColorStop(1, '#ff9900')  # Darker gold at edges
        else:
            # Normal ball gradient
            ball_gradient.addColorStop(0, '#ffffff')  # Bright white at highlight
            ball_gradient.addColorStop(0.5, '#cccccc')  # Light gray in middle
            ball_gradient.addColorStop(1, '#999999')  # Darker gray at edges

        # Draw main ball body
        ctx.beginPath()
        ctx.arc(ball['x'], ball['y'], ball['radius'], 0, math.pi * 2)
        ctx.fillStyle = ball_gradient
        ctx.fill()

        # Draw highlight
        ctx.beginPath()
        ctx.arc(
            ball['x'] - ball['radius'] * 0.3,
            ball['y'] - ball['radius'] * 0.3,
            ball['radius'] * 0.4,
            0, math.pi * 2
        )
        ctx.fillStyle = 'rgba(255, 255, 255, 0.4)'
        ctx.fill()

        # Draw shadow
        ctx.beginPath()
        ctx.arc(
            ball['x'] + ball['radius'] * 0.2,
            ball['y'] + ball['radius'] * 0.2,
            ball['radius'] * 0.3,
            0, math.pi * 2
        )
        ctx.fillStyle = 'rgba(0, 0, 0, 0.2)'
        ctx.fill() 