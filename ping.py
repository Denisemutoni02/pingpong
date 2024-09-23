import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFrame
from PyQt5.QtGui import QPainter, QColor, QBrush
from PyQt5.QtCore import Qt, QTimer, QRect

class PingPongGame(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Ping Pong Game with Background')
        self.setGeometry(100, 100, 800, 400)

        # Game variables
        self.ball_x = 390
        self.ball_y = 190
        self.ball_dx = 5
        self.ball_dy = 5
        self.ball_size = 20
        self.paddle_width = 15
        self.paddle_height = 100
        self.paddle1_x = 30
        self.paddle1_y = 150
        self.paddle2_x = 755
        self.paddle2_y = 150
        self.paddle_speed = 20

        # Timer for ball movement
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_game)
        self.timer.start(30)  # update every 30 ms

    def update_game(self):
        # Update ball position
        self.ball_x += self.ball_dx
        self.ball_y += self.ball_dy

        # Ball collision with top and bottom
        if self.ball_y <= 0 or self.ball_y + self.ball_size >= self.height():
            self.ball_dy = -self.ball_dy

        # Ball collision with paddles
        if self.ball_x <= self.paddle1_x + self.paddle_width and \
           self.paddle1_y < self.ball_y < self.paddle1_y + self.paddle_height:
            self.ball_dx = -self.ball_dx

        if self.ball_x + self.ball_size >= self.paddle2_x and \
           self.paddle2_y < self.ball_y < self.paddle2_y + self.paddle_height:
            self.ball_dx = -self.ball_dx

        # Ball out of bounds (reset ball)
        if self.ball_x <= 0 or self.ball_x >= self.width():
            self.ball_x = 390
            self.ball_y = 190
            self.ball_dx = -self.ball_dx

        self.update()

    def keyPressEvent(self, event):
        # Paddle 1 movement (W and S keys)
        if event.key() == Qt.Key_W and self.paddle1_y > 0:
            self.paddle1_y -= self.paddle_speed
        if event.key() == Qt.Key_S and self.paddle1_y + self.paddle_height < self.height():
            self.paddle1_y += self.paddle_speed

        # Paddle 2 movement (Up and Down arrow keys)
        if event.key() == Qt.Key_Up and self.paddle2_y > 0:
            self.paddle2_y -= self.paddle_speed
        if event.key() == Qt.Key_Down and self.paddle2_y + self.paddle_height < self.height():
            self.paddle2_y += self.paddle_speed

    def paintEvent(self, event):
        painter = QPainter(self)

        # Draw background
        painter.setBrush(QBrush(QColor(50, 50, 150)))  # Background color
        painter.drawRect(self.rect())

        # Draw paddles
        painter.setBrush(QBrush(QColor(255, 255, 255)))
        painter.drawRect(self.paddle1_x, self.paddle1_y, self.paddle_width, self.paddle_height)
        painter.drawRect(self.paddle2_x, self.paddle2_y, self.paddle_width, self.paddle_height)

        # Draw ball
        painter.setBrush(QBrush(QColor(255, 255, 255)))
        painter.drawEllipse(self.ball_x, self.ball_y, self.ball_size, self.ball_size)

def main():
    app = QApplication(sys.argv)
    game = PingPongGame()
    game.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
